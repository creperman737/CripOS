# CripOS Testing

## Overview

CripOS uses Python's `unittest` framework for testing. All tests are automated and can be run individually or together.

## Test Files

### `tests/test_alpha_apps.py`

Tests the core application APIs.

```bash
python tests/test_alpha_apps.py
```

**Tests:**
- Launcher has core apps (Files, Terminal, Settings)
- Center has core sections (Appearance, Updates, About)

**Expected output:** `Ran 2 tests ... OK`

---

### `tests/test_system_modules.py`

Tests the system layer modules.

```bash
python tests/test_system_modules.py
```

**Test classes:**
- `BootTests` — disk space and memory checks
- `LoginTests` — password hashing
- `SecurityTests` — security config defaults
- `UpdateTests` — update config defaults
- `StartupTests` — startup config defaults

**Expected output:** `Ran 10 tests ... OK`

---

### `tests/test_sdk.py`

Tests the SDK packages.

```bash
python tests/test_sdk.py
```

**Test classes:**
- `CripAPITests` — system_status, system_info, get_apps, get_version
- `CripUITests` — button, label, input, checkbox, dropdown, progress_bar
- `CripWidgetTests` — card, window, dialog, toast, sidebar, toolbar
- `CripThemeTests` — default, light, minecraft themes

**Expected output:** `Ran 20 tests ... OK`

---

### `apps/crip-welcome/test_ui.py`

Tests the Crip Welcome application.

```bash
python apps/crip-welcome/test_ui.py
```

**Tests:**
- Localized string loading (uz/en)
- Language fallback to Uzbek
- Config merge with defaults
- Config save to explicit path
- Flow state machine (language → internet → complete)
- Skip window when setup complete
- Internet check success/offline
- PNG asset validation

**Expected output:** `Ran 9 tests ... OK`

## Running All Tests

### On Windows (PowerShell):

```powershell
python tests/test_alpha_apps.py
python tests/test_system_modules.py
python tests/test_sdk.py
python apps/crip-welcome/test_ui.py
```

### On Linux:

```bash
python -m unittest discover tests -v
```

## Test Count Summary

| Test File | Tests |
|---|---|
| `tests/test_alpha_apps.py` | 2 |
| `tests/test_system_modules.py` | 10 |
| `tests/test_sdk.py` | 20 |
| `apps/crip-welcome/test_ui.py` | 9 |
| **Total** | **41** |

## Adding New Tests

1. Create a test file in `tests/` or alongside app code
2. Import the modules you want to test
3. Use `unittest.TestCase` classes
4. Run with `python <test_file>.py`

Example:

```python
"""Test for my module."""
import unittest
from system.boot.boot import check_disk_space


class MyModuleTests(unittest.TestCase):
    def test_disk_space_returns_bool(self):
        result = check_disk_space()
        self.assertIsInstance(result, bool)


if __name__ == "__main__":
    unittest.main()
```

## Code Quality Checks

The repo includes helper scripts in `scripts/`:

| Script | Purpose |
|---|---|
| `check_errors.py` | Python syntax validation across all files |
| `check_imports.py` | Import resolution testing |
| `check_json.py` | JSON file validation |
| `check_packages.py` | Package structure validation |

Run all checks:

```bash
python scripts/check_errors.py
python scripts/check_imports.py
python scripts/check_json.py
python scripts/check_packages.py