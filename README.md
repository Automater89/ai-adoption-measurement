# AI Adoption Measurement Framework

An open-source framework for measuring whether AI tool adoption is actually working — not just whether people showed up.

Built from real enterprise AI enablement experience. Designed for any organization rolling out Microsoft Copilot, ChatGPT Enterprise, or similar AI tools and needing a structured way to measure impact beyond license utilization.

[![Status](https://img.shields.io/badge/status-in%20progress-yellow)](https://github.com/Automater89/ai-adoption-measurement)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Portfolio](https://img.shields.io/badge/portfolio-Agent%20Showcase-teal)](https://automater89.github.io/Agent-Showcase/)

---

## The Problem This Solves

Most organizations measure AI adoption by counting:
- Licenses assigned
- Sessions attended
- Features activated

None of these tell you whether AI is actually changing how people work.

This framework measures what matters:

| Vanity Metric | Meaningful Metric |
|---|---|
| Licenses assigned | Active weekly users |
| Sessions attended | Session completion rate |
| Features shown | Features used post-training |
| Headcount trained | Voluntary re-engagement rate |
| Survey distributed | CSAT score and trend |
| Prompts shared | Prompt quality score |

---

## Framework Overview

Four measurement dimensions, each with defined metrics, collection methods, and target benchmarks.

### Dimension 1: Reach
Are we getting to the right people?
- Total unique participants
- % of target population covered
- Coverage by department, site, role level
- Sessions delivered vs. planned

### Dimension 2: Engagement
Are people actually participating?
- Session completion rate (target: 85%+)
- Voluntary attendance rate (not manager-mandated)
- Repeat attendance rate
- YoY growth in voluntary learning hours

### Dimension 3: Effectiveness
Is training producing behavior change?
- Post-session skill conversion rate (target: 70%+)
- CSAT score (target: 2.8/3.0+)
- Manager-reported productivity change (30/60/90 day)
- Feature adoption rate post-training

### Dimension 4: Momentum
Is adoption accelerating or stalling?
- Month-over-month active user growth
- Prompt library contribution rate
- Peer-to-peer sharing incidents
- Unsolicited positive feedback count

---

## What's in This Repository

```text
ai-adoption-measurement/
├── README.md
├── LICENSE
├── docs/
│   ├── framework.md           # Full methodology and metric definitions
│   ├── data-collection.md     # How to collect each metric (Forms, Teams, HRIS)
│   ├── benchmarks.md          # Industry benchmarks and target ranges
│   └── decisions.md           # Design decisions and rationale
├── data/
│   ├── sample/
│   │   ├── sessions.csv       # Sample session-level data
│   │   ├── participants.csv   # Sample participant tracking data
│   │   └── survey.csv         # Sample CSAT survey responses
│   └── outputs/               # Generated reports and charts
├── src/
│   ├── loader.py              # Load and validate CSV input data
│   ├── metrics.py             # Calculate all four dimensions
│   ├── reporter.py            # Generate Markdown summary report
│   ├── scorer.py              # Compute overall adoption health score
│   └── utils/
│       ├── config.py
│       └── logger.py
├── templates/
│   ├── session_log_template.csv       # Blank template for session tracking
│   ├── participant_template.csv       # Blank template for participant tracking
│   └── survey_template.csv           # Blank CSAT survey template
├── tests/
│   ├── test_metrics.py
│   └── test_scorer.py
├── .gitignore
└── requirements.txt
```

---

## Quick Start

```bash
git clone https://github.com/Automater89/ai-adoption-measurement.git
cd ai-adoption-measurement
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run against sample data
python src/metrics.py --sessions data/sample/sessions.csv \
                      --participants data/sample/participants.csv \
                      --survey data/sample/survey.csv

# Generate a Markdown report
python src/reporter.py --output data/outputs/
```

---

## Sample Output

```
================================================
AI ADOPTION HEALTH REPORT
================================================
Program          : Copilot Enablement Initiative
Reporting Period : Q1 2026
Generated        : 2026-05-06
================================================

OVERALL ADOPTION HEALTH SCORE: 78 / 100  [Strong]

DIMENSION SCORES
  Reach        : 82 / 100
  Engagement   : 79 / 100
  Effectiveness: 74 / 100
  Momentum     : 76 / 100

KEY METRICS
  Total unique participants   : 1,019
  Session completion rate     : 90.4%     [Target: 85%]  PASS
  Voluntary attendance rate   : 68.2%     [Target: 60%]  PASS
  CSAT score                  : 2.91/3.0  [Target: 2.8]  PASS
  Skill conversion rate       : 72.1%     [Target: 70%]  PASS
  YoY voluntary learning hrs  : +380%     [Target: +50%] PASS

ATTENTION AREAS
  Feature adoption rate       : 54.3%     [Target: 65%]  BELOW TARGET
  Repeat attendance rate      : 41.0%     [Target: 50%]  BELOW TARGET

PRIORITY ACTION
  Increase feature adoption through 30-day post-training nudge
  campaign and manager accountability check-in.
================================================
```

---

## Milestones

### Milestone 1: Data Templates and Sample Data
- Define CSV schema for sessions, participants, survey
- Generate realistic sample dataset (1,000+ rows)
- Validate templates are usable without modification

### Milestone 2: Metrics Engine
- Implement all four dimension calculations
- Add benchmark comparison logic
- Unit test all metric calculations

### Milestone 3: Adoption Health Score
- Define weighted scoring model
- Implement pass/fail threshold per metric
- Output overall score with dimension breakdown

### Milestone 4: Reporter
- Generate Markdown summary report
- Generate CSV export of all metrics
- Add trend calculation (period-over-period comparison)

### Milestone 5: Portfolio Polish
- Add Power BI template (.pbit) connected to sample CSVs
- Record Loom walkthrough
- Publish methodology write-up on LinkedIn
- Link to Agent Showcase: https://automater89.github.io/Agent-Showcase/

---

## Domain Expertise Behind This Project

This framework was built from real enterprise AI enablement experience:

- Designed and ran a 34-session AI enablement program (TechSmart) across 9 sites with 1,019 attendees
- Achieved 72% skill conversion rate, 3.0/3.0 CSAT, and 380% YoY growth in voluntary learning hours
- Built 500+ enterprise AI prompts across Microsoft 365 Copilot use cases
- 90%+ completion rate on high-volume training tracks

The metrics, benchmarks, and scoring model in this framework reflect what actually predicts sustained adoption — not what looks good in a dashboard.

---

## Related Projects

- [process-waste-detector](https://github.com/Automater89/process-waste-detector) — Lean waste analysis using Azure OpenAI
- [benefits-faq-agent](https://github.com/Automater89/benefits-faq-agent) — RAG-based HR benefits Q&A agent
- [azure-doc-agent](https://github.com/Automater89/azure-doc-agent) — Document extraction and agent workflow pipeline
- [Agent Showcase](https://automater89.github.io/Agent-Showcase/) — Live portfolio of AI and automation projects

---

## License

MIT
