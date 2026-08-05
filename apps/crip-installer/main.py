#!/usr/bin/env python3
"""Crip Installer - system installer for CripOS."""

import subprocess
import sys
from pathlib import Path

import tkinter as tk
from tkinter import ttk

APP_DIR = Path(__file__).resolve().parent
REPO_ROOT = APP_DIR.parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


class InstallerWindow:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Crip Installer")
        self.root.geometry("640x480")
        self.root.configure(bg="#161B22")

        tk.Label(
            root,
            text="CripOS Installer",
            fg="#F0F6FC",
            bg="#161B22",
            font=("Segoe UI", 18, "bold"),
        ).pack(pady=(30, 10))

        tk.Label(
            root,
            text="Install CripOS on this computer",
            fg="#8B949E",
            bg="#161B22",
            font=("Segoe UI", 11),
        ).pack(pady=(0, 20))

        # Installation options
        options = tk.Frame(root, bg="#161B22")
        options.pack(fill="x", padx=40, pady=10)

        self.install_type = tk.StringVar(value="full")
        for text, value in [
            ("Full Installation (Recommended)", "full"),
            ("Minimal Installation", "minimal"),
            ("Custom Installation", "custom"),
        ]:
            tk.Radiobutton(
                options,
                text=text,
                variable=self.install_type,
                value=value,
                bg="#161B22",
                fg="#F0F6FC",
                selectcolor="#2EA043",
                activebackground="#161B22",
                activeforeground="#F0F6FC",
                font=("Segoe UI", 11),
                anchor="w",
            ).pack(fill="x", pady=4)

        # Progress bar
        self.progress = ttk.Progressbar(root, mode="determinate", maximum=100)
        self.progress.pack(fill="x", padx=40, pady=20)

        self.status_label = tk.Label(
            root,
            text="Ready to install",
            fg="#8B949E",
            bg="#161B22",
            font=("Segoe UI", 10),
        )
        self.status_label.pack(pady=(0, 10))

        # Buttons
        actions = tk.Frame(root, bg="#161B22")
        actions.pack(fill="x", padx=40, pady=(0, 20))

        tk.Button(
            actions,
            text="Cancel",
            bg="#30363D",
            fg="#F0F6FC",
            relief="flat",
            padx=16,
            pady=8,
            font=("Segoe UI", 10),
            command=root.destroy,
        ).pack(side="left")

        tk.Button(
            actions,
            text="Install",
            bg="#39D353",
            fg="#0D1117",
            relief="flat",
            padx=24,
            pady=8,
            font=("Segoe UI", 10, "bold"),
            command=self.start_install,
        ).pack(side="right")

    def start_install(self) -> None:
        """Start the installation process."""
        install_script = REPO_ROOT / "installer" / "install.sh"
        if not install_script.exists():
            self.status_label.config(text="❌ install.sh not found")
            return

        self.status_label.config(text="Installing CripOS...")
        self.progress["value"] = 10
        self.root.update()

        try:
            result = subprocess.run(
                ["bash", str(install_script)],
                check=False,
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                self.status_label.config(text="✅ Installation complete! Please reboot.")
                self.progress["value"] = 100
            else:
                self.status_label.config(text="❌ Installation failed (run as root?)")
                self.progress["value"] = 0
        except FileNotFoundError:
            self.status_label.config(text="❌ bash not found")
            self.progress["value"] = 0


def run_installer() -> None:
    root = tk.Tk()
    InstallerWindow(root)
    root.mainloop()


if __name__ == "__main__":
    run_installer()