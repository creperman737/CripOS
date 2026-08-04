#!/usr/bin/env python3
"""Tkinter first-run experience for CripOS Alpha 0.1."""

from __future__ import annotations

import re
import threading
from pathlib import Path
from typing import Any, Callable
import tkinter as tk

from config import load_config, save_config
from internet import InternetStatus, check_internet
from language import load_language, normalize_language


STEP_INTRO = 0
STEP_LANGUAGE = 1
STEP_INTERNET = 2
STEP_UPDATES = 3
STEP_COMPLETE = 4
STEP_COUNT = 5

DEFAULT_STRINGS = {
    "title": "Welcome to CripOS",
    "start": "Start",
    "continue": "Continue",
    "finish": "Finish",
    "internet": "Checking Internet...",
    "updates": "Checking Updates...",
    "done": "Ready!",
    "intro_subtitle": "CripOS 0.1 Alpha · First run",
    "tagline": "Never Give Up.",
    "language_title": "Choose your language",
    "language_message": "You can change this later in Crip Center.",
    "language_uz": "O'zbekcha",
    "language_en": "English",
    "internet_title": "Internet connection",
    "internet_connected": "Connected",
    "internet_offline": "No connection found. You can continue setup and connect later.",
    "updates_title": "Updates",
    "updates_message": "CripOS Alpha 0.1",
    "updates_hint": "Use Crip Update to manage system updates after setup.",
    "complete_title": "Setup complete",
    "complete_message": "Start exploring CripOS from Crip Launcher.",
    "back": "Back",
    "step": "Step {current} of {total}",
}


def get_strings(lang_code: str) -> dict[str, str]:
    """Return a complete set of display strings with safe defaults."""
    strings = DEFAULT_STRINGS.copy()
    strings.update(load_language(lang_code))
    return strings


def load_theme(style_path: Path) -> dict[str, str]:
    """Read the color tokens shared by Crip Welcome's stylesheet."""
    defaults = {
        "primary-green": "#39D353",
        "secondary-green": "#2EA043",
        "background-dark": "#0D1117",
        "surface-dark": "#161B22",
        "border": "#30363D",
        "text": "#F0F6FC",
        "muted": "#8B949E",
        "danger": "#F85149",
    }
    if not style_path.exists():
        return defaults

    css = style_path.read_text(encoding="utf-8")
    for name in defaults:
        match = re.search(rf"--{name}\s*:\s*([^;]+);", css)
        if match:
            defaults[name] = match.group(1).strip()
    return defaults


class WelcomeFlow:
    """UI-independent state machine for the five welcome screens."""

    def __init__(
        self,
        config: dict[str, Any],
        save_callback: Callable[[dict[str, Any]], Any] = save_config,
    ) -> None:
        self.config = dict(config)
        self.save_callback = save_callback
        self.language = normalize_language(self.config.get("language"))
        self.step = STEP_INTRO

    def select_language(self, language: str) -> None:
        self.language = normalize_language(language)

    def go_back(self) -> None:
        self.step = max(STEP_INTRO, self.step - 1)

    def advance(self) -> bool:
        """Advance one screen; return ``True`` when the user finishes setup."""
        if self.step == STEP_LANGUAGE:
            self.config["language"] = self.language
            self.save_callback(dict(self.config))

        if self.step == STEP_COMPLETE:
            self.config["language"] = self.language
            self.config["completed"] = True
            self.save_callback(dict(self.config))
            return True

        self.step += 1
        return False


class WelcomeWindow:
    """The Crip Welcome desktop window."""

    def __init__(
        self,
        root: tk.Tk,
        config: dict[str, Any] | None = None,
        internet_checker: Callable[[], InternetStatus] = check_internet,
    ) -> None:
        self.root = root
        self.root.title("Crip Welcome")
        self.root.geometry("760x500")
        self.root.resizable(False, False)

        self.base_dir = Path(__file__).resolve().parent
        self.theme = load_theme(self.base_dir / "style.css")
        self.root.configure(bg=self.theme["background-dark"])

        self.flow = WelcomeFlow(config if config is not None else load_config())
        self.language_var = tk.StringVar(value=self.flow.language)
        self.strings = get_strings(self.flow.language)
        self.internet_checker = internet_checker
        self._network_request = 0
        self._network_status: InternetStatus | None = None

        self._build_ui()
        self.render_step()

    def _load_image(self, filename: str) -> tk.PhotoImage | None:
        try:
            return tk.PhotoImage(file=str(self.base_dir / "assets" / filename))
        except tk.TclError:
            return None

    def _build_ui(self) -> None:
        self.background_image = self._load_image("background.png")
        if self.background_image is not None:
            tk.Label(
                self.root,
                image=self.background_image,
                bg=self.theme["background-dark"],
                borderwidth=0,
            ).place(x=0, y=0, relwidth=1, relheight=1)

        self.card = tk.Frame(
            self.root,
            bg=self.theme["surface-dark"],
            padx=26,
            pady=22,
            highlightbackground=self.theme["border"],
            highlightthickness=1,
        )
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=660, height=390)

        header = tk.Frame(self.card, bg=self.theme["surface-dark"])
        header.pack(fill="x")

        self.logo_image = self._load_image("logo.png")
        if self.logo_image is not None:
            self.logo_image = self.logo_image.subsample(2, 2)
            tk.Label(header, image=self.logo_image, bg=self.theme["surface-dark"]).pack(
                side="left", padx=(0, 12)
            )

        heading = tk.Frame(header, bg=self.theme["surface-dark"])
        heading.pack(side="left", fill="x", expand=True)
        self.title_label = tk.Label(
            heading,
            text="",
            fg=self.theme["text"],
            bg=self.theme["surface-dark"],
            font=("Segoe UI", 22, "bold"),
            anchor="w",
        )
        self.title_label.pack(fill="x")
        self.subtitle_label = tk.Label(
            heading,
            text="",
            fg=self.theme["primary-green"],
            bg=self.theme["surface-dark"],
            font=("Segoe UI", 10),
            anchor="w",
        )
        self.subtitle_label.pack(fill="x", pady=(2, 0))

        self.step_label = tk.Label(
            header,
            text="",
            fg=self.theme["muted"],
            bg=self.theme["surface-dark"],
            font=("Segoe UI", 9),
            anchor="e",
        )
        self.step_label.pack(side="right", anchor="n")

        self.message_label = tk.Label(
            self.card,
            text="",
            fg=self.theme["text"],
            bg=self.theme["surface-dark"],
            font=("Segoe UI", 12),
            justify="left",
            anchor="w",
            wraplength=600,
        )
        self.message_label.pack(fill="x", pady=(18, 8))

        self.content_frame = tk.Frame(self.card, bg=self.theme["surface-dark"])
        self.content_frame.pack(fill="both", expand=True)

        actions = tk.Frame(self.card, bg=self.theme["surface-dark"])
        actions.pack(fill="x", pady=(12, 0))
        self.back_button = tk.Button(
            actions,
            command=self.go_back,
            bg=self.theme["surface-dark"],
            fg=self.theme["muted"],
            activebackground=self.theme["surface-dark"],
            activeforeground=self.theme["text"],
            relief="flat",
            borderwidth=0,
            padx=8,
            pady=8,
            font=("Segoe UI", 10),
            cursor="hand2",
        )
        self.next_button = tk.Button(
            actions,
            command=self.next_step,
            bg=self.theme["primary-green"],
            fg=self.theme["background-dark"],
            activebackground=self.theme["secondary-green"],
            activeforeground=self.theme["text"],
            relief="flat",
            borderwidth=0,
            padx=18,
            pady=9,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
        )
        self.next_button.pack(side="right")
        self.root.bind("<Return>", lambda _event: self.next_step())

    def _clear_content(self) -> None:
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def _set_header(self, title: str, subtitle: str) -> None:
        self.title_label.config(text=title)
        self.subtitle_label.config(text=subtitle)
        self.step_label.config(
            text=self.strings["step"].format(current=self.flow.step + 1, total=STEP_COUNT)
        )

    def _show_back_button(self) -> None:
        if self.flow.step == STEP_INTRO:
            self.back_button.pack_forget()
        else:
            self.back_button.config(text=self.strings["back"])
            self.back_button.pack(side="left")

    def render_step(self) -> None:
        self._clear_content()
        self.strings = get_strings(self.flow.language)
        self._show_back_button()

        if self.flow.step == STEP_INTRO:
            self._render_intro()
        elif self.flow.step == STEP_LANGUAGE:
            self._render_language()
        elif self.flow.step == STEP_INTERNET:
            self._render_internet()
        elif self.flow.step == STEP_UPDATES:
            self._render_updates()
        else:
            self._render_complete()

    def _render_intro(self) -> None:
        self._set_header("CripOS", self.strings["intro_subtitle"])
        self.message_label.config(text=f"{self.strings['title']}\n\n{self.strings['tagline']}")
        self.next_button.config(text=self.strings["start"])

    def _render_language(self) -> None:
        self._set_header("Crip Welcome", self.strings["language_title"])
        self.message_label.config(text=self.strings["language_message"])
        self.language_var.set(self.flow.language)

        for code, key in (("uz", "language_uz"), ("en", "language_en")):
            tk.Radiobutton(
                self.content_frame,
                text=self.strings[key],
                variable=self.language_var,
                value=code,
                command=self._select_language,
                indicatoron=0,
                selectcolor=self.theme["secondary-green"],
                bg=self.theme["background-dark"],
                fg=self.theme["text"],
                activebackground=self.theme["secondary-green"],
                activeforeground=self.theme["text"],
                relief="flat",
                padx=16,
                pady=10,
                anchor="w",
                font=("Segoe UI", 11),
            ).pack(fill="x", pady=4)
        self.next_button.config(text=self.strings["continue"])

    def _render_internet(self) -> None:
        self._set_header("Crip Welcome", self.strings["internet_title"])
        self.message_label.config(text=self.strings["internet"])
        self.next_button.config(text=self.strings["continue"])
        self._network_request += 1
        request_id = self._network_request

        self.status_label = tk.Label(
            self.content_frame,
            text="…",
            fg=self.theme["muted"],
            bg=self.theme["surface-dark"],
            font=("Segoe UI", 11),
            anchor="w",
        )
        self.status_label.pack(anchor="w", pady=(8, 0))
        threading.Thread(
            target=self._check_internet_in_background,
            args=(request_id,),
            daemon=True,
        ).start()

    def _check_internet_in_background(self, request_id: int) -> None:
        try:
            status = self.internet_checker()
        except Exception:
            status = InternetStatus(False, "Offline")
        try:
            self.root.after(0, self._show_internet_status, request_id, status)
        except tk.TclError:
            pass

    def _show_internet_status(self, request_id: int, status: InternetStatus) -> None:
        if request_id != self._network_request or self.flow.step != STEP_INTERNET:
            return
        self._network_status = status
        self.flow.config["internet"] = status.connected
        text_key = "internet_connected" if status.connected else "internet_offline"
        color = self.theme["primary-green"] if status.connected else self.theme["danger"]
        self.status_label.config(text=self.strings[text_key], fg=color)

    def _render_updates(self) -> None:
        self._set_header("Crip Welcome", self.strings["updates_title"])
        self.message_label.config(text=self.strings["updates"])
        tk.Label(
            self.content_frame,
            text=self.strings["updates_message"],
            fg=self.theme["primary-green"],
            bg=self.theme["surface-dark"],
            font=("Segoe UI", 12, "bold"),
            anchor="w",
        ).pack(anchor="w", pady=(8, 2))
        tk.Label(
            self.content_frame,
            text=self.strings["updates_hint"],
            fg=self.theme["muted"],
            bg=self.theme["surface-dark"],
            font=("Segoe UI", 10),
            justify="left",
            wraplength=580,
            anchor="w",
        ).pack(anchor="w")
        self.next_button.config(text=self.strings["continue"])

    def _render_complete(self) -> None:
        self._set_header("CripOS", self.strings["complete_title"])
        self.message_label.config(text=f"{self.strings['done']}\n\n{self.strings['complete_message']}")
        self.next_button.config(text=self.strings["finish"])

    def _select_language(self) -> None:
        self.flow.select_language(self.language_var.get())
        self.render_step()

    def go_back(self) -> None:
        self.flow.go_back()
        self.render_step()

    def next_step(self) -> None:
        if self.flow.advance():
            self.root.destroy()
            return
        self.render_step()


def run_welcome(force: bool = False) -> bool:
    """Run the welcome app, unless first-run setup is already complete."""
    config = load_config()
    if config.get("completed") and not force:
        return False

    root = tk.Tk()
    WelcomeWindow(root, config=config)
    root.mainloop()
    return True
