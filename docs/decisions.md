# Decision Log

---

## 2026-05-06: CSV-first data model (no database)

**Decision:** Use CSV files as the primary data format. No database, no API.

**Rationale:** The target user for this framework is a program manager or digital enablement lead at a mid-size organization. They have Excel and SharePoint, not a data engineering team. CSV keeps the barrier to entry as low as possible. A Power BI template can connect directly to the CSVs for visualization without any transformation layer.

---

## 2026-05-06: No Azure OpenAI dependency

**Decision:** This project uses only pandas and Python standard library. No Azure AI services required.

**Rationale:** The measurement logic is deterministic calculation, not inference. Adding Azure OpenAI would add cost and credential complexity with no benefit. The sister projects (process-waste-detector, benefits-faq-agent) demonstrate Azure AI skills; this project demonstrates data and measurement methodology.

---

## 2026-05-06: Four dimensions with weighted scoring

**Decision:** Organize metrics into four dimensions (Reach, Engagement, Effectiveness, Momentum) with Effectiveness weighted highest (35%).

**Rationale:** Most adoption dashboards treat all metrics equally, which obscures what matters. Effectiveness (behavior change) is the only metric that proves business value. Weighting it highest forces the score to reflect actual impact, not just activity.

---

## 2026-05-06: 1-3 CSAT scale instead of 1-5

**Decision:** Use a 1-3 scale for session CSAT with target of 2.8/3.0.

**Rationale:** A 1-5 scale produces grade inflation and social desirability bias in professional training contexts. A 1-3 scale forces more meaningful differentiation. The 2.8/3.0 target reflects a genuinely high bar — not just "people didn't complain."
