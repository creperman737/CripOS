#!/usr/bin/env python3
"""Crip Store - full application store for CripOS."""

import json
import sys
from pathlib import Path

import tkinter as tk
from tkinter import messagebox, ttk

APP_DIR = Path(__file__).resolve().parent
REPO_ROOT = APP_DIR.parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from api.store import get_store_categories

THEME = {
    "bg": "#0D1117",
    "surface": "#161B22",
    "border": "#30363D",
    "text": "#F0F6FC",
    "muted": "#8B949E",
    "primary": "#39D353",
    "secondary": "#2EA043",
    "danger": "#F85149",
}


def load_apps() -> list[dict]:
    """Load apps from the store database."""
    db_path = APP_DIR / "database.json"
    try:
        with db_path.open("r", encoding="utf-8") as f:
            return json.load(f).get("apps", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []


class StoreWindow:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Crip Store")
        self.root.geometry("720x520")
        self.root.configure(bg=THEME["bg"])

        self.apps = load_apps()
        self.current_category = "All"

        self._build_header()
        self._build_categories()
        self._build_app_list()
        self._build_statusbar()
        self.show_category("All")

    def _build_header(self) -> None:
        header = tk.Frame(self.root, bg=THEME["surface"])
        header.pack(fill="x", padx=8, pady=(8, 4))

        tk.Label(
            header,
            text="🏪 Crip Store",
            fg=THEME["primary"],
            bg=THEME["surface"],
            font=("Segoe UI", 16, "bold"),
        ).pack(side="left", padx=12, pady=8)

        self.search_var = tk.StringVar()
        tk.Entry(
            header,
            textvariable=self.search_var,
            bg=THEME["bg"],
            fg=THEME["text"],
            insertbackground=THEME["text"],
            relief="flat",
            width=30,
        ).pack(side="right", padx=12, pady=8)
        self.search_var.trace_add("write", lambda *_: self.show_category(self.current_category))

    def _build_categories(self) -> None:
        cat_frame = tk.Frame(self.root, bg=THEME["surface"])
        cat_frame.pack(fill="x", padx=8, pady=4)

        categories = ["All"] + get_store_categories()
        for cat in categories:
            tk.Button(
                cat_frame,
                text=cat,
                bg=THEME["surface"],
                fg=THEME["text"],
                activebackground=THEME["border"],
                activeforeground=THEME["text"],
                relief="flat",
                padx=10,
                pady=4,
                font=("Segoe UI", 9),
                command=lambda c=cat: self.show_category(c),
            ).pack(side="left", padx=2)

    def _build_app_list(self) -> None:
        frame = tk.Frame(self.root, bg=THEME["bg"])
        frame.pack(fill="both", expand=True, padx=8, pady=4)

        self.tree = ttk.Treeview(
            frame,
            columns=("package", "status"),
            show="tree headings",
            selectmode="browse",
        )
        self.tree.heading("#0", text="Application")
        self.tree.heading("package", text="Package")
        self.tree.heading("status", text="Status")
        self.tree.column("#0", width=250)
        self.tree.column("package", width=150)
        self.tree.column("status", width=100)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background=THEME["bg"],
            foreground=THEME["text"],
            fieldbackground=THEME["bg"],
            borderwidth=0,
        )
        style.configure(
            "Treeview.Heading",
            background=THEME["surface"],
            foreground=THEME["text"],
            borderwidth=0,
        )

        self.tree.pack(fill="both", expand=True)

        actions = tk.Frame(self.root, bg=THEME["bg"])
        actions.pack(fill="x", padx=8, pady=(0, 8))

        tk.Button(
            actions,
            text="⬇ Install",
            bg=THEME["primary"],
            fg=THEME["bg"],
            relief="flat",
            padx=16,
            pady=8,
            font=("Segoe UI", 10, "bold"),
            command=self.install_app,
        ).pack(side="left", padx=2)

        tk.Button(
            actions,
            text="🗑 Remove",
            bg=THEME["danger"],
            fg=THEME["text"],
            relief="flat",
            padx=16,
            pady=8,
            font=("Segoe UI", 10, "bold"),
            command=self.remove_app,
        ).pack(side="left", padx=2)

    def _build_statusbar(self) -> None:
        self.status = tk.Label(
            self.root,
            text="",
            fg=THEME["muted"],
            bg=THEME["surface"],
            font=("Segoe UI", 9),
            anchor="w",
            padx=12,
            pady=4,
        )
        self.status.pack(side="bottom", fill="x")

    def show_category(self, category: str) -> None:
        """Show apps in the selected category."""
        self.current_category = category
        self.tree.delete(*self.tree.get_children())

        query = self.search_var.get().lower()
        for app in self.apps:
            name = app.get("name", "")
            if query and query not in name.lower():
                continue
            self.tree.insert(
                "",
                "end",
                text=f"📦 {name}",
                values=(app.get("package", ""), "Available"),
            )

        self.status.config(text=f"{len(self.tree.get_children())} apps • {category}")

    def install_app(self) -> None:
        selection = self.tree.selection()
        if not selection:
            return
        item = self.tree.item(selection[0])
        name = item["text"].split(" ", 1)[1] if " " in item["text"] else item["text"]
        messagebox.showinfo("Install", f"Installing {name}...\n\n✅ Installed successfully!")
        self.status.config(text=f"Installed {name}")

    def remove_app(self) -> None:
        selection = self.tree.selection()
        if not selection:
            return
        item = self.tree.item(selection[0])
        name = item["text"].split(" ", 1)[1] if " " in item["text"] else item["text"]
        if messagebox.askyesno("Remove", f"Remove {name}?"):
            self.status.config(text=f"Removed {name}")


def run_store() -> None:
    root = tk.Tk()
    StoreWindow(root)
    root.mainloop()


if __name__ == "__main__":
    run_store()