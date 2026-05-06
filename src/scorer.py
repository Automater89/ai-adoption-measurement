"""
scorer.py -- Interpret overall adoption health score.
"""

SCORE_BANDS = [
    (85, 100, "Exceptional", "Program is self-sustaining. Focus on expansion and advanced use cases."),
    (70, 84, "Strong", "One or two dimensions need attention. Investigate below-target metrics."),
    (55, 69, "Moderate", "Engagement or effectiveness gaps present. Program redesign may be needed."),
    (40, 54, "Early-stage", "Likely a reach or motivation problem. Revisit program design and manager involvement."),
    (0, 39, "Critical", "Significant gaps. Consider pausing expansion until root causes are addressed."),
]


def interpret_score(score: int) -> dict:
    for low, high, label, advice in SCORE_BANDS:
        if low <= score <= high:
            return {"score": score, "label": label, "advice": advice}
    return {"score": score, "label": "Unknown", "advice": ""}


def flag_attention_areas(results: dict, targets: dict) -> list:
    flags = []
    eng = results["engagement"]["metrics"]
    eff = results["effectiveness"]["metrics"]

    checks = [
        (eng["session_completion_rate"], targets["session_completion_rate"], "Session completion rate"),
        (eng["voluntary_attendance_rate"], targets["voluntary_attendance_rate"], "Voluntary attendance rate"),
        (eng["repeat_attendance_rate"], targets["repeat_attendance_rate"], "Repeat attendance rate"),
        (eff["csat_score"] / 3.0, targets["csat_score"] / 3.0, "CSAT score"),
        (eff["recommend_rate"], targets["recommend_rate"], "Recommend rate"),
    ]
    for actual, target, label in checks:
        if actual < target:
            gap_pct = round((target - actual) / target * 100, 1)
            flags.append({"metric": label, "actual": actual, "target": target, "gap_pct": gap_pct})
    return flags
