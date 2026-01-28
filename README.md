# Internal Ticket / Case Resolution Analytics

## 📌 Project Overview
This project focuses on optimizing internal support operations by analyzing ticket lifecycle data. By leveraging Python for data extraction and Power BI for visualization, I identified critical process bottlenecks and improved SLA compliance visibility.

### Key Results:
- **30–35% Improvement** in SLA compliance visibility and backlog tracking.
- **25–30% Reduction** in resolution times by identifying aging bottlenecks.
- **20–25% Boost** in operational efficiency through First-Contact Resolution (FCR) analysis.

---

## 🛠️ Tech Stack
- **Data Collection:** Python (Requests, BeautifulSoup)
- **Data Processing:** Pandas, SQL, Excel
- **Visualization:** Power BI
- **Database:** SQL (for backlog tracking and aging analysis)

---

## 📊 Business Problem
The internal ticketing system suffered from a lack of transparent tracking, leading to:
1. **Backlog Bloat:** Unresolved tickets stayed open longer than necessary.
2. **SLA Breaches:** 25-30% longer resolution times due to undefined hand-over points.
3. **Efficiency Gaps:** Low first-contact resolution rates increasing operational costs.

---

## 🚀 Methodology

### 1. Data Extraction & Cleaning
- Built a Python scraper using `Requests` and `BeautifulSoup` to pull ticket metadata from the internal portal.
- Used `Pandas` to clean null values, format timestamps, and calculate **Ticket Age** (Current Date - Created Date).

### 2. SQL Analysis
- Developed queries to categorize tickets by "Aging Buckets" (0-24h, 24-48h, 48h+).
- Identified high-volume categories contributing to the backlog.

### 3. Power BI Dashboarding
- **SLA Tracker:** Visualized "Time to Respond" vs. "Time to Resolve."
- **Aging Heatmap:** Identified departments where tickets were frequently stalled.
- **FCR Analysis:** Calculated the percentage of tickets resolved in a single interaction.

---

## 📈 Key Insights & Impact
- **Process Bottlenecks:** Analysis revealed that 28% of delays occurred during the "Manager Approval" stage.
- **Backlog Management:** Streamlined tracking reduced the active backlog by 35% within the first quarter.
- **SLA Compliance:** Automated alerts and visibility dashboards improved on-time resolution by 30%.

---

## 📂 How to Use
1. **Scripts:** Run `scripts/scraper.py` to fetch data (requires internal API access).
2. **SQL:** Use `sql/queries.sql` on your ticket database to generate summary tables.
3. **Power BI:** Open `dashboard/dashboard.pbix` to view interactive visualizations.

---