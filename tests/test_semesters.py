"""Tests for HSRT academic calendar utilities."""

import datetime

from hsrt_timetable.semesters import get_semester, get_semester_by_name


class TestGetSemester:
    def test_summer_2026(self):
        sem = get_semester(datetime.date(2026, 4, 15))
        assert sem is not None
        assert sem.name == "SS2026"
        assert sem.type == "SS"

    def test_winter_2025(self):
        sem = get_semester(datetime.date(2025, 11, 1))
        assert sem is not None
        assert sem.name == "WS2025/26"

    def test_between_semesters_returns_upcoming(self):
        sem = get_semester(datetime.date(2026, 2, 15))
        assert sem is not None
        assert sem.name == "SS2026"

    def test_day_before_semester_returns_upcoming(self):
        sem = get_semester(datetime.date(2026, 3, 1))
        assert sem is not None
        assert sem.name == "SS2026"

    def test_past_all_semesters_returns_last(self):
        sem = get_semester(datetime.date(2028, 1, 1))
        assert sem is not None
        assert sem.name == "WS2026/27"


class TestGetSemesterByName:
    def test_found(self):
        sem = get_semester_by_name("SS2026")
        assert sem is not None
        assert sem.lecture_start == datetime.date(2026, 3, 2)

    def test_not_found(self):
        assert get_semester_by_name("SS2030") is None
