#!/usr/bin/env python3
"""CripOS boot sequence."""

import os
import subprocess
import sys
from pathlib import Path


def check_disk_space() -> bool:
    """Check if there is enough disk space to boot."""
    try:
        if hasattr(os, "statvfs"):
            stat = os.statvfs("/")
            free_gb = (stat.f_bavail * stat.f_frsize) / (1024 ** 3)
            return free_gb > 1.0
        # Fallback for platforms without statvfs (e.g. Windows)
        return True
    except OSError:
        return True


def check_memory() -> bool:
    """Check if there is enough memory to boot."""
    try:
        with open("/proc/meminfo", "r") as f:
            for line in f:
                if line.startswith("MemAvailable:"):
                    available_kb = int(line.split()[1])
                    return available_kb > 512 * 1024  # 512 MB
    except OSError:
        return True
    return True


def start_services() -> None:
    """Start core CripOS services."""
    services = [
        "crip-network.service",
        "crip-notify.service",
        "crip-power.service",
        "crip-update.service",
        "crip-wallpaper.service",
    ]
    for service in services:
        try:
            subprocess.run(
                ["systemctl", "start", service],
                check=False,
                capture_output=True,
            )
        except FileNotFoundError:
            pass


def run_boot() -> None:
    """Execute the boot sequence."""
    print("CripOS booting...")

    if not check_disk_space():
        print("WARNING: Low disk space!")
    if not check_memory():
        print("WARNING: Low memory!")

    start_services()
    print("CripOS boot complete.")


if __name__ == "__main__":
    run_boot()