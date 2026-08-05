#!/usr/bin/env python3
"""crip-about - show CripOS branding and about information."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from branding.splash import get_all_splash_texts, get_splash_text


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    print("💚 CripOS")
    print("=" * 35)
    print(f"  {get_splash_text()}")
    print()
    print("  CripOS is a modern Debian-based operating system")
    print("  built with Python and modular components.")
    print()
    print("  Base       : Debian 13 (Trixie)")
    print("  Desktop    : Cinnamon")
    print("  Version    : Alpha 0.1")
    print("  Codename   : Creeper")
    print("  Author     : Criperman")
    print()
    print("  Tagline    : Never Give Up.")
    print()
    print("  Repository : https://github.com/creperman737/CripOS")
    print()

    if "--splash" in sys.argv:
        print("Splash Texts:")
        for text in get_all_splash_texts():
            print(f"  ✨ {text}")


if __name__ == "__main__":
    main()