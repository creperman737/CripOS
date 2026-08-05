#!/usr/bin/env python3
"""Crip Center - full settings application for CripOS."""

import json
import sys
from pathlib import Path

import tkinter as tk
from tkinter import ttk

APP_DIR = Path(__file__).resolve().parent
REPO_ROOT = APP_DIR.parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import sdk.cripthemes as themes

# Theme colors
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

SECTIONS = [
    ("Appearance", "🖌️"),
    ("Wallpaper", "🖼️"),
    ("Language", "🌍"),
    ("Network", "🌐"),
    ("Updates", "🔄"),
    ("Security", "🔒"),
    ("About", "ℹ️"),
]


def get_center_sections() -> list[str]:
    """Return the list of Crip Center sections."""
    return [name for name, _ in SECTIONS]


def load_config() -> dict:
    """Load CripOS user configuration."""
    config_path = Path.home() / ".config" / "cripos" / "center.json"
    defaults = {
        "theme": "crip-dark",
        "language": "uz",
        "firewall": True,
        "auto_updates": True,
        "start_launcher": True,
    }
    try:
        with config_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            defaults.update(data)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return defaults


def save_config(config: dict) -> None:
    """Save CripOS user configuration."""
    config_path = Path.home() / ".config" / "cripos" / "center.json"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    with config_path.open("w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)


def get_language_strings(lang: str) -> dict:
    """Return localized strings for the given language."""
    if lang == "en":
        return {
            "title": "Crip Center",
            "appearance": "Appearance",
            "theme_label": "Theme",
            "theme_crip_dark": "Crip Dark",
            "theme_crip_light": "Crip Light",
            "theme_minecraft": "Minecraft",
            "apply": "Apply",
            "language": "Language",
            "language_label": "Language",
            "language_uz": "O'zbekcha",
            "language_en": "English",
            "network": "Network",
            "network_status": "Status",
            "connected": "Connected",
            "offline": "Offline",
            "updates": "Updates",
            "auto_updates": "Automatic Updates",
            "check_updates": "Check for Updates",
            "security": "Security",
            "firewall": "Firewall",
            "secure_boot": "Secure Boot",
            "about": "About",
            "version": "Version",
            "codename": "Codename",
            "base": "Base",
            "ok": "OK",
        }
    return {
        "title": "Crip Center",
        "appearance": "Ko'rinish",
        "theme_label": "Mavzu",
        "theme_crip_dark": "Crip Dark",
        "theme_crip_light": "Crip Light",
        "theme_minecraft": "Minecraft",
        "apply": "Qo'llash",
        "language": "Til",
        "language_label": "Til",
        "language_uz": "O'zbekcha",
        "language_en": "English",
        "network": "Tarmoq",
        "network_status": "Holat",
        "connected": "Ulangan",
        "offline": "Uzilgan",
        "updates": "Yangilanishlar",
        "auto_updates": "Avtomatik yangilanishlar",
        "check_updates": "Yangilanishlarni tekshirish",
        "security": "Xavfsizlik",
        "firewall": "Xavfsizlik devori",
        "secure_boot": "Secure Boot",
        "about": "Tizim haqida",
        "version": "Versiya",
        "codename": "Kod nomi",
        "base": "Asos",
        "ok": "OK",
    }


class CenterWindow:
    """Main Crip Center window with sidebar navigation."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Crip Center")
        self.root.geometry("760x520")
        self.root.configure(bg=THEME["bg"])

        self.config = load_config()
        self.strings = get_language_strings(self.config.get("language", "uz"))

        self._build_navbar()
        self._build_content()
        self.show_section("Appearance")

    def _build_navbar(self) -> None:
        """Build the left sidebar navigation."""
        self.nav = tk.Frame(self.root, bg=THEME["surface"], width=180)
        self.nav.pack(side="left", fill="y")
        self.nav.pack_propagate(False)

        tk.Label(
            self.nav,
            text="Crip Center",
            fg=THEME["primary"],
            bg=THEME["surface"],
            font=("Segoe UI", 14, "bold"),
        ).pack(pady=(20, 16))

        for name, icon in SECTIONS:
            tk.Button(
                self.nav,
                text=f"{icon}  {self.strings.get(name.lower(), name)}",
                bg=THEME["surface"],
                fg=THEME["text"],
                activebackground=THEME["border"],
                activeforeground=THEME["text"],
                relief="flat",
                borderwidth=0,
                anchor="w",
                padx=16,
                pady=10,
                font=("Segoe UI", 10),
                command=lambda n=name: self.show_section(n),
            ).pack(fill="x", padx=8, pady=2)

    def _build_content(self) -> None:
        """Build the right content area."""
        self.content = tk.Frame(self.root, bg=THEME["bg"])
        self.content.pack(side="right", fill="both", expand=True)

    def _clear_content(self) -> None:
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_section(self, section: str) -> None:
        """Display the selected section."""
        self._clear_content()
        handler = {
            "Appearance": self._render_appearance,
            "Wallpaper": self._render_wallpaper,
            "Language": self._render_language,
            "Network": self._render_network,
            "Updates": self._render_updates,
            "Security": self._render_security,
            "About": self._render_about,
        }.get(section)
        if handler:
            handler()

    def _render_appearance(self) -> None:
        """Theme selection UI."""
        self._render_header(self.strings["appearance"], "theme")

        tk.Label(
            self.content,
            text=self.strings["theme_label"],
            fg=THEME["text"],
            bg=THEME["bg"],
            font=("Segoe UI", 10, "bold"),
        ).pack(anchor="w", padx=30, pady=(12, 4))

        self.theme_var = tk.StringVar(value=self.config.get("theme", "crip-dark"))
        theme_options = [
            ("crip-dark", self.strings["theme_crip_dark"]),
            ("crip-light", self.strings["theme_crip_light"]),
            ("minecraft", self.strings["theme_minecraft"]),
        ]
        for value, label in theme_options:
            tk.Radiobutton(
                self.content,
                text=label,
                variable=self.theme_var,
                value=value,
                bg=THEME["bg"],
                fg=THEME["text"],
                selectcolor=THEME["secondary"],
                activebackground=THEME["bg"],
                activeforeground=THEME["text"],
                font=("Segoe UI", 11),
                padx=10,
                pady=6,
            ).pack(anchor="w", padx=40)

        self._render_action_button(self.strings["apply"], self._apply_theme)

    def _apply_theme(self) -> None:
        from system.theme_manager import set_theme
        theme = self.theme_var.get()
        if set_theme(theme):
            self.config["theme"] = theme
            save_config(self.config)
            self._show_toast(f"{self.strings['theme_label']}: {theme}")
        else:
            self._show_toast("❌ Theme failed")

    def _render_wallpaper(self) -> None:
        """Wallpaper selection UI."""
        self._render_header(self.strings["appearance"], "wallpaper")

        from system.wallpaper_manager import get_current_wallpaper, list_wallpapers, set_wallpaper

        tk.Label(
            self.content,
            text="Wallpaper",
            fg=THEME["text"],
            bg=THEME["bg"],
            font=("Segoe UI", 10, "bold"),
        ).pack(anchor="w", padx=30, pady=(12, 4))

        self.wallpaper_var = tk.StringVar(value=get_current_wallpaper())
        for wp in list_wallpapers():
            tk.Radiobutton(
                self.content,
                text=wp,
                variable=self.wallpaper_var,
                value=wp,
                bg=THEME["bg"],
                fg=THEME["text"],
                selectcolor=THEME["secondary"],
                activebackground=THEME["bg"],
                activeforeground=THEME["text"],
                font=("Segoe UI", 11),
                padx=10,
                pady=6,
            ).pack(anchor="w", padx=40)

        self._render_action_button(self.strings["apply"], self._apply_wallpaper)

    def _apply_wallpaper(self) -> None:
        from system.wallpaper_manager import set_wallpaper
        wp = self.wallpaper_var.get()
        if set_wallpaper(wp):
            self._show_toast(f"Wallpaper: {wp}")
        else:
            self._show_toast("❌ Wallpaper failed")

    def _render_language(self) -> None:
        """Language selection UI."""
        self._render_header(self.strings["language"], "language")

        tk.Label(
            self.content,
            text=self.strings["language_label"],
            fg=THEME["text"],
            bg=THEME["bg"],
            font=("Segoe UI", 10, "bold"),
        ).pack(anchor="w", padx=30, pady=(12, 4))

        self.language_var = tk.StringVar(value=self.config.get("language", "uz"))
        language_options = [
            ("uz", self.strings["language_uz"]),
            ("en", self.strings["language_en"]),
        ]
        for value, label in language_options:
            tk.Radiobutton(
                self.content,
                text=label,
                variable=self.language_var,
                value=value,
                bg=THEME["bg"],
                fg=THEME["text"],
                selectcolor=THEME["secondary"],
                activebackground=THEME["bg"],
                activeforeground=THEME["text"],
                font=("Segoe UI", 11),
                padx=10,
                pady=6,
            ).pack(anchor="w", padx=40)

        self._render_action_button(self.strings["apply"], self._apply_language)

    def _apply_language(self) -> None:
        from system.language_manager import set_language
        lang = self.language_var.get()
        if set_language(lang):
            self.config["language"] = lang
            save_config(self.config)
            self.strings = get_language_strings(lang)
            self._show_toast(f"{self.strings['language_label']}: {lang}")
        else:
            self._show_toast("❌ Language failed")

    def _render_network(self) -> None:
        """Network status UI."""
        self._render_header(self.strings["network"], "network")

        status_text = self.strings["connected"] if self.config.get("internet", True) else self.strings["offline"]
        status_color = THEME["primary"] if self.config.get("internet", True) else THEME["danger"]

        tk.Label(
            self.content,
            text=f"{self.strings['network_status']}: {status_text}",
            fg=status_color,
            bg=THEME["bg"],
            font=("Segoe UI", 12),
        ).pack(anchor="w", padx=40, pady=20)

    def _render_updates(self) -> None:
        """Updates UI with auto-update toggle."""
        self._render_header(self.strings["updates"], "updates")

        self.auto_updates_var = tk.BooleanVar(value=self.config.get("auto_updates", True))
        tk.Checkbutton(
            self.content,
            text=self.strings["auto_updates"],
            variable=self.auto_updates_var,
            bg=THEME["bg"],
            fg=THEME["text"],
            selectcolor=THEME["secondary"],
            activebackground=THEME["bg"],
            activeforeground=THEME["text"],
            font=("Segoe UI", 11),
            padx=10,
            pady=6,
            command=self._toggle_auto_updates,
        ).pack(anchor="w", padx=40, pady=12)

        self._render_action_button(self.strings["check_updates"], self._check_updates)

    def _toggle_auto_updates(self) -> None:
        from system.updates.updates import load_update_config, save_update_config
        self.config["auto_updates"] = self.auto_updates_var.get()
        save_config(self.config)
        update_config = load_update_config()
        update_config["auto_install"] = self.auto_updates_var.get()
        save_update_config(update_config)

    def _check_updates(self) -> None:
        from system.updates.updates import check_updates
        status = check_updates()
        available = status.get("available", 0)
        self._show_toast(f"{self.strings['updates']}: {available}")

    def _render_security(self) -> None:
        """Security settings UI."""
        self._render_header(self.strings["security"], "security")

        self.firewall_var = tk.BooleanVar(value=self.config.get("firewall", True))
        tk.Checkbutton(
            self.content,
            text=self.strings["firewall"],
            variable=self.firewall_var,
            bg=THEME["bg"],
            fg=THEME["text"],
            selectcolor=THEME["secondary"],
            activebackground=THEME["bg"],
            activeforeground=THEME["text"],
            font=("Segoe UI", 11),
            padx=10,
            pady=6,
            command=self._toggle_firewall,
        ).pack(anchor="w", padx=40, pady=(12, 4))

        tk.Label(
            self.content,
            text=self.strings["secure_boot"] + ": ✅",
            fg=THEME["text"],
            bg=THEME["bg"],
            font=("Segoe UI", 11),
        ).pack(anchor="w", padx=50, pady=4)

    def _toggle_firewall(self) -> None:
        from system.security.security import load_security_config, save_security_config
        self.config["firewall"] = self.firewall_var.get()
        save_config(self.config)
        security = load_security_config()
        security["firewall"] = self.firewall_var.get()
        save_security_config(security)

    def _render_about(self) -> None:
        """About section with system info."""
        self._render_header(self.strings["about"], "info")

        from sdk.cripapi import system_info
        info = system_info()

        rows = [
            (self.strings["version"], info["version"]),
            (self.strings["codename"], info["codename"]),
            (self.strings["base"], info["base"]),
            ("Desktop", info["desktop"]),
            ("Kernel", info["kernel"]),
            ("Architecture", info["architecture"]),
        ]
        for label, value in rows:
            frame = tk.Frame(self.content, bg=THEME["bg"])
            frame.pack(fill="x", padx=40, pady=4)
            tk.Label(
                frame,
                text=f"{label}:",
                fg=THEME["muted"],
                bg=THEME["bg"],
                font=("Segoe UI", 11),
                width=16,
                anchor="w",
            ).pack(side="left")
            tk.Label(
                frame,
                text=value,
                fg=THEME["text"],
                bg=THEME["bg"],
                font=("Segoe UI", 11),
                anchor="w",
            ).pack(side="left")

    def _render_header(self, title: str, subtitle: str) -> None:
        """Render the section header."""
        tk.Label(
            self.content,
            text=title,
            fg=THEME["text"],
            bg=THEME["bg"],
            font=("Segoe UI", 18, "bold"),
        ).pack(anchor="w", padx=30, pady=(24, 4))
        tk.Label(
            self.content,
            text=subtitle,
            fg=THEME["muted"],
            bg=THEME["bg"],
            font=("Segoe UI", 10),
        ).pack(anchor="w", padx=30)

    def _render_action_button(self, text: str, command) -> None:
        """Render a primary action button."""
        tk.Button(
            self.content,
            text=text,
            bg=THEME["primary"],
            fg=THEME["bg"],
            activebackground=THEME["secondary"],
            activeforeground=THEME["text"],
            relief="flat",
            padx=20,
            pady=8,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
            command=command,
        ).pack(anchor="w", padx=40, pady=16)

    def _show_toast(self, message: str) -> None:
        """Show a temporary toast notification."""
        toast = tk.Label(
            self.content,
            text=message,
            fg=THEME["text"],
            bg=THEME["border"],
            font=("Segoe UI", 10),
            padx=16,
            pady=8,
        )
        toast.place(relx=0.5, rely=0.9, anchor="center")
        self.root.after(2000, toast.destroy)


def run_center() -> None:
    root = tk.Tk()
    CenterWindow(root)
    root.mainloop()


if __name__ == "__main__":
    run_center()