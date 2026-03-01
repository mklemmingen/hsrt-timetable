"""HSRT academic calendar utilities."""

from __future__ import annotations

import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class AcademicSemester:
    """Represents an HSRT academic semester with its lecture period dates."""
    name: str  # e.g. "SS2026", "WS2025/26"
    type: str  # "SS" (summer) or "WS" (winter)
    lecture_start: datetime.date
    lecture_end: datetime.date


# Known HSRT semester dates (lecture periods)
SEMESTERS: list[AcademicSemester] = [
    AcademicSemester("WS2025/26", "WS", datetime.date(2025, 10, 6), datetime.date(2026, 1, 30)),
    AcademicSemester("SS2026", "SS", datetime.date(2026, 3, 2), datetime.date(2026, 7, 5)),
    AcademicSemester("WS2026/27", "WS", datetime.date(2026, 10, 5), datetime.date(2027, 1, 29)),
]


def get_semester(date: datetime.date | None = None) -> AcademicSemester | None:
    """Return the academic semester containing the given date.

    Falls back to the current date if not specified.
    Returns None if no matching semester is found.
    """
    if date is None:
        date = datetime.date.today()
    for sem in SEMESTERS:
        if sem.lecture_start <= date <= sem.lecture_end:
            return sem
    return None


def get_current_semester() -> AcademicSemester | None:
    """Return the current academic semester based on today's date."""
    return get_semester()


def get_semester_by_name(name: str) -> AcademicSemester | None:
    """Look up a semester by its name (e.g. 'SS2026')."""
    for sem in SEMESTERS:
        if sem.name == name:
            return sem
    return None
