"""Tests for HSRTClient (mocked)."""

import datetime
from unittest.mock import patch

from webuntis_public import ClassGroup

from hsrt_timetable.client import HSRTClient
from hsrt_timetable.semesters import AcademicSemester


MOCK_CLASSES = [
    ClassGroup(id=100, name="3MKIB4", long_name="MKIB Sem 4"),
    ClassGroup(id=101, name="3MKIB6", long_name="MKIB Sem 6"),
    ClassGroup(id=200, name="3WIB2", long_name="WIB Sem 2"),
]


class TestGetProgramClasses:
    @patch("hsrt_timetable.client.WebUntisPublicClient.find_classes")
    def test_finds_mkib(self, mock_find):
        mock_find.return_value = MOCK_CLASSES[:2]
        client = HSRTClient(rate_limit=0)
        result = client.get_program_classes("MKIB")
        assert len(result) == 2
        mock_find.assert_called_once_with("3MKIB")


class TestFetchProgramSemester:
    @patch("hsrt_timetable.client.WebUntisPublicClient.fetch_semester")
    @patch("hsrt_timetable.client.WebUntisPublicClient.find_classes")
    def test_fetches_with_semester(self, mock_find, mock_fetch):
        mock_find.return_value = [MOCK_CLASSES[1]]  # 3MKIB6
        client = HSRTClient(rate_limit=0)
        sem = AcademicSemester("SS2026", "SS", datetime.date(2026, 3, 2), datetime.date(2026, 7, 5))
        client.fetch_program_semester("3MKIB6", semester=sem)
        mock_fetch.assert_called_once_with(
            101,
            datetime.date(2026, 3, 2),
            datetime.date(2026, 7, 5),
            on_error="warn",
        )
