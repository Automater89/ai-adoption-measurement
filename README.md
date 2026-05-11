# AI Adoption Measurement Framework

> **A practitioner-built framework for proving whether enterprise AI rollouts are actually changing how people work — not just whether licenses got assigned.**

Built by an IT Project Manager who ran a 1,000+ participant Microsoft 365 Copilot enablement program across 9 sites. Designed for program leads, digital workplace teams, and change managers responsible for proving ROI on enterprise AI investment.

[![Status](https://img.shields.io/badge/status-active-brightgreen)](https://github.com/Automater89/ai-adoption-measurement)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Stack](https://img.shields.io/badge/stack-Python%20%7C%20pandas%20%7C%20Power%20BI-informational)](#tech-stack)
[![Portfolio](https://img.shields.io/badge/portfolio-Agent%20Showcase-teal)](https://automater89.github.io/Agent-Showcase/)

---

## The Business Problem

Enterprises are spending heavily on Microsoft Copilot, ChatGPT Enterprise, and Power Platform AI features — and most can't answer the question their CFO is about to ask:

> *"We bought 5,000 licenses. Is anything actually changing?"*

Standard adoption dashboards count the wrong things:

| What dashboards usually show | What leadership actually needs to know |
|---|---|
| Licenses assigned | Are people **using the tool weekly**? |
| Sessions attended | Did attendees **change their workflow**? |
| Features activated | Are users **producing better output**? |
| Headcount trained | Are people **coming back voluntarily**? |
| Surveys distributed | Is **CSAT trending up** quarter over quarter? |
| Prompts shared | Are prompts **high-quality and reused**? |

Activity is not adoption. This framework gives program leaders a defensible, repeatable way to measure the difference — using tools every enterprise already owns (Microsoft Forms, Teams, SharePoint, Power BI).

---

## Enterprise Value

This framework helps an organization:

- **Defend AI program budget** to finance and executive sponsors with behavior-based metrics, not vanity counts
- **Identify stalls early** — distinguish "people attending" from "people changing" before momentum dies
- **Prioritize intervention** — surface which dimension (Reach, Engagement, Effectiveness, Momentum) is underperforming and where to spend the next dollar
- **Standardize reporting** across sites, business units, and AI products so cross-program comparisons are meaningful
- **Operationalize change management** with metrics that translate into Power Automate nudges, manager check-ins, and peer-champion programs

Designed to plug into an existing Microsoft 365 environment with zero new vendors.

---

## What This Project Proves

This repository is a working artifact, not a slide deck. It demonstrates the ability to:

- Translate enterprise change-management problems into a quantitative model
- Design measurement systems that survive contact with real program data
- Ship clean, testable Python that a Power BI analyst or junior PM can run
- Build templates and documentation a program team can actually adopt
- Connect AI enablement strategy to the Power Platform and Microsoft 365 ecosystem

It is intended as a portfolio artifact for **IT Project Management, AI Enablement, Process Improvement, and Workforce Adoption** roles.

---

## Tech Stack

| Layer | Technology | Why |
|---|---|---|
| Data input | CSV (Excel, SharePoint Lists, Microsoft Forms exports) | Zero ramp for program coordinators |
| Processing | Python 3.10+, pandas | Deterministic, auditable calculations |
| CLI / output | `rich`, Markdown reports | Readable in terminal, in PRs, and in SharePoint |
| Visualization | Power BI template (planned `.pbit`) | Direct connection to the same CSVs |
| Automation pattern | Power Automate + Microsoft Forms for 30/60/90 follow-ups | Matches how enterprises already work |
| Testing | pytest | Every metric is unit-tested |

No Azure OpenAI dependency. The measurement logic is deterministic by design — adding an LLM here would add cost and credentials without improving accuracy. (Sister projects [`process-waste-detector`](https://github.com/Automater89/process-waste-detector) and [`benefits-faq-agent`](https://github.com/Automater89/benefits-faq-agent) demonstrate Azure AI / RAG patterns where they belong.)

---

## AI Enablement & Workflow Pattern

The framework operationalizes a four-stage adoption loop common to enterprise AI programs:

```
   ┌─────────────┐    ┌───────────────┐    ┌───────────────┐    ┌──────────────┐
   │  1. Reach   │───▶│ 2. Engagement │───▶│ 3. Effective- │───▶│ 4. Momentum  │
   │ Right people│    │  Real partici-│    │    ness       │    │ Self-        │
   │ at scale    │    │  pation       │    │ Behavior      │    │ sustaining   │
   │             │    │               │    │ change        │    │ growth       │
   └─────────────┘    └───────────────┘    └───────────────┘    └──────────────┘
          │                  │                    │                    │
          ▼                  ▼                    ▼                    ▼
     Session log       Attendance &         30-day follow-up      Usage data +
     + HRIS            Forms registration   + manager pulse       prompt library
          │                  │                    │                    │
          └──────────────────┴──────────┬─────────┴────────────────────┘
                                        ▼
                          metrics.py  ─▶  scorer.py  ─▶  reporter.py
                                        ▼
                         Markdown report + CSV export + Power BI
```

Each stage feeds the next. Programs that win on Reach but lose on Effectiveness produce inflated dashboards; the framework's weighted scoring (Effectiveness = 35%) is designed to expose that pattern instead of hide it.

---

## Business Outcome (Reference Program)

Benchmarks in this framework are calibrated against a real Microsoft 365 Copilot enablement program — not industry survey averages:

- **34 sessions** delivered across **9 sites**, **1,019 unique attendees**
- **90%+** completion on high-volume tracks
- **72%** average **skill conversion** rate (tool actively used 30 days post-training)
- **3.0 / 3.0** sustained **CSAT** across the program
- **+380% YoY** growth in voluntary AI learning hours
- **500+** enterprise AI prompts catalogued across Microsoft 365 Copilot use cases

These numbers shape the default targets in `metrics.py` and `docs/benchmarks.md`. A program manager dropping this framework into a new rollout starts with realistic, defensible thresholds on day one.

---

## Architecture Summary

```text
ai-adoption-measurement/
├── docs/
│   ├── framework.md         # Methodology and metric definitions
│   ├── data-collection.md   # How to collect each metric (Forms, Teams, HRIS)
│   ├── benchmarks.md        # Target ranges and interpretation bands
│   └── decisions.md         # Design-decision log
├── data/
│   ├── sample/              # Synthetic but realistic 1,000-row dataset
│   └── outputs/             # Generated reports
├── src/
│   ├── loader.py            # CSV ingest + validation
│   ├── metrics.py           # 4-dimension calculations
│   ├── scorer.py            # Weighted health score + attention flags
│   ├── reporter.py          # Markdown report generator
│   └── utils/               # config, logging
├── templates/               # Blank CSVs for session, participant, survey
└── tests/                   # pytest suite
```

**Data flow:** CSV → `loader` validates → `metrics` computes per-dimension scores → `scorer` produces a weighted health score and flags attention areas → `reporter` emits a Markdown summary suitable for SharePoint, a PR, or an exec brief.

---

## Quick Start

```bash
git clone https://github.com/Automater89/ai-adoption-measurement.git
cd ai-adoption-measurement
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run against the bundled sample dataset
python -m src.metrics \
    --sessions data/sample/sessions.csv \
    --participants data/sample/participants.csv \
    --survey data/sample/survey.csv

# Generate a Markdown adoption health report
python -m src.reporter --output data/outputs/
```

**Demo path (no install):** open `data/sample/` to see the data shape, then read `docs/framework.md` for the methodology and `docs/benchmarks.md` for how targets were derived.

---

## Sample Output

```
================================================
AI ADOPTION HEALTH REPORT
================================================
Program          : Copilot Enablement Initiative
Reporting Period : Q1 2026
================================================

OVERALL ADOPTION HEALTH SCORE: 78 / 100  [Strong]

DIMENSION SCORES
  Reach        : 82 / 100
  Engagement   : 79 / 100
  Effectiveness: 74 / 100
  Momentum     : 76 / 100

KEY METRICS
  Total unique participants   : 1,019
  Session completion rate     : 90.4%     [Target: 85%]   PASS
  Voluntary attendance rate   : 68.2%     [Target: 60%]   PASS
  CSAT score                  : 2.91/3.0  [Target: 2.8]   PASS
  Skill conversion rate       : 72.1%     [Target: 70%]   PASS
  YoY voluntary learning hrs  : +380%     [Target: +50%]  PASS

ATTENTION AREAS
  Feature adoption rate       : 54.3%     [Target: 65%]   BELOW TARGET
  Repeat attendance rate      : 41.0%     [Target: 50%]   BELOW TARGET

PRIORITY ACTION
  Increase feature adoption through 30-day post-training nudge
  campaign and manager accountability check-in.
================================================
```

---

## Why These Metrics, and Not Others

The full design rationale lives in [`docs/framework.md`](docs/framework.md) and [`docs/decisions.md`](docs/decisions.md). The short version:

- **Effectiveness is weighted highest (35%).** It's the only dimension that proves the program changed behavior. Programs that pass everything except Effectiveness are theatre.
- **Voluntary attendance is tracked separately from total attendance.** A program propped up by manager mandates will look healthy until the mandate ends.
- **CSAT uses a 1–3 scale, not 1–5.** Five-point scales in professional training reliably inflate; three points force a real signal.
- **Momentum is its own dimension.** Without it, a program that peaked six months ago still scores well.

This is the difference between a dashboard that makes a program look good and one that tells leadership where to spend the next dollar.

---

## Recruiter-Friendly Positioning

**Built by:** Wes Shelton — IT Project Manager focused on AI enablement, process improvement, automation, Power Platform, and enterprise workforce adoption.

**This project demonstrates fit for roles involving:**
- AI enablement / digital adoption program leadership
- Microsoft 365 Copilot, ChatGPT Enterprise, or Gemini Workspace rollouts
- Power Platform–centric change management (Forms, Power Automate, Power BI, SharePoint)
- Measurement-and-reporting design for executive stakeholders
- Process improvement and Lean-style waste reduction (see [`process-waste-detector`](https://github.com/Automater89/process-waste-detector))

**What's evidenced here:**
- Translating ambiguous business problems into quantitative models
- Writing clean, testable Python that non-engineers can run
- Designing documentation and templates a program team will actually adopt
- Calibrating targets from real-world program data, not vendor marketing
- Connecting AI strategy, change management, and Microsoft 365 tooling end-to-end

**Related portfolio work:**
- [Agent Showcase](https://automater89.github.io/Agent-Showcase/) — live portfolio of AI and automation projects
- [`process-waste-detector`](https://github.com/Automater89/process-waste-detector) — Lean waste analysis using Azure OpenAI
- [`benefits-faq-agent`](https://github.com/Automater89/benefits-faq-agent) — RAG-based HR benefits Q&A agent
- [`azure-doc-agent`](https://github.com/Automater89/azure-doc-agent) — Document extraction and agent workflow pipeline

---

## Roadmap

- [x] CSV schema, sample dataset, and templates
- [x] Four-dimension metrics engine with unit tests
- [x] Weighted Adoption Health Score
- [x] Markdown report generator
- [ ] Power BI template (`.pbit`) connected to sample CSVs
- [ ] Period-over-period trend comparison in reporter
- [ ] Loom walkthrough and methodology write-up

---

## License

MIT — see [LICENSE](LICENSE).
