"""Hochschule Reutlingen timetable client — convenience wrapper for WebUntis."""

from .client import HSRTClient
from .programs import PROGRAMS, parse_group_name, program_search_pattern, semester_group_name
from .semesters import AcademicSemester, get_current_semester, get_semester, get_semester_by_name

__all__ = [
    "AcademicSemester",
    "HSRTClient",
    "PROGRAMS",
    "get_current_semester",
    "get_semester",
    "get_semester_by_name",
    "parse_group_name",
    "program_search_pattern",
    "semester_group_name",
]

__version__ = "0.2.0"
