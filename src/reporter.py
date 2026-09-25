"""
reporter.py -- Generate Markdown and CSV adoption health reports.

Usage:
    python src/reporter.py --sessions data/sample/sessions.csv \
                           --participants data/sample/participants.csv \
                           --survey data/sample/survey.csv \
                           --output data/outputs/
"""
import argparse
import csv
from datetime import datetime
from pathlib import Path

from src.metrics import calculate_all, TARGETS
from src.scorer import interpret_score, flag_attention_areas
from src.utils.logger import get_logger

logger = get_logger(__name__)


def pct(value: float) -> str:
    return f"{value * 100:.1f}%"


def target_status(actual: float, target: float) -> str:
    return "PASS" if actual >= target else "BELOW TARGET"


def build_markdown_report(results: dict, period: str = "Q1 2026", program: str = "AI Enablement Program") -> str:
    ts = datetime.now().strftime("%Y-%m-%d")
    overall = results["overall_score"]
    interpretation = interpret_score(overall)
    attention = flag_attention_areas(results, TARGETS)

    eng = results["engagement"]["metrics"]
    eff = results["effectiveness"]["metrics"]
    reach = results["reach"]["metrics"]

    lines = []
    lines.append("# AI Adoption Health Report")
    lines.append(f"\n**Program:** {program}")
    lines.append(f"**Reporting Period:** {period}")
    lines.append(f"**Generated:** {ts}")
    lines.append("\n---\n")

    lines.append(f"## Overall Adoption Heal