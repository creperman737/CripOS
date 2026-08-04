#!/usr/bin/env python3
"""CripOS desktop environment manager."""

import os
import subprocess
from pathlib import Path

DESKTOP_DIR = Path("/usr/share/applications")
CRIP_APPS = [
    "crip-center",
    "crip-files",
    "crip-launcher",
    "crip-monitor",
    "crip-store",
    "crip-terminal",
    "crip-update",
    "crip-welcome",
]


def start_desktop() -> None:
    """Start the desktop environment."""
    print("CripOS desktop starting...")

    # Launch Crip Launcher automatically
    launcher_path = "/usr/local/bin/crip-launcher"
    if Path(launcher_path).exists():
        subprocess.Popen([launcher_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("CripOS desktop ready.")


def generate_desktop_entry(app_name: str, exec_path: str, icon_path: str = "") -> str:
    """Generate a .desktop entry for an application."""
    return f"""[Desktop Entry]
Name={app_name}
Comment={app_name} for CripOS
Exec={exec_path}
Icon={icon_path}
Terminal=false
Type=Application
Categories=Utility;
"""


def install_desktop_entry(app_name: str, exec_path: str, icon_path: str = "") -> Path:
    """Install a .desktop entry."""
    DESKTOP_DIR.mkdir(parents=True, exist_ok=True)
    entry_path = DESKTOP_DIR / f"{app_name}.desktop"
    entry_path.write_text(
        generate_desktop_entry(app_name, exec_path, icon_path),
        encoding="utf-8",
    )
    return entry_path


if __name__ == "__main__":
    start_desktop()