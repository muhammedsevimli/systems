#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The lookout's scanner.

Reads the public sources in company/radar/sources.md and writes the items from the last N days
to company/radar/raw-<YYYY-MM-DD>.json. The lookout writes its report from that file.

- Read only (HTTP GET). Sends no data anywhere, logs in nowhere, needs no API key.
- Python 3 standard library only. Works the same on Windows, Mac and Linux.
- If a source does not open, it skips it, writes the error to the file and carries on.

Usage (from the project folder):
  python bin/lookout_scan.py                        scan
  python bin/lookout_scan.py --days 7               scan the last 7 days
  python bin/lookout_scan.py --find-channel <url>   finds the channel_id from a YouTube channel URL
  python bin/lookout_scan.py --try <type> <address> tries one source, writes no file
On Mac and Linux type `python3` instead of `python`.
"""

import argparse
import datetime as dt
import email.utils
import gzip
import html
import json
import re
import ssl
import statistics
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RADAR = ROOT / "company" / "radar"
SOURCES = RADAR / "sources.md"

BROWSER = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
           "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
REDDIT_AGENT = "agent-company-lookout/1.0 (public RSS reader)"
TIMEOUT = 20
MAX_BODY = 6_000_000
MAX_PER_SOURCE = 15
DEFAULT_DAYS = 4
RETRY_WAIT = 5

TYPES = {
    "youtube": "youtube", "yt": "youtube",
    "news": "news", "google": "news",
    "rss": "rss", "atom": "rss", "feed": "rss",
    "site": "site", "blog": "site",
    "sitemap": "sitemap",
    "reddit": "reddit",
    "link": "link", "manual": "link",
}

LOGIN_WALLED = ("instagram.com", "facebook.com", "fb.com", "threads.net", "threads.com", "linkedin.com")


# ---------------------------------------------------------------- helpers

def utf8_output():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def now():
    return dt.datetime.now(dt.timezone.utc)


def fetch(url, agent=BROWSER):
    """One GET request. Returns the body as bytes. There is no data parameter: no POST is possible."""
    host = urllib.parse.urlsplit(url).netloc.lower()
    headers = {"User-Agent": agent, "Accept-Language": "en-US,en;q=0.9"}
    if host.endswith("youtube.com") or host.endswith("google.com"):
        # read-only cookies so we do not land on the EU consent page
        headers["Cookie"] = "CONSENT=YES+1; SOCS=CAI"
    request = urllib.request.Request(url, headers=headers, method="GET")
    for attempt in (1, 2):
        try:
            return _read(request)
        except urllib.error.HTTPError as e:
            if attempt == 2 or e.code not in (429, 500, 502, 503, 504):
                raise
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            if attempt == 2 or "CERTIFICATE_VERIFY_FAILED" in str(e):
                raise
        time.sleep(RETRY_WAIT)  # temporary error (busy, connection dropped): try once more


def _read(request):
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        body = response.read(MAX_BODY)
        encoding = (response.headers.get("Content-Encoding") or "").lower()
        if "gzip" in encoding:
            body = gzip.decompress(body)
        elif "deflate" in encoding:
            body = zlib.decompress(body)
        return body, response.geturl()


def text(body):
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            return body.decode(enc)
        except UnicodeDecodeError:
            continue
    return body.decode("utf-8", errors="replace")


def error_text(e):
    if isinstance(e, ValueError) and not isinstance(e, UnicodeError):
        return str(e)
    if isinstance(e, urllib.error.HTTPError):
        return f"HTTP {e.code}"
    if isinstance(e, urllib.error.URLError):
        reason = e.reason
        if isinstance(reason, ssl.SSLCertVerificationError) or "CERTIFICATE_VERIFY_FAILED" in str(reason):
            return ("SSL certificate could not be verified. On Mac, run 'Install Certificates.command' "
                    "in the Python folder once.")
        return f"could not connect ({reason})"
    if isinstance(e, ET.ParseError):
        return "feed could not be read (not XML or broken)"
    if isinstance(e, TimeoutError):
        return f"timed out ({TIMEOUT} s)"
    return f"{type(e).__name__}: {e}"


def plain(s, limit=400):
    if not s:
        return ""
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= limit else s[: limit - 1].rstrip() + "…"


ISO = re.compile(r"^(\d{4})-(\d{2})-(\d{2})(?:[T ](\d{2}):(\d{2})(?::(\d{2}))?(?:\.\d+)?)?\s*(Z|[+-]\d{2}:?\d{2})?$")


def parse_date(s):
    if not s:
        return None
    s = s.strip()
    m = ISO.match(s)
    if m:
        y, mo, d, h, mi, se, zone = m.groups()
        tz = dt.timezone.utc
        if zone and zone != "Z":
            sign = 1 if zone[0] == "+" else -1
            digits = zone[1:].replace(":", "")
            tz = dt.timezone(sign * dt.timedelta(hours=int(digits[:2]), minutes=int(digits[2:])))
        return dt.datetime(int(y), int(mo), int(d), int(h or 0), int(mi or 0), int(se or 0), tzinfo=tz)
    try:
        t = email.utils.parsedate_to_datetime(s)
        if t.tzinfo is None:
            t = t.replace(tzinfo=dt.timezone.utc)
        return t
    except (TypeError, ValueError, IndexError):
        return None


def local(tag):
    return tag.rsplit("}", 1)[-1] if isinstance(tag, str) else ""


def xml_root(body):
    body = re.sub(rb"<!DOCTYPE[^>]*>", b"", body, count=1)
    return ET.fromstring(body)


def child(el, name):
    for c in el:
        if local(c.tag) == name:
            return c
    return None


def child_text(el, *names):
    for name in names:
        c = child(el, name)
        if c is not None and (c.text or "").strip():
            return c.text.strip()
    return ""


# ---------------------------------------------------------------- feed reader

def feed_items(body):
    """One reader for RSS 2.0, RSS 1.0 and Atom. Also picks up YouTube view counts."""
    root = xml_root(body)
    root_name = local(root.tag)
    if root_name in ("urlset", "sitemapindex"):
        raise ValueError("this address is a sitemap, set its type to 'sitemap'")
    items = []
    for el in root.iter():
        name = local(el.tag)
        if name not in ("item", "entry"):
            continue
        title = child_text(el, "title")
        link = ""
        for c in el:
            if local(c.tag) == "link":
                if c.get("href") and c.get("rel", "alternate") == "alternate":
                    link = c.get("href")
                    break
                if (c.text or "").strip():
                    link = c.text.strip()
                    break
        date = child_text(el, "pubDate", "published", "date", "updated", "issued")
        summary = child_text(el, "description", "summary", "content", "encoded")
        item = {"title": plain(title, 200), "link": link, "date_raw": date, "summary": plain(summary)}
        source = child(el, "source")
        if source is not None and (source.text or "").strip():
            item["outlet"] = source.text.strip()
        group = child(el, "group")
        if group is not None:
            if not item["summary"]:
                item["summary"] = plain(child_text(group, "description"))
            community = child(group, "community")
            if community is not None:
                stats = child(community, "statistics")
                stars = child(community, "starRating")
                if stats is not None and stats.get("views", "").isdigit():
                    item["views"] = int(stats.get("views"))
                if stars is not None and stars.get("count", "").isdigit():
                    item["likes"] = int(stars.get("count"))
        vid = child_text(el, "videoId")
        if vid:
            item["video_id"] = vid
            if "/shorts/" in link:
                item["format"] = "shorts"
        items.append(item)
    return items


def sitemap_items(body, depth=0):
    root = xml_root(body)
    root_name = local(root.tag)
    if root_name == "sitemapindex":
        if depth > 0:
            return []
        subs = []
        for sm in root:
            if local(sm.tag) != "sitemap":
                continue
            loc = child_text(sm, "loc")
            last = parse_date(child_text(sm, "lastmod"))
            if loc:
                subs.append((last or dt.datetime(1970, 1, 1, tzinfo=dt.timezone.utc), loc))
        subs.sort(reverse=True)
        items = []
        for _, loc in subs[:3]:
            try:
                b, _u = fetch(loc)
                items.extend(sitemap_items(b, depth + 1))
            except Exception:
                continue
        return items
    items = []
    for u in root:
        if local(u.tag) != "url":
            continue
        loc = child_text(u, "loc")
        if not loc:
            continue
        piece = urllib.parse.urlsplit(loc).path.rstrip("/").rsplit("/", 1)[-1]
        title = urllib.parse.unquote(piece).replace("-", " ").replace("_", " ").strip() or loc
        items.append({"title": title[:200], "link": loc, "date_raw": child_text(u, "lastmod"),
                      "summary": "", "note": "title taken from the address (the sitemap has no titles)"})
    return items


# ---------------------------------------------------------------- source types

CHANNEL_PATTERNS = [
    r'<link rel="canonical" href="https://www\.youtube\.com/channel/(UC[\w-]{22})"',
    r'"externalId":"(UC[\w-]{22})"',
    r'<meta itemprop="identifier" content="(UC[\w-]{22})"',
    r'"browseId":"(UC[\w-]{22})"',
    r'"channelId":"(UC[\w-]{22})"',
]


def find_channel_id(address):
    address = address.strip()
    m = re.search(r"(UC[\w-]{22})", address)
    if m and ("/channel/" in address or "channel_id=" in address or address.startswith("UC")):
        return m.group(1)
    if address.startswith("@"):
        address = "https://www.youtube.com/" + address
    if not address.startswith("http"):
        address = "https://" + address
    body, final = fetch(address)
    if "consent." in final:
        raise ValueError("YouTube redirected to its consent page, channel_id could not be read")
    page = text(body)
    for pattern in CHANNEL_PATTERNS:
        m = re.search(pattern, page)
        if m:
            return m.group(1)
    raise ValueError("no channelId found in the page source")


def youtube_feed(address):
    if "feeds/videos.xml" in address:
        return address
    return "https://www.youtube.com/feeds/videos.xml?channel_id=" + find_channel_id(address)


def news_url(address, days):
    if address.startswith("http"):
        return address
    query = address if "when:" in address else f"{address} when:{days}d"
    return ("https://news.google.com/rss/search?q=" + urllib.parse.quote_plus(query)
            + "&hl=en-US&gl=US&ceid=US:en")


def reddit_url(address):
    if address.startswith("http"):
        return address
    a = address.strip().strip("/")
    if a.startswith("r/"):
        return f"https://www.reddit.com/{a}/new/.rss"
    return "https://www.reddit.com/search.rss?sort=new&q=" + urllib.parse.quote_plus(a)


def find_site_feed(address):
    """Finds the RSS/Atom link on the home page; otherwise tries common paths and the sitemap."""
    if not address.startswith("http"):
        address = "https://" + address
    tried = []
    try:
        body, final = fetch(address)
        page = text(body)
        for tag in re.findall(r"<link[^>]+>", page, flags=re.I):
            if re.search(r'type=["\']application/(rss|atom)\+xml["\']', tag, flags=re.I):
                h = re.search(r'href=["\']([^"\']+)["\']', tag, flags=re.I)
                if h and "comments" not in h.group(1):
                    return "rss", urllib.parse.urljoin(final, html.unescape(h.group(1)))
    except Exception as e:
        tried.append(f"home page: {error_text(e)}")
    base = urllib.parse.urljoin(address if address.endswith("/") else address + "/", "/")
    for path, kind in (("feed", "rss"), ("rss", "rss"), ("feed.xml", "rss"), ("rss.xml", "rss"),
                       ("atom.xml", "rss"), ("sitemap.xml", "sitemap"), ("sitemap_index.xml", "sitemap")):
        u = urllib.parse.urljoin(base, path)
        try:
            body, _ = fetch(u)
            root = xml_root(body)
            name = local(root.tag)
            if name in ("urlset", "sitemapindex"):
                return "sitemap", u
            if name in ("rss", "feed", "RDF"):
                return "rss", u
        except Exception as e:
            tried.append(f"{path}: {error_text(e)}")
    raise ValueError("no feed or sitemap found on the site (" + "; ".join(tried[:3]) + ")")


def read_link(address, note):
    """One link added by hand. Keyless oEmbed for X and TikTok, page title for everything else."""
    host = urllib.parse.urlsplit(address).netloc.lower()
    item = {"title": "", "link": address, "date_raw": "", "summary": "", "manual": True}
    if note:
        item["owner_note"] = note
    try:
        if host.endswith("x.com") or host.endswith("twitter.com"):
            b, _ = fetch("https://publish.twitter.com/oembed?omit_script=1&url=" + urllib.parse.quote(address, safe=""))
            data = json.loads(text(b))
            item["title"] = "X post: " + data.get("author_name", "")
            raw = data.get("html", "")
            p = re.search(r"<p[^>]*>(.*?)</p>", raw, flags=re.S)
            item["summary"] = plain(p.group(1) if p else raw)
            t = re.findall(r">([A-Z][a-z]+ \d{1,2}, \d{4})</a>", raw)
            if t:
                try:
                    item["date_raw"] = dt.datetime.strptime(t[-1], "%B %d, %Y").strftime("%Y-%m-%d")
                except ValueError:
                    pass
            return item
        if host.endswith("tiktok.com"):
            b, _ = fetch("https://www.tiktok.com/oembed?url=" + urllib.parse.quote(address, safe=""))
            data = json.loads(text(b))
            item["title"] = "TikTok: " + data.get("author_name", "")
            item["summary"] = plain(data.get("title", ""))
            return item
        if any(host.endswith(h) for h in LOGIN_WALLED):
            item["unreadable"] = "this site needs a login, only the owner's note is used"
            return item
        if host == "news.google.com":
            item["unreadable"] = ("Google News redirect link; paste the article's own address and its title "
                                  "is read. For now the owner's note is used")
            return item
        b, _ = fetch(address)
        page = text(b)

        def meta(*names):
            for n in names:
                m = re.search(r'<meta[^>]+(?:property|name|itemprop)=["\']' + re.escape(n)
                              + r'["\'][^>]*content=["\']([^"\']*)["\']', page, flags=re.I)
                if m:
                    return html.unescape(m.group(1))
            return ""
        t = re.search(r"<title[^>]*>(.*?)</title>", page, flags=re.S | re.I)
        item["title"] = plain(meta("og:title") or (t.group(1) if t else ""), 200)
        item["summary"] = plain(meta("og:description", "description"))
        item["date_raw"] = meta("article:published_time", "datePublished", "date")
    except Exception as e:
        item["unreadable"] = error_text(e) + "; only the owner's note is used"
    return item


# ---------------------------------------------------------------- source list

def read_sources(path):
    if not path.exists():
        return None, None
    days = None
    sources = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*[-*]?\s*days\s*:\s*(\d+)", line, flags=re.I)
        if m:
            days = int(m.group(1))
            continue
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or set("".join(cells)) <= set("-: "):
            continue
        name, kind, address = cells[0], cells[1].lower(), cells[2].strip("`<> ")
        note = cells[3] if len(cells) > 3 else ""
        if name.lower() in ("name", "who") or kind == "type":
            continue
        if not address or address.startswith("...") or kind not in TYPES:
            continue
        sources.append({"name": name, "type": TYPES[kind], "address": address, "note": note})
    return days, sources


# ---------------------------------------------------------------- scan

def scan_source(s, days, now_t):
    kind, address = s["type"], s["address"]
    status = {"name": s["name"], "type": kind, "address": address}
    if kind == "link":
        item = read_link(address, s.get("note", ""))
        t = parse_date(item.pop("date_raw", ""))
        if t:
            item["date"] = t.astimezone().isoformat(timespec="minutes")
            item["hours_ago"] = round(max((now_t - t).total_seconds() / 3600, 0.0), 1)
        status["read_url"] = address
        return status, [item], 1
    if kind == "youtube":
        url = youtube_feed(address)
        raw, _ = fetch(url)
        items = feed_items(raw)
    elif kind == "news":
        url = news_url(address, days)
        raw, _ = fetch(url)
        items = feed_items(raw)
    elif kind == "reddit":
        url = reddit_url(address)
        raw, _ = fetch(url, agent=REDDIT_AGENT)
        items = feed_items(raw)
    elif kind == "rss":
        url = address
        raw, _ = fetch(url)
        items = feed_items(raw)
    elif kind == "sitemap":
        url = address
        raw, _ = fetch(url)
        items = sitemap_items(raw)
    else:  # site
        found, url = find_site_feed(address)
        raw, _ = fetch(url)
        items = feed_items(raw) if found == "rss" else sitemap_items(raw)
        status["found_type"] = found
    status["read_url"] = url
    total = len(items)

    if kind == "youtube":
        views = [i["views"] for i in items if "views" in i]
        if views:
            status["channel_median_views"] = int(statistics.median(views))
            status["channel_recent_videos"] = len(views)

    cutoff = now_t - dt.timedelta(days=days)
    picked = []
    undated = 0
    for i in items:
        t = parse_date(i.pop("date_raw", ""))
        if t is None:
            undated += 1
            continue
        if t < cutoff:
            continue
        i["date"] = t.astimezone().isoformat(timespec="minutes")
        hours = max((now_t - t).total_seconds() / 3600, 0.0)
        i["hours_ago"] = round(hours, 1)
        if "views" in i:
            i["views_per_hour"] = round(i["views"] / max(hours, 1.0), 1)
            if status.get("channel_median_views"):
                i["vs_channel_median"] = round(i["views"] / max(status["channel_median_views"], 1), 2)
        picked.append(i)
    picked.sort(key=lambda x: x["date"], reverse=True)
    if undated:
        status["undated_skipped"] = undated
    return status, picked[:MAX_PER_SOURCE], total


def previous_scan():
    # Read before writing: if there is a second scan on the same day, the morning file counts as the previous scan.
    candidates = sorted(RADAR.glob("raw-*.json"))
    if not candidates:
        return None, {}
    last = candidates[-1]
    try:
        data = json.loads(last.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None, {}
    views = {}
    for i in data.get("items", []):
        if "views" in i and i.get("link"):
            views[i["link"]] = i["views"]
    return {"file": last.name, "time": data.get("scanned_at")}, views


def scan(days_arg):
    days_file, sources = read_sources(SOURCES)
    if sources is None:
        print(f"no source list: {SOURCES}. Run the 'watch my competitors' command first.")
        return 2
    if not sources:
        print("no readable rows in the source list (table: | Name | Type | Address | Note |).")
        return 2
    days = days_arg or days_file or DEFAULT_DAYS
    now_t = now()
    local_now = now_t.astimezone()
    file_name = f"raw-{local_now.strftime('%Y-%m-%d')}.json"
    prev, prev_views = previous_scan()
    prev_t = parse_date(prev["time"]) if prev and prev.get("time") else None

    statuses, errors, everything = [], [], []
    for s in sources:
        try:
            status, items, total = scan_source(s, days, now_t)
        except Exception as e:  # network error, broken feed: skip the source, carry on
            errors.append({"name": s["name"], "type": s["type"], "address": s["address"], "error": error_text(e)})
            print(f"  SKIPPED  {s['name']} ({s['type']}): {error_text(e)}")
            continue
        for i in items:
            i["source"] = s["name"]
            i["type"] = s["type"]
            if s.get("note") and s["type"] != "link":
                i["source_note"] = s["note"]
            if prev_t and "views" in i and i.get("link") in prev_views:
                before = prev_views[i["link"]]
                gap = (now_t - prev_t).total_seconds() / 3600
                i["previous_views"] = before
                i["growth_since_last_scan"] = i["views"] - before
                if gap > 0.5:
                    i["growth_per_hour_between_scans"] = round((i["views"] - before) / gap, 1)
        status["items_in_feed"] = total
        status["in_window"] = len(items)
        statuses.append(status)
        everything.extend(items)
        print(f"  OK       {s['name']} ({s['type']}): {len(items)} items (feed had {total})")

    result = {
        "scanned_at": now_t.isoformat(timespec="seconds"),
        "local_time": local_now.isoformat(timespec="minutes"),
        "days": days,
        "previous_scan": prev,
        "source_count": len(sources),
        "sources_ok": len(statuses),
        "sources_failed": len(errors),
        "item_count": len(everything),
        "note": ("views and likes exist only in YouTube feeds. News, blog, sitemap and Reddit feeds "
                 "have no view data."),
        "sources": statuses,
        "errors": errors,
        "items": everything,
    }
    RADAR.mkdir(parents=True, exist_ok=True)
    target = RADAR / file_name
    with open(target, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"{len(statuses)}/{len(sources)} sources read, {len(everything)} items (last {days} days), "
          f"file: {target.relative_to(ROOT).as_posix()}")
    return 0


def main():
    utf8_output()
    p = argparse.ArgumentParser(description="The lookout's scanner: reads public sources.")
    p.add_argument("--days", type=int, help="how many days back (default: 'days' in sources.md, else 4)")
    p.add_argument("--find-channel", metavar="URL", help="finds the channel_id from a YouTube channel URL")
    p.add_argument("--try", dest="try_", nargs=2, metavar=("TYPE", "ADDRESS"), help="tries one source, writes no file")
    a = p.parse_args()
    if a.find_channel:
        try:
            cid = find_channel_id(a.find_channel)
        except Exception as e:
            print(f"not found: {error_text(e)}")
            return 1
        print(f"channel_id: {cid}")
        print(f"feed: https://www.youtube.com/feeds/videos.xml?channel_id={cid}")
        return 0
    if a.try_:
        kind = TYPES.get(a.try_[0].lower())
        if not kind:
            print("type must be one of: " + ", ".join(sorted(set(TYPES.values()))))
            return 1
        days = a.days or DEFAULT_DAYS
        try:
            status, items, total = scan_source({"name": "try", "type": kind, "address": a.try_[1]}, days, now())
        except Exception as e:
            print(f"could not read: {error_text(e)}")
            return 1
        print(f"read: {status.get('read_url')} · {total} in feed, {len(items)} items in the last {days} days")
        for i in items[:5]:
            extra = f" · {i['views']} views" if "views" in i else ""
            print(f"  - {i.get('date', '')[:16]} {i['title'][:90]}{extra}")
        return 0
    return scan(a.days)


if __name__ == "__main__":
    sys.exit(main())
