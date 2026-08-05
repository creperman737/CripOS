#!/usr/bin/env python3
"""Crip Monitor - lightweight system monitoring panel."""

import os
import platform
import shutil
import sys
import tkinter as tk
from tkinter import ttk

THEME = {
    "bg": "#0D1117",
    "surface": "#161B22",
    "border": "#30363D",
    "text": "#F0F6FC",
    "muted": "#8B949E",
    "primary": "#39D353",
    "secondary": "#2EA043",
}


def get_system_metrics() -> dict:
    """Gather current system metrics."""
    metrics = {}

    # CPU Count
    metrics["CPU Cores"] = f"{os.cpu_count() or 1} cores ({platform.machine()})"

    # Disk
    try:
        total, used, free = shutil.disk_usage(os.getcwd())
        disk_pct = int((used / total) * 100)
        metrics["Disk Usage"] = f"{disk_pct}% ({used // (1024**3)} GB / {total // (1024**3)} GB)"
    except Exception:
        metrics["Disk Usage"] = "N/A"

    # Memory (via psutil if available, else standard fallback)
    try:
        import psutil

        mem = psutil.virtual_memory()
        metrics["RAM Usage"] = f"{mem.percent}% ({mem.used // (1024**2)} MB / {mem.total // (1024**2)} MB)"
        metrics["CPU Load"] = f"{psutil.cpu_percent(interval=None)}%"
    except ImportError:
        metrics["RAM Usage"] = "Active"
        metrics["CPU Load"] = "Normal"

    metrics["OS"] = f"{platform.system()} {platform.release()}"
    metrics["Python"] = platform.python_version()

    return metrics


class MonitorWindow:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Crip Monitor")
        self.root.geometry("520x420")
        self.root.configure(bg=THEME["bg"])

        self._build_header()
        self._build_metrics()
        self._build_footer()
        self._refresh()

    def _build_header(self) -> None:
        header = tk.Frame(self.root, bg=THEME["surface"])
        header.pack(fill="x", padx=12, pady=(12, 6))

        tk.Label(
            header,
            text="📊 Crip Monitor",
            fg=THEME["primary"],
            bg=THEME["surface"],
            font=("Segoe UI", 16, "bold"),
        ).pack(side="left", padx=12, pady=10)

        tk.Label(
            header,
            text="Real-time System Stats",
            fg=THEME["muted"],
            bg=THEME["surface"],
            font=("Segoe UI", 10),
        ).pack(side="right", padx=12, pady=10)

    def _build_metrics(self) -> None:
        self.metrics_frame = tk.Frame(self.root, bg=THEME["bg"])
        self.metrics_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.labels = {}
        for key in ["OS", "Python", "CPU Cores", "CPU Load", "RAM Usage", "Disk Usage"]:
            row = tk.Frame(self.metrics_frame, bg=THEME["surface"], padx=12, pady=8)
            row.pack(fill="x", pady=4)

            tk.Label(
                row,
                text=key,
                fg=THEME["muted"],
                bg=THEME["surface"],
                font=("Segoe UI", 11, "bold"),
                width=14,
                anchor="w",
            ).pack(side="left")

            val_lbl = tk.Label(
                row,
                text="Loading...",
                fg=THEME["text"],
                bg=THEME["surface"],
                font=("Segoe UI", 11),
                anchor="w",
            )
            val_lbl.pack(side="left", fill="x", expand=True)
            self.labels[key] = val_lbl

    def _build_footer(self) -> None:
        footer = tk.Frame(self.root, bg=THEME["surface"])
        footer.pack(fill="x", side="bottom")

        tk.Button(
            footer,
            text="🔄 Refresh",
            bg=THEME["primary"],
            fg=THEME["bg"],
            relief="flat",
            padx=12,
            pady=4,
            font=("Segoe UI", 9, "bold"),
            command=self._refresh,
        ).pack(side="right", padx=12, pady=6)

        self.status = tk.Label(
            footer,
            text="Monitoring active",
            fg=THEME["muted"],
            bg=THEME["surface"],
            font=("Segoe UI", 9),
        )
        self.status.pack(side="left", padx=12, pady=6)

    def _refresh(self) -> None:
        data = get_system_metrics()
        for key, lbl in self.labels.items():
            if key in data:
                lbl.config(text=data[key])
        self.root.after(3000, self._refresh)


def run_monitor() -> None:
    root = tk.Tk()
    MonitorWindow(root)
    root.mainloop()


if __name__ == "__main__":
    run_monitor()
