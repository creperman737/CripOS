#!/usr/bin/env python3
"""Crip Welcome entry point."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


APP_DIR = Path(__file__).resolve().parent
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from ui import run_welcome  # noqa: E402  (path setup is required for symlink launches)


def main() -> None:
    parser = argparse.ArgumentParser(description="Start the CripOS first-run experience.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="show Welcome even after setup has been completed",
    )
    args = parser.parse_args()
    run_welcome(force=args.force)


if __name__ == "__main__":
    main()
