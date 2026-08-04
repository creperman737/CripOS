#!/usr/bin/env python3
"""Crip Store entrypoint."""

import sys
from pathlib import Path

import tkinter as tk

APP_DIR = Path(__file__).resolve().parent
REPO_ROOT = APP_DIR.parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from api.store import get_store_categories


class StoreWindow:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Crip Store")
        self.root.geometry("520x420")
        self.root.configure(bg="#161B22")

        tk.Label(
            root,
            text="Crip Store",
            fg="#F0F6FC",
            bg="#161B22",
            font=("Segoe UI", 16, "bold"),
        ).pack(pady=(20, 10))

        for category in get_store_categories():
            tk.Button(
                root,
                text=category,
                bg="#39D353",
                fg="#0D1117",
                relief="flat",
                padx=10,
                pady=6,
                command=lambda c=category: print(f"Open {c}"),
            ).pack(fill="x", padx=20, pady=4)


def run_store() -> None:
    root = tk.Tk()
    StoreWindow(root)
    root.mainloop()


if __name__ == "__main__":
    run_store()
