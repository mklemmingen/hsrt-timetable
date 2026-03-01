"""Known study program codes and helpers for Hochschule Reutlingen."""

from __future__ import annotations

# Mapping of program abbreviation -> full name
PROGRAMS: dict[str, str] = {
    "MKIB": "Medien- und Kommunikationsinformatik (Bachelor)",
    "WIB": "Wirtschaftsinformatik (Bachelor)",
    "ACB": "Applied Chemistry (Bachelor)",
    "BME": "Biomedical Engineering (Bachelor)",
    "INB": "Informatik (Bachelor)",
    "MEB": "Mechatronik (Bachelor)",
    "TEB": "Textiltechnologie (Bachelor)",
    "TIB": "Technische Informatik (Bachelor)",
    "UIB": "Umwelt- und Prozessingenieurwesen (Bachelor)",
    "WIM": "Wirtschaftsinformatik (Master)",
    "INM": "Informatik (Master)",
}

# Typical semester prefix pattern: "3" + program + semester number
# e.g. "3MKIB4" = MKIB, 4th semester


def semester_group_name(program: str, semester: int) -> str:
    """Build the class group name for a program and semester number.

    >>> semester_group_name("MKIB", 4)
    '3MKIB4'
    """
    return f"3{program}{semester}"


def program_search_pattern(program: str) -> str:
    """Return a search pattern to find all semester groups of a program.

    >>> program_search_pattern("MKIB")
    '3MKIB'
    """
    return f"3{program}"


def parse_group_name(name: str) -> tuple[str, int] | None:
    """Extract (program, semester) from a group name like '3MKIB4'.

    Returns None if the name doesn't match the expected pattern.
    """
    if not name.startswith("3") or len(name) < 3:
        return None
    # The last character(s) should be the semester number
    body = name[1:]  # strip leading "3"
    # Find where the digits at the end start
    i = len(body) - 1
    while i >= 0 and body[i].isdigit():
        i -= 1
    if i < 0 or i == len(body) - 1:
        return None
    program = body[: i + 1]
    semester = int(body[i + 1 :])
    return (program, semester)
