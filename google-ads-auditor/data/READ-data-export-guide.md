# How to Export the Report (5 minutes)

> The system does not connect to your account. You take the report from the Google Ads panel and put it in this folder. Nothing technical: open, export, paste.
> There are two reports. The most important one is the **Search terms report**. If you have time, add the **Campaigns report** too, and the budget audit will run.

## First set the date range
Log into Google Ads (`ads.google.com`). From the date picker at the top right, select **Last 30 days**. (A longer range means a more accurate audit; 90 days works too.)

## Report 1 · Search terms report (the main source)
This report shows which searches ACTUALLY triggered your ads. The wasted money is hidden here.

1. From the left menu, go to **Search terms** under **Campaigns** (in the panel: Insights and reports, Search terms). Shortcut: in the left menu, among the search groups it says "Search terms".
2. Check the columns at the top. These columns should be visible (if not, add columns · the "Columns" icon at the top right):
   - Search term
   - Match type
   - Campaign
   - Ad group
   - Impr.
   - Clicks
   - Cost
   - Conversions
   - Conv. value
3. The **download icon** at the top right (the down arrow) · choose **CSV** or **Excel (.xlsx)** as the format, download. Easiest: select the table with the mouse and copy it (Ctrl+A then Ctrl+C while on the table).
4. In this folder, open a file named `search-terms.md`, and paste the table you downloaded/copied into it. Opening the CSV in Notepad and pasting its contents is enough too. The system reads the table, the format does not have to be perfect.

> Filled-in example: `data/EXAMPLE-search-terms.md`. Your own file just needs to resemble this structure.

## Report 2 · Campaigns report (for the budget audit)
This report shows which campaign eats a lot of money and returns little.

1. From the left menu, go to **Campaigns**.
2. These columns should be visible: Campaign, Cost, Conversions, Conv. value, (if available) Conv. value / cost or ROAS.
3. Download or copy the same way.
4. In this folder, open a file named `campaigns.md`, and paste.

> Filled-in example: `data/EXAMPLE-campaigns.md`.

## Tips
- **Do not skip the conversions and conversion value columns.** They are needed to separate the wasted from the converting. If you do not have conversion tracking set up, the system still finds the wasted spend but cannot comment on return, and it tells you so.
- Do not fix the numbers, paste them as they are. The currency sign and thousands separator can stay, the system reads them.
- Leave a column you are unsure about empty. The system does not invent, if it is missing it says "give that column too".
- Whatever the currency is (USD, EUR, GBP), the system uses it, it does not convert.
