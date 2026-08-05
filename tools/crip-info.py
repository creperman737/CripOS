#!/usr/bin/env python3
"""crip-info - display CripOS system information."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from sdk.cripapi import system_info, get_version
from branding.splash import get_splash_text


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    info = system_info()
    print("💚 CripOS System Information")
    print("=" * 35)
    print(f"  {get_splash_text()}")
    print("=" * 35)
    for key, value in info.items():
        print(f"  {key.capitalize():<14}: {value}")


if __name__ == "__main__":
    main()