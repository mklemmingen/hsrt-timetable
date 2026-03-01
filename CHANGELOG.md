# Changelog

## 0.2.0 (2026-03-01)

### Changed

- `HSRTClient` now passes `school="hs-reutlingen"` to `WebUntisPublicClient`,
  enabling anonymous access via the REST v1 API.
- Bumped `webuntis-public` dependency to `>=0.2.0`.

### Fixed

- `get_semester()` now returns the nearest upcoming semester when the date falls
  between semesters (e.g. between WS end and SS start), instead of returning
  `None`. (Fixed in v0.1.1)

## 0.1.1 (2026-03-01)

- Fixed `get_semester()` gap handling for dates between lecture periods.

## 0.1.0 (2025-12-01)

- Initial release with HSRT semester calendar and program utilities.
