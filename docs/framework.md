# AI Adoption Measurement Framework: Full Methodology

## Design Principles

1. **Measure behavior change, not activity** — attendance and license counts are leading indicators only; the framework's primary metrics are behavioral
2. **Every metric has a defined collection method** — no metric is included if it cannot be collected with tools most organizations already have (Microsoft Forms, Teams, Excel/CSV, HRIS)
3. **Benchmarks are grounded in real program data** — targets are based on observed outcomes from a real 1,000+ participant AI enablement program, not industry averages
4. **The score is directional, not definitive** — the adoption health score surfaces attention areas; it is not a pass/fail grade for the program

---

## Dimension 1: Reach

**Question:** Are we getting to the right people at the right scale?

| Metric | Definition | Collection | Target |
|---|---|---|---|
| Unique participants | Count of distinct individuals trained | Session log deduplicated by employee ID | Program-dependent |
| Population coverage | Unique participants / total target population | Session log + HRIS headcount | 80%+ of target groups |
| Site coverage | Number of sites with at least one session | Session log | All sites with 10+ target employees |
| Sessions delivered vs. planned | Actual sessions / planned sessions | Session log vs. program plan | 95%+ |

---

## Dimension 2: Engagement

**Question:** Are people choosing to participate, and are they staying?

| Metric | Definition | Collection | Target |
|---|---|---|---|
| Session completion rate | Participants who stayed for full session / registered | Attendance tracking | 85%+ |
| Voluntary attendance rate | Attendees who registered without manager mandate / total | Registration form field | 60%+ |
| Repeat attendance rate | Participants who attended 2+ sessions / total unique | Session log | 50%+ |
| YoY voluntary learning hours | Total voluntary hours this period / same period last year | Session log + duration | +50% YoY minimum |

---

## Dimension 3: Effectiveness

**Question:** Is training producing measurable behavior change?

| Metric | Definition | Collection | Target |
|---|---|---|---|
| Skill conversion rate | Participants who demonstrate tool use post-training / total | 30-day follow-up survey or manager check-in | 70%+ |
| CSAT score | Average satisfaction rating from post-session survey | Microsoft Forms (1-3 scale or 1-5 scale) | 2.8/3.0 or 4.5/5.0 |
| Feature adoption rate | % of trained features actively used 30 days post-training | Usage data from admin portal or self-report | 65%+ |
| Manager-reported improvement | % of managers reporting productivity change at 30/60/90 days | Manager pulse survey | 60%+ at 60 days |

---

## Dimension 4: Momentum

**Question:** Is adoption self-sustaining and accelerating?

| Metric | Definition | Collection | Target |
|---|---|---|---|
| MoM active user growth | Active users this month / last month - 1 | Usage data or session log | Positive for 6 consecutive months |
| Prompt contribution rate | Employees who submitted prompts to shared library / total trained | Prompt library submission log | 10%+ of trained population |
| Peer sharing rate | Documented cases of trained employees teaching others | Manager reports or peer nominations | Tracked; growth trend |
| Unsolicited positive feedback | Count of unprompted positive comments, emails, Viva Engage posts | Manual log | Tracked; growth trend |

---

## Scoring Model

Each metric is scored against its target benchmark:
- **Exceeds target:** 100 points
- **Meets target:** 80 points
- **Within 10% of target:** 60 points
- **10-25% below target:** 40 points
- **More than 25% below target:** 20 points

Dimension scores are the average of their metric scores.

Overall Adoption Health Score is a weighted average:
| Dimension | Weight |
|---|---|
| Reach | 20% |
| Engagement | 25% |
| Effectiveness | 35% |
| Momentum | 20% |

Effectiveness is weighted highest because it is the only dimension that measures actual behavior change.
