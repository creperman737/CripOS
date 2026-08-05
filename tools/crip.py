#!/usr/bin/env python3
"""Unified CLI for CripOS: `crip <subcommand>`."""

import sys
import importlib.util
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from sdk.cripapi import get_version

COMMANDS = {
    "about": "Show CripOS branding and about info",
    "doctor": "Diagnose system health and structure",
    "update": "Check for system updates",
    "center": "Open Crip Center settings",
    "welcome": "Run Crip Welcome wizard",
    "store": "Open Crip Store",
    "files": "Open Crip Files manager",
    "version": "Display CripOS version",
    "info": "Display system information",
}


def _load_and_run(tool_name: str, func_name: str = "main", *args) -> None:
    path = REPO_ROOT / "tools" / f"{tool_name}.py"
    if not path.exists():
        print(f"Tool {tool_name} not found.")
        return
    spec = importlib.util.spec_from_file_location(tool_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    fn = getattr(module, func_name, None)
    if callable(fn):
        fn(*args)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    if len(sys.argv) < 2 or sys.argv[1] in ["-h", "--help", "help"]:
        print("💚 CripOS CLI Control Tool")
        print("=" * 35)
        print("Usage: crip <command> [options]\n")
        print("Commands:")
        for cmd, desc in COMMANDS.items():
            print(f"  {cmd:<12} : {desc}")
        print("=" * 35)
        return

    cmd = sys.argv[1].lower()

    if cmd == "version":
        print(get_version())
    elif cmd == "about":
        _load_and_run("crip-about")
    elif cmd == "doctor":
        _load_and_run("crip-doctor", "run_doctor")
    elif cmd == "info":
        _load_and_run("crip-info")
    elif cmd == "update":
        _load_and_run("crip-update")
    elif cmd == "welcome":
        _load_and_run("crip-welcome")
    elif cmd == "store":
        _load_and_run("crip-store")
    elif cmd == "center":
        _load_and_run("crip-center")
    elif cmd == "files":
        path = REPO_ROOT / "apps" / "crip-files" / "main.py"
        spec = importlib.util.spec_from_file_location("crip_files_main", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.run_files()
    else:
        print(f"Unknown command: '{cmd}'")
        print("Run 'crip help' to see available commands.")


if __name__ == "__main__":
    main()
