#!/usr/bin/env python3
"""Crip Terminal - simple terminal app shell."""

import tkinter as tk


class TerminalWindow:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Crip Terminal")
        self.root.geometry("640x360")
        self.root.configure(bg="#0D1117")

        tk.Label(
            root,
            text="Crip Terminal",
            fg="#F0F6FC",
            bg="#0D1117",
            font=("Segoe UI", 16, "bold"),
        ).pack(pady=(20, 10))

        tk.Text(root, bg="#161B22", fg="#F0F6FC", padx=12, pady=12).pack(fill="both", expand=True, padx=20, pady=(0, 20))


def run_terminal() -> None:
    root = tk.Tk()
    TerminalWindow(root)
    root.mainloop()


if __name__ == "__main__":
    run_terminal()
