#!/usr/bin/env python3
"""crip-welcome - show the CripOS welcome screen."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from branding.splash import get_splash_text


def main() -> None:
    print("💚 CripOS Welcome")
    print("=" * 35)
    print(f"  {get_splash_text()}")
    print("=" * 35)
    print("  Welcome to CripOS!")
    print("  Use 'crip-center' to configure your system.")
    print("  Use 'crip-store' to browse applications.")


if __name__ == "__main__":
    main()