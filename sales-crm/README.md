# Sales CRM 🧩

A simple customer-tracking system for sales and call-center teams. One file, double-click to open, no server and no sign-up. Every customer lives on a single card, the rep drops two lines of notes, the system sets the follow-up day on its own, and the people to call that day surface in the morning list.

In call centers and sales, every customer sits somewhere different: one in excel, one on whatsapp, one in the rep's head. Then who was going to be called, who was promised what, where each conversation left off, all of it gets lost. This system pulls it into one board.

> **Note:** the interface is currently in Turkish. A full English UI translation is next on the list; the system itself works the same regardless of language.

## What it does

- Every customer on one card: who, which stage, what was last discussed, what the next step is.
- The moment a call ends, the rep writes two lines; the system stamps the date and sets the follow-up day itself.
- The people to call that day drop into the morning list automatically, overdue ones on top, nobody forgotten.
- At month end, how many calls and how many sales each rep produced is visible on a single screen.

The rep does not wrestle with excel, and the manager does not ask "who did what today" one by one; it is on the screen.

## What you need

- A computer and a browser (Chrome, Edge, Firefox, any). No internet, sign-up, or server required.
- `satis-crm.html` and `crm-cekirdek.js` (in this package). The two files sit side by side in the same folder.

## Install (local mode, default)

Three ways, and the third is the easiest.

**1. One command (degit).** Downloads the folder as is:

```bash
npx degit muhammedsevimli/systems/sales-crm sales-crm
```

**2. Clone or download ZIP.** Use the green **Code → Download ZIP**, or:

```bash
git clone https://github.com/muhammedsevimli/systems.git
```

**3. Hand the folder to your AI tool and say "open and adapt it".** The easiest option. Open this folder in Claude Code or Cursor and say "open these two files" or "change the stages to match my sales pipeline". No coding required.

Then put `satis-crm.html` and `crm-cekirdek.js` in the **same folder** and **double-click** `satis-crm.html`. It opens in your browser with a board full of sample customers. On first launch it comes with 6 sample customers and 3 reps (fictional). When you are ready for your own data, use **Settings → Clear sample data** and add your list with **+ Customer**.

Data stays in this computer's browser. It does not go to a server or any third party.

## How it looks

For a quick tour see `EXAMPLE-OUTPUT.md`: how the morning list, a customer card, a call note, and the month-end panel look with the sample data. (All examples are fictional.)

## Team / shared mode (optional)

Local mode is for a single computer. If you want the team to see the same data, a one-time ~10-minute setup connects the system to a free Google Sheet: no rented server, no sign-up, just your own Google account. The step-by-step walkthrough is in **`ORTAK-KURULUM.md`** in this package (currently Turkish). `kod-google-apps-script.gs` is the code for this mode.

Once connected, everyone on the team enters the same link and sees the same data. When one rep adds a note, it shows up for the others within seconds. The manager watches everyone from the same panel.

## Security

- **The shared-mode web app link is like a password.** Whoever has the link can see and change the data. Share it only with your team, never post it in public.
- In shared mode the data lives in **your Google Drive**, in your Sheet. It does not go to a third party.
- In local mode the data lives only in that computer's browser.
- If you want stronger security (an extra secret key on the link), tell Claude Code "add a secret key to CRM shared mode".

## Who it is for

Sales teams, call centers, small businesses: anyone whose customer tracking is scattered between excel and whatsapp. You do not need to code.

## Files in this package

- `satis-crm.html` · the system itself, double-click to open.
- `crm-cekirdek.js` · the rules file, keep it in the same folder as `satis-crm.html`.
- `ornek-veri.json` · fictional sample data (6 customers, 3 reps).
- `ORTAK-KURULUM.md` · team / shared mode setup (Turkish).
- `kod-google-apps-script.gs` · Google Apps Script code for shared mode.

---

**Muhammed Sevimli** built this system. Real sales and growth systems with AI, taught in Turkish. If you get stuck setting it up or want step-by-step help, reach out:

- Web: https://muhammedsevimli.com
- Instagram: https://instagram.com/msevimli_
- X: https://x.com/_msevimli
- Threads: https://threads.net/@msevimli_
- YouTube: https://youtube.com/@msevimli
- Email: hey@muhammedsevimli.com

## License

[MIT](LICENSE) · use, adapt, and share freely.
