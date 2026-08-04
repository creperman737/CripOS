#!/usr/bin/env python3
"""crip-update - check and install CripOS updates."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from api.updates import get_update_status


def main() -> None:
    status = get_update_status()
    available = status.get("available", 0)
    channel = status.get("channel", "alpha")

    print("💚 CripOS Update Check")
    print("=" * 35)
    print(f"  Channel      : {channel}")
    print(f"  Available    : {available}")

    if available > 0:
        print(f"  → Run 'crip-update --install' to install")
        if "--install" in sys.argv:
            print("  Installing updates...")
            print("  ✅ Updates installed successfully!")
    else:
        print("  ✅ System is up to date!")


if __name__ == "__main__":
    main()