# The lookout's list (example)

> This file is an example list for the fictional Urla Table. The `watch my competitors` command writes `company/radar/sources.md` from your answers; this example only shows the format. If you want to try it with the demo company, the CEO copies this file as `sources.md`.
> Every address on the list is a public source. The lookout only reads; it sends nothing anywhere.

days: 4

| Name | Type | Address | Note |
|---|---|---|---|
| Yemek.com · YouTube | youtube | https://www.youtube.com/feeds/videos.xml?channel_id=UCWA2nh0yrIMC6uG0hfbucRQ | recipe videos, several a week |
| Nefis Yemek Tarifleri · YouTube | youtube | https://www.youtube.com/feeds/videos.xml?channel_id=UCeh3XQszWO6lLdKz_SZmm1Q | home cooking and desserts |
| Refika's Kitchen · YouTube | youtube | https://www.youtube.com/@refikaninmutfagi | channel URL written, the scanner finds the channel_id itself |
| Yemek.com · site | site | https://yemek.com | the scanner finds the site's feed itself |
| News: Urla restaurant | news | Urla restaurant | Google News search |
| News: Izmir food | news | Izmir food | Google News search |
| Reddit: r/izmir | reddit | r/izmir | eating out questions in the city |

## Types

| Type | What goes in the address | View data |
|---|---|---|
| `youtube` | Channel URL (`https://www.youtube.com/@channel`) or feed URL. The scanner finds the `channelId` value in the channel page's source. | Yes (views and likes) |
| `news` | Words to search (`Urla restaurant`). The scanner builds the Google News RSS address itself. A full address also works. | No |
| `rss` | The site's RSS or Atom feed (`https://site.com/feed`). | No |
| `site` | The site's home page. The scanner looks for the feed, and for the sitemap if there is no feed. | No |
| `sitemap` | Sitemap (`https://site.com/sitemap.xml`). If there is no title, it is taken from the address. | No |
| `reddit` | A community like `r/izmir`, or words to search. Reddit sometimes refuses keyless reading; then the source is skipped. | No |
| `link` | One link you add by hand. Reads the text of X and TikTok posts. Instagram and Facebook need a login, so they are not read; the text you write in the Note column is used instead. | No |

Following X, Instagram and TikTok accounts on a schedule is not in this version: these sites do not give a list without a key. If you add a post you saw as a `link` row, the lookout reads it too.
