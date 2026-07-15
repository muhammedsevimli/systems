# Automatic production every morning · setup

> This section is optional. The system also runs with one command (`RUN.md` Step 1). This is for people who want "run it while I sleep, 50 concepts ready in the morning".
> The idea is simple: a task that runs every morning runs the command you would normally type by hand. No magic, just a scheduled single command.

## Run it by hand once first (required)
Before switching to automatic, run the system by hand once (`RUN.md` Step 1). After you see it works, wire it to the automatic task. Your input files must be filled.

## It does not run while the computer is off (honest limit)
This task runs on your computer. If your computer is off at 07:00, the task does not run (on Windows it can run when the computer turns on, via the "run task as soon as possible after a missed start" option). If your computer is not always on, set it to a time when you turn it on, or run the single command yourself. A 24/7 server setup is a separate job, outside the scope of this playbook.

---

## Windows · Task Scheduler

### The easy way · one command (recommended)
Find the FULL path of the `automation` folder (right-click `every-morning.cmd` in File Explorer, "copy as path"). Then type `cmd` in Start to open Command Prompt and paste this (replace the path with your own, keep the quotes):

```text
schtasks /create /tn "Ad Concept Factory" /tr "\"C:\Users\YOURNAME\Desktop\ad-concept-factory\automation\every-morning.cmd\"" /sc daily /st 07:00
```

- `/tn` is the task name. `/tr` is the file to run (your `every-morning.cmd` path). `/sc daily` is every day. `/st 07:00` is the time.
- When you press Enter and it says "SUCCESS", it is set up. The next morning at 07:00 the system writes 50 concepts into the `outputs/` folder.
- If you also want missed tasks to run (if the computer was off at that time): open Task Scheduler, find the task, and in the "Conditions/Settings" tab check "Run task as soon as possible after a scheduled start is missed".

### The click way (if you do not want the command prompt)
1. Type `Task Scheduler` in Start, open it.
2. Click "Create Basic Task" on the right. Name: `Ad Concept Factory`. Next.
3. Trigger: "Daily". Next. Time: `07:00`. Next.
4. Action: "Start a program". Next.
5. In the "Program/script" box, type the full path of your `every-morning.cmd` file (or select it with "Browse"). Next, Finish.

### Test / delete
```text
schtasks /run /tn "Ad Concept Factory"     (run once now, for a test)
schtasks /query /tn "Ad Concept Factory"   (check whether it is set up)
schtasks /delete /tn "Ad Concept Factory" /f   (delete the task)
```

---

## Mac · cron

Open Terminal, type `crontab -e`, and add this line to the editor that opens (replace the path with your own):

```text
0 7 * * * /Users/YOURNAME/Desktop/ad-concept-factory/automation/every-morning.sh
```

- `0 7 * * *` is every day at 07:00. Make the script executable: in Terminal, `chmod +x /Users/YOURNAME/.../automation/every-morning.sh`.
- Save, exit. cron does not run while the Mac is asleep; set it to a time when you keep the computer on, or set up a wake with `launchd` (advanced).

---

## Where the output lands
Default: the `outputs/` folder inside the project, named `YYYY-MM-DD-morning.md`. A new file every morning.
If you want to see it on your desktop, two ways:
1. Put the whole `ad-concept-factory` folder on your desktop (easiest).
2. Change the "write the output to the outputs folder ..." line in `automation/daily-task.txt` to "write the output to the concept-output folder on my desktop ..." and open that folder.

## Checking whether it ran
Open `automation/last-run.log`: the start/finish time of each run and any error are written there.
