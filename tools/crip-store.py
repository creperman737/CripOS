#!/usr/bin/env python3
"""crip-store - open Crip Store or list apps."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from api.store import get_store_categories
from sdk.cripapi import get_apps


def main() -> None:
    print("💚 Crip Store")
    print("=" * 35)

    if "--categories" in sys.argv:
        print("\nCategories:")
        for cat in get_store_categories():
            print(f"  • {cat}")
    else:
        print("\nApplications:")
        for app in get_apps():
            print(f"  • {app}")
        print("\n  Use --categories to see categories")


if __name__ == "__main__":
    main()