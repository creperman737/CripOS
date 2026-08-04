#!/usr/bin/env python3
"""Crip Update - system update manager for CripOS."""

import sys
from pathlib import Path

import tkinter as tk
from tkinter import ttk

APP_DIR = Path(__file__).resolve().parent
REPO_ROOT = APP_DIR.parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from api.updates import get_update_status


class UpdateWindow:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Crip Update")
        self.root.geometry("520x420")
        self.root.configure(bg="#161B22")

        header = tk.Frame(root, bg="#161B22")
        header.pack(fill="x", padx=20, pady=(20, 10))

        tk.Label(
            header,
            text="Crip Update",
            fg="#F0F6FC",
            bg="#161B22",
            font=("Segoe UI", 16, "bold"),
        ).pack(side="left")

        self.status_label = tk.Label(
            header,
            text="",
            fg="#39D353",
            bg="#161B22",
            font=("Segoe UI", 10),
        )
        self.status_label.pack(side="right")

        self.list_frame = tk.Frame(root, bg="#161B22")
        self.list_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.tree = ttk.Treeview(self.list_frame, columns=("desc",), show="tree")
        self.tree.heading("#0", text="Package")
        self.tree.heading("desc", text="Description")
        self.tree.column("#0", width=200)
        self.tree.column("desc", width=250)
        self.tree.pack(fill="both", expand=True)

        actions = tk.Frame(root, bg="#161B22")
        actions.pack(fill="x", padx=20, pady=(0, 20))

        tk.Button(
            actions,
            text="Check for Updates",
            bg="#39D353",
            fg="#0D1117",
            relief="flat",
            padx=16,
            pady=8,
            font=("Segoe UI", 10, "bold"),
            command=self.check_updates,
        ).pack(side="left")

        tk.Button(
            actions,
            text="Install Updates",
            bg="#2EA043",
            fg="#0D1117",
            relief="flat",
            padx=16,
            pady=8,
            font=("Segoe UI", 10, "bold"),
            command=self.install_updates,
        ).pack(side="right")

    def check_updates(self) -> None:
        """Check for available updates."""
        status = get_update_status()
        available = status.get("available", 0)
        self.status_label.config(text=f"{available} available")
        self.tree.delete(*self.tree.get_children())

    def install_updates(self) -> None:
        """Install available updates."""
        status = get_update_status()
        available = status.get("available", 0)
        if available == 0:
            self.status_label.config(text="Up to date")
            return
        self.status_label.config(text="Installing...")


def run_update() -> None:
    root = tk.Tk()
    UpdateWindow(root)
    root.mainloop()


if __name__ == "__main__":
    run_update()