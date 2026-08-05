#!/usr/bin/env python3
"""Main CripOS CLI wrapper."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO_ROOT))

from tools.crip import main

if __name__ == "__main__":
    main()
