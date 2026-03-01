# hsrt-timetable

Convenience Python client for accessing **Hochschule Reutlingen** timetable data via the WebUntis public API. Built on top of [`webuntis-public`](https://pypi.org/project/webuntis-public/).

## Installation

```bash
pip install hsrt-timetable
```

## Quick Start

```python
from hsrt_timetable import HSRTClient

client = HSRTClient()

# Find all MKIB class groups
mkib_classes = client.get_program_classes("MKIB")
for c in mkib_classes:
    print(f"{c.id}: {c.name}")

# Get current academic semester
semester = client.get_current_semester()
if semester:
    print(f"Current: {semester.name} ({semester.lecture_start} - {semester.lecture_end})")

# Fetch a full semester of timetable data
timetable = client.fetch_program_semester("3MKIB6")
print(f"Total periods: {len(timetable.periods)}")
```

## Programs

Known study programs at HSRT:

| Code | Name |
|------|------|
| MKIB | Medien- und Kommunikationsinformatik (Bachelor) |
| WIB  | Wirtschaftsinformatik (Bachelor) |
| INB  | Informatik (Bachelor) |
| ACB  | Applied Chemistry (Bachelor) |
| BME  | Biomedical Engineering (Bachelor) |
| MEB  | Mechatronik (Bachelor) |

## Utilities

```python
from hsrt_timetable import semester_group_name, parse_group_name

# Build group name from program + semester
semester_group_name("MKIB", 4)  # "3MKIB4"

# Parse group name back
parse_group_name("3MKIB4")  # ("MKIB", 4)
```

## License

MIT
