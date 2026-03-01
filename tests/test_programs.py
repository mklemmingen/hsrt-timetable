"""Tests for HSRT program utilities."""

from hsrt_timetable.programs import (
    parse_group_name,
    program_search_pattern,
    semester_group_name,
)


class TestSemesterGroupName:
    def test_mkib4(self):
        assert semester_group_name("MKIB", 4) == "3MKIB4"

    def test_wib2(self):
        assert semester_group_name("WIB", 2) == "3WIB2"


class TestProgramSearchPattern:
    def test_mkib(self):
        assert program_search_pattern("MKIB") == "3MKIB"


class TestParseGroupName:
    def test_valid(self):
        result = parse_group_name("3MKIB4")
        assert result == ("MKIB", 4)

    def test_double_digit_semester(self):
        result = parse_group_name("3WIB12")
        assert result == ("WIB", 12)

    def test_invalid_no_prefix(self):
        assert parse_group_name("MKIB4") is None

    def test_invalid_too_short(self):
        assert parse_group_name("3A") is None

    def test_invalid_no_digit(self):
        assert parse_group_name("3MKIB") is None
