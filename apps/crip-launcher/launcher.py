#!/usr/bin/env python3
"""Crip Launcher - a start-menu-like interface with search, favorites, recent, categories."""

import json
import sys
from pathlib import Path

import tkinter as tk

APP_DIR = Path(__file__).resolve().parent
REPO_ROOT = APP_DIR.parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

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

# App registry: name -> (category, icon)
APPS = {
    "Files": ("System", "📁"),
    "Browser": ("Internet", "🌐"),
    "Terminal": ("System", "💻"),
    "Settings": ("System", "⚙️"),
    "Store": ("System", "🛒"),
    "Updates": ("System", "🔄"),
    "Games": ("Games", "🎮"),
    "Welcome": ("System", "👋"),
    "Center": ("System", "🖌️"),
    "Monitor": ("System", "📊"),
    "Installer": ("System", "💿"),
}

CATEGORIES = ["All", "System", "Internet", "Games"]

CONFIG_PATH = Path.home() / ".config" / "cripos" / "launcher.json"


def get_launcher_apps() -> list[str]:
    """Return the list of core launcher apps."""
    return list(APPS.keys())


def get_categories() -> list[str]:
    """Return the list of launcher categories."""
    return CATEGORIES.copy()


def load_launcher_config() -> dict:
    """Load launcher preferences (favorites, recent)."""
    defaults = {"favorites": [], "recent": []}
    try:
        with CONFIG_PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)
            defaults.update(data)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return defaults


def save_launcher_config(config: dict) -> None:
    """Save launcher preferences."""
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with CONFIG_PATH.open("w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)


class LauncherWindow:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Crip Launcher")
        self.root.geometry("360x520")
        self.root.configure(bg=THEME["bg"])

        self.config = load_launcher_config()
        self.current_category = "All"
        self.search_query = ""

        self._build_search()
        self._build_categories()
        self._build_app_list()
        self._build_footer()
        self.refresh_apps()

    def _build_search(self) -> None:
        search_frame = tk.Frame(self.root, bg=THEME["surface"])
        search_frame.pack(fill="x", padx=12, pady=(12, 4))

        self.search_var = tk.StringVar()
        tk.Entry(
            search_frame,
            textvariable=self.search_var,
            bg=THEME["bg"],
            fg=THEME["text"],
            insertbackground=THEME["text"],
            relief="flat",
            font=("Segoe UI", 11),
        ).pack(fill="x", padx=8, pady=8)
        self.search_var.trace_add("write", lambda *_: self._on_search())

    def _on_search(self) -> None:
        self.search_query = self.search_var.get().lower()
        self.refresh_apps()

    def _build_categories(self) -> None:
        cat_frame = tk.Frame(self.root, bg=THEME["surface"])
        cat_frame.pack(fill="x", padx=12, pady=4)

        for cat in CATEGORIES:
            tk.Button(
                cat_frame,
                text=cat,
                bg=THEME["surface"],
                fg=THEME["text"],
                activebackground=THEME["border"],
                activeforeground=THEME["text"],
                relief="flat",
                padx=8,
                pady=4,
                font=("Segoe UI", 9),
                command=lambda c=cat: self._select_category(c),
            ).pack(side="left", padx=2)

    def _select_category(self, category: str) -> None:
        self.current_category = category
        self.refresh_apps()

    def _build_app_list(self) -> None:
        self.list_frame = tk.Frame(self.root, bg=THEME["bg"])
        self.list_frame.pack(fill="both", expand=True, padx=12, pady=4)

    def _build_footer(self) -> None:
        footer = tk.Frame(self.root, bg=THEME["surface"])
        footer.pack(fill="x", side="bottom")

        tk.Label(
            footer,
            text="⭐ Favorites",
            fg=THEME["muted"],
            bg=THEME["surface"],
            font=("Segoe UI", 9, "bold"),
        ).pack(anchor="w", padx=12, pady=(8, 2))

        self.fav_frame = tk.Frame(footer, bg=THEME["surface"])
        self.fav_frame.pack(fill="x", padx=12, pady=(0, 8))
        self._render_favorites()

    def _render_favorites(self) -> None:
        for widget in self.fav_frame.winfo_children():
            widget.destroy()
        favorites = self.config.get("favorites", [])
        if not favorites:
            tk.Label(
                self.fav_frame,
                text="No favorites yet. Click ⭐ on an app.",
                fg=THEME["muted"],
                bg=THEME["surface"],
                font=("Segoe UI", 9),
            ).pack(anchor="w")
        else:
            for name in favorites:
                icon = APPS.get(name, ("", "📦"))[1]
                tk.Button(
                    self.fav_frame,
                    text=f"{icon} {name}",
                    bg=THEME["surface"],
                    fg=THEME["text"],
                    activebackground=THEME["border"],
                    activeforeground=THEME["text"],
                    relief="flat",
                    anchor="w",
                    padx=8,
                    pady=2,
                    font=("Segoe UI", 9),
                    command=lambda n=name: self._launch(n),
                ).pack(fill="x")

    def refresh_apps(self) -> None:
        """Rebuild the app list based on category and search."""
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        for name, (category, icon) in APPS.items():
            if self.current_category != "All" and category != self.current_category:
                continue
            if self.search_query and self.search_query not in name.lower():
                continue

            row = tk.Frame(self.list_frame, bg=THEME["bg"])
            row.pack(fill="x", pady=2)

            is_fav = name in self.config.get("favorites", [])
            star = "★" if is_fav else "☆"

            tk.Button(
                row,
                text=f"{icon} {name}",
                bg=THEME["bg"],
                fg=THEME["text"],
                activebackground=THEME["border"],
                activeforeground=THEME["text"],
                relief="flat",
                anchor="w",
                padx=10,
                pady=6,
                font=("Segoe UI", 11),
                command=lambda n=name: self._launch(n),
            ).pack(side="left", fill="x", expand=True)

            tk.Button(
                row,
                text=star,
                bg=THEME["bg"],
                fg=THEME["primary"],
                activebackground=THEME["border"],
                relief="flat",
                padx=8,
                font=("Segoe UI", 12),
                command=lambda n=name: self._toggle_favorite(n),
            ).pack(side="right")

    def _launch(self, name: str) -> None:
        """Launch an app and record it in recent."""
        print(f"Open {name}")
        recent = self.config.get("recent", [])
        if name in recent:
            recent.remove(name)
        recent.insert(0, name)
        self.config["recent"] = recent[:5]
        save_launcher_config(self.config)

    def _toggle_favorite(self, name: str) -> None:
        favorites = self.config.get("favorites", [])
        if name in favorites:
            favorites.remove(name)
        else:
            favorites.append(name)
        self.config["favorites"] = favorites
        save_launcher_config(self.config)
        self.refresh_apps()
        self._render_favorites()


def launch_launcher() -> None:
    root = tk.Tk()
    LauncherWindow(root)
    root.mainloop()


if __name__ == "__main__":
    launch_launcher()