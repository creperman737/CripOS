#!/usr/bin/env python3
"""crip-center - open Crip Center settings."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import importlib.util

# Load ui directly from file path (avoids package import issues)
UI_PATH = REPO_ROOT / "apps" / "crip-center" / "ui.py"
spec = importlib.util.spec_from_file_location("crip_center_ui", UI_PATH)
ui_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ui_module)
get_center_sections = ui_module.get_center_sections


def main() -> None:
    print("💚 Crip Center")
    print("=" * 35)
    print("\nSections:")
    for section in get_center_sections():
        print(f"  • {section}")

    if "open" in sys.argv:
        print("\nOpening Crip Center GUI...")
        try:
            from apps.crip_center.main import run_center
            run_center()
        except ImportError:
            print("  GUI not available. Use --list to see sections.")


if __name__ == "__main__":
    main()