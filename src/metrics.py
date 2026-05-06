"""
metrics.py -- Calculate all four adoption measurement dimensions.

Usage:
    python src/metrics.py --sessions data/sample/sessions.csv \
                          --participants data/sample/participants.csv \
                          --survey data/sample/survey.csv
"""
import argparse
import json
from src.loader import load_sessions, load_participants, load_survey
from src.utils.logger import get_logger

logger = get_logger(__name__)

# Benchmark targets
TARGETS = {
    "session_completion_rate": 0.85,
    "voluntary_attendance_rate": 0.60,
    "repeat_attendance_rate": 0.50,
    "csat_score": 2.8,
    "recommend_rate": 0.85,
    "confidence_lift": 1.5,
    "sessions_delivered_rate": 0.95,
}


def score_metric(value: float, target: float) -> int:
    ratio = value / target if target > 0 else 0
    if ratio >= 1.0:
        return 100
    elif ratio >= 0.90:
        return 80
    elif ratio >= 0.75:
        return 60
    elif ratio >= 0.50:
        return 40
    else:
        return 20


def calc_reach(sessions_df, participants_df) -> dict:
    total_unique = participants_df["employee_id"].nunique()
    sessions_planned = sessions_df["planned"].str.upper().eq("Y").sum()
    sessions_delivered = len(sessions_df)
    delivery_rate = sessions_delivered / sessions_planned if sessions_planned > 0 else 0
    sites_covered = sessions_df["site"].nunique()

    metrics = {
        "total_unique_participants": int(total_unique),
        "sessions_delivered": int(sessions_delivered),
        "sessions_planned": int(sessions_planned),
        "sessions_delivered_rate": round(delivery_rate, 4),
        "sites_covered": int(sites_covered),
    }
    score = score_metric(delivery_rate, TARGETS["sessions_delivered_rate"])
    return {"metrics": metrics, "score": score}


def calc_engagement(participants_df) -> dict:
    total_records = len(participants_df)
    completed = participants_df["completed_session"].sum()
    completion_rate = completed / total_records if total_records > 0 else 0

    voluntary = participants_df["voluntary"].sum()
    voluntary_rate = voluntary / total_records if total_records > 0 else 0

    repeat = participants_df[participants_df["prior_sessions_attended"] >= 1]["employee_id"].nunique()
    total_unique = participants_df["employee_id"].nunique()
    repeat_rate = repeat / total_unique if total_unique > 0 else 0

    metrics = {
        "session_completion_rate": round(completion_rate, 4),
        "voluntary_attendance_rate": round(voluntary_rate, 4),
        "repeat_attendance_rate": round(repeat_rate, 4),
        "total_completions": int(completed),
        "total_voluntary": int(voluntary),
        "total_repeat_attendees": int(repeat),
    }
    scores = [
        score_metric(completion_rate, TARGETS["session_completion_rate"]),
        score_metric(voluntary_rate, TARGETS["voluntary_attendance_rate"]),
        score_metric(repeat_rate, TARGETS["repeat_attendance_rate"]),
    ]
    return {"metrics": metrics, "score": round(sum(scores) / len(scores))}


def calc_effectiveness(survey_df) -> dict:
    avg_csat = survey_df["overall_rating"].mean()
    recommend_rate = survey_df["would_recommend"].mean()
    avg_confidence_before = survey_df["confidence_before"].mean()
    avg_confidence_after = survey_df["confidence_after"].mean()
    confidence_lift = avg_confidence_after - avg_confidence_before

    metrics = {
        "csat_score": round(avg_csat, 3),
        "csat_max": 3.0,
        "recommend_rate": round(recommend_rate, 4),
        "avg_confidence_before": round(avg_confidence_before, 2),
        "avg_confidence_after": round(avg_confidence_after, 2),
        "confidence_lift": round(confidence_lift, 2),
        "survey_responses": len(survey_df),
    }
    scores = [
        score_metric(avg_csat, TARGETS["csat_score"]),
        score_metric(recommend_rate, TARGETS["recommend_rate"]),
        score_metric(confidence_lift, TARGETS["confidence_lift"]),
    ]
    return {"metrics": metrics, "score": round(sum(scores) / len(scores))}


def calc_momentum(sessions_df, participants_df) -> dict:
    # Month-over-month session growth
    sessions_df = sessions_df.copy()
    sessions_df["month"] = sessions_df["session_date"].dt.to_period("M")
    monthly = sessions_df.groupby("month").size()
    if len(monthly) >= 2:
        last = monthly.iloc[-1]
        prev = monthly.iloc[-2]
        mom_growth = (last - prev) / prev if prev > 0 else 0
    else:
        mom_growth = 0

    # Repeat engagement as momentum proxy
    repeat_sessions = participants_df[participants_df["prior_sessions_attended"] >= 2]["employee_id"].nunique()
    total_unique = participants_df["employee_id"].nunique()
    deep_engagement_rate = repeat_sessions / total_unique if total_unique > 0 else 0

    metrics = {
        "mom_session_growth": round(mom_growth, 4),
        "deep_engagement_rate": round(deep_engagement_rate, 4),
        "participants_3plus_sessions": int(repeat_sessions),
    }
    score = 80 if mom_growth >= 0 else 40
    return {"metrics": metrics, "score": score}


def calculate_all(sessions_path: str, participants_path: str, survey_path: str) -> dict:
    sessions = load_sessions(sessions_path)
    participants = load_participants(participants_path)
    survey = load_survey(survey_path)

    reach = calc_reach(sessions, participants)
    engagement = calc_engagement(participants)
    effectiveness = calc_effectiveness(survey)
    momentum = calc_momentum(sessions, participants)

    # Weighted overall score
    overall = round(
        reach["score"] * 0.20 +
        engagement["score"] * 0.25 +
        effectiveness["score"] * 0.35 +
        momentum["score"] * 0.20
    )

    return {
        "overall_score": overall,
        "reach": reach,
        "engagement": engagement,
        "effectiveness": effectiveness,
        "momentum": momentum,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate AI adoption metrics.")
    parser.add_argument("--sessions", required=True)
    parser.add_argument("--participants", required=True)
    parser.add_argument("--survey", required=True)
    args = parser.parse_args()

    results = calculate_all(args.sessions, args.participants, args.survey)
    print(json.dumps(results, indent=2))
