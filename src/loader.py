"""
loader.py -- Load and validate CSV input data for the measurement framework.
"""
import pandas as pd
from pathlib import Path
from src.utils.logger import get_logger

logger = get_logger(__name__)

SESSION_COLS = [
    "session_id", "session_date", "session_name", "site", "facilitator",
    "registered_count", "attended_count", "completed_count", "duration_minutes", "planned"
]
PARTICIPANT_COLS = [
    "participant_id", "employee_id", "session_id", "session_date", "department",
    "site", "role_level", "voluntary", "completed_session", "prior_sessions_attended"
]
SURVEY_COLS = [
    "response_id", "session_id", "session_date", "overall_rating", "would_recommend",
    "most_useful", "improvement_suggestion", "confidence_before", "confidence_after"
]


def load_sessions(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, comment="#")
    df["session_date"] = pd.to_datetime(df["session_date"])
    logger.info(f"Loaded {len(df)} sessions from {path}")
    return df


def load_participants(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, comment="#")
    df["session_date"] = pd.to_datetime(df["session_date"])
    df["voluntary"] = df["voluntary"].str.upper() == "Y"
    df["completed_session"] = df["completed_session"].str.upper() == "Y"
    logger.info(f"Loaded {len(df)} participant records from {path}")
    return df


def load_survey(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, comment="#")
    df["session_date"] = pd.to_datetime(df["session_date"])
    df["would_recommend"] = df["would_recommend"].str.upper() == "Y"
    logger.info(f"Loaded {len(df)} survey responses from {path}")
    return df
