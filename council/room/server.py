# Council room: a small server that reads the session folder live. No AI calls, it only reads files.
# Run: python room/server.py  -> http://localhost:4731  (?id=<session-folder> for a specific session)
import json, os, sys
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESSIONS = os.path.join(ROOT, "sessions")
ROOM = os.path.dirname(os.path.abspath(__file__))
SEATS = {"buffett": "Warren Buffett", "bezos": "Jeff Bezos", "musk": "Elon Musk", "jobs": "Steve Jobs", "hormozi": "Alex Hormozi", "chair": "Chair (Claude)"}
ROUNDS = (("tur1", "round1"), ("tur2", "round2"))

def latest_session():
    p = os.path.join(SESSIONS, "LATEST.txt")
    if os.path.exists(p):
        name = open(p, encoding="utf-8").read().strip()
        if name and os.path.isdir(os.path.join(SESSIONS, name)):
            return name
    names = [d for d in os.listdir(SESSIONS) if os.path.isdir(os.path.join(SESSIONS, d)) and d != "questions"] if os.path.isdir(SESSIONS) else []
    return sorted(names)[-1] if names else None

def read(p):
    try:
        return open(p, encoding="utf-8").read()
    except Exception:
        return ""

def session_json(name):
    k = os.path.join(SESSIONS, name)
    cards = []
    for key, folder in ROUNDS:
        d = os.path.join(k, folder)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if not f.endswith(".md"):
                continue
            who = f[:-3].lower()
            cards.append({"tur": key, "kim": who, "isim": SEATS.get(who, who.title()), "mtime": os.path.getmtime(os.path.join(d, f)), "metin": read(os.path.join(d, f))})
    cards.sort(key=lambda c: (c["tur"], c["kim"] == "chair", c["mtime"]))
    out = {"oturum": name, "brief": read(os.path.join(k, "brief.md")), "kartlar": cards,
           "karar": read(os.path.join(k, "decision.md")), "muhur_var": os.path.exists(os.path.join(k, "seal.md"))}
    dj = os.path.join(k, "decision.json")
    if os.path.exists(dj):
        try:
            j = json.loads(read(dj))
            # the page uses short internal keys
            out["karar_json"] = {"karar": j.get("decision"), "etiket": j.get("label"), "secenek": j.get("option"), "ortalama": j.get("averages", {})}
        except Exception:
            out["karar_json"] = None
    return out

class H(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOM, **kw)
    def log_message(self, *a):
        pass
    def do_GET(self):
        u = urlparse(self.path)
        if u.path == "/api/session":
            q = parse_qs(u.query)
            name = q.get("id", [None])[0] or latest_session()
            data = session_json(name) if name else {"oturum": None, "kartlar": []}
            b = json.dumps(data, ensure_ascii=False).encode("utf-8")
            self.send_response(200); self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Cache-Control", "no-store"); self.send_header("Content-Length", str(len(b))); self.end_headers()
            self.wfile.write(b); return
        if u.path == "/":
            self.path = "/index.html"
        return super().do_GET()

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 4731
    print(f"Council room: http://localhost:{port}  (session: {latest_session()})")
    ThreadingHTTPServer(("127.0.0.1", port), H).serve_forever()
