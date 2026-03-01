"""Pre-configured WebUntis client for Hochschule Reutlingen."""

from __future__ import annotations

import datetime

from webuntis_public import ClassGroup, SemesterTimetable, WebUntisPublicClient

from .programs import program_search_pattern
from .semesters import AcademicSemester, get_current_semester


HSRT_SERVER = "hs-reutlingen.webuntis.com"


class HSRTClient:
    """Convenience wrapper around :class:`WebUntisPublicClient` pre-configured
    for Hochschule Reutlingen.

    Usage::

        client = HSRTClient()
        mkib_classes = client.get_program_classes("MKIB")
        timetable = client.fetch_program_semester("3MKIB6")
    """

    def __init__(self, *, rate_limit: float = 0.3) -> None:
        self._client = WebUntisPublicClient(HSRT_SERVER, rate_limit=rate_limit)

    @property
    def inner(self) -> WebUntisPublicClient:
        """Access the underlying :class:`WebUntisPublicClient`."""
        return self._client

    def list_classes(self) -> list[ClassGroup]:
        """List all class groups at HSRT."""
        return self._client.list_classes()

    def get_program_classes(self, program: str) -> list[ClassGroup]:
        """Find all class groups for a study program (e.g. ``"MKIB"``)."""
        pattern = program_search_pattern(program)
        return self._client.find_classes(pattern)

    def get_current_semester(self) -> AcademicSemester | None:
        """Return the current HSRT academic semester, if known."""
        return get_current_semester()

    def fetch_program_semester(
        self,
        group_name: str,
        semester: AcademicSemester | None = None,
        *,
        on_error: str = "warn",
    ) -> SemesterTimetable:
        """Fetch a full semester of timetable data for a specific class group.

        Parameters
        ----------
        group_name:
            The class group name, e.g. ``"3MKIB6"``.
        semester:
            The academic semester to fetch.  Defaults to the current semester.
        on_error:
            Error handling strategy (``"warn"``, ``"raise"``, or ``"skip"``).
        """
        if semester is None:
            semester = get_current_semester()
            if semester is None:
                raise ValueError(
                    "No current semester found. Pass a semester explicitly."
                )

        # Find the class ID for this group name
        matches = self._client.find_classes(group_name)
        exact = [c for c in matches if c.name == group_name]
        if not exact:
            raise ValueError(
                f"Class group '{group_name}' not found on server. "
                f"Found: {[c.name for c in matches]}"
            )
        class_id = exact[0].id

        return self._client.fetch_semester(
            class_id,
            semester.lecture_start,
            semester.lecture_end,
            on_error=on_error,
        )
