# Data Collection Guide

All metrics in this framework can be collected using tools most organizations already have. No specialized analytics platform is required.

---

## Session Log

**What it captures:** One row per session delivery

**Collection method:** Maintained manually by program coordinator or auto-populated from calendar/Teams meeting records

**Required columns:**
```
session_id, session_date, session_name, site, facilitator,
registered_count, attended_count, completed_count, duration_minutes, planned
```

**Tool:** Excel or CSV; can be connected to Power BI directly

---

## Participant Log

**What it captures:** One row per participant per session attended

**Collection method:** Attendance taken via Teams meeting roster export, QR code sign-in, or manual sign-in sheet

**Required columns:**
```
participant_id, employee_id, session_id, session_date, department,
site, role_level, voluntary (Y/N), completed_session (Y/N),
prior_sessions_attended
```

**Tool:** Excel, SharePoint list, or Microsoft Forms attendance integration

---

## CSAT Survey

**What it captures:** Post-session satisfaction and self-reported confidence

**Collection method:** Microsoft Forms link shared at end of each session; anonymous responses preferred

**Required columns:**
```
response_id, session_id, session_date, overall_rating (1-3),
would_recommend (Y/N), most_useful, improvement_suggestion, confidence_before (1-5), confidence_after (1-5)
```

**Recommended Microsoft Forms questions:**
1. How would you rate today's session? (1 = Needs improvement, 2 = Good, 3 = Excellent)
2. Would you recommend this session to a colleague? (Yes / No)
3. What was most useful? (open text)
4. What could be improved? (open text)
5. Before today, how confident were you using AI tools? (1-5)
6. After today, how confident are you using AI tools? (1-5)

---

## 30-Day Follow-Up Survey

**What it captures:** Skill conversion and feature adoption 30 days after training

**Collection method:** Microsoft Forms email sent automatically via Power Automate 30 days after session attendance

**Recommended questions:**
1. Are you using [AI tool] in your regular work? (Yes / Sometimes / No)
2. Which features are you using? (checkbox list of trained features)
3. Has your productivity changed since training? (Yes, noticeably / Somewhat / No change)
4. What barriers are preventing you from using the tool? (open text, shown only if No or Sometimes above)

---

## Notes on Privacy

- Collect employee IDs for deduplication; do not display individual names in dashboards
- CSAT surveys should be anonymous at the response level
- 30-day follow-ups should be pseudonymized (response linked to session cohort, not individual) where possible
- Store all data in SharePoint or OneDrive with appropriate access controls
