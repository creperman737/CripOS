#!/usr/bin/env python3
"""Crip Files - full file manager for CripOS."""

import os
import shutil
import sys
from pathlib import Path

import tkinter as tk
from tkinter import filedialog, messagebox, ttk

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


class CripFilesWindow:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Crip Files")
        self.root.geometry("800x520")
        self.root.configure(bg=THEME["bg"])

        self.current_dir = Path.home()

        self._build_toolbar()
        self._build_sidebar()
        self._build_file_list()
        self._build_statusbar()
        self.load_directory(self.current_dir)

    def _build_toolbar(self) -> None:
        toolbar = tk.Frame(self.root, bg=THEME["surface"])
        toolbar.pack(fill="x", padx=8, pady=(8, 4))

        tk.Button(
            toolbar,
            text="⬅",
            bg=THEME["surface"],
            fg=THEME["text"],
            relief="flat",
            padx=8,
            command=self.go_back,
        ).pack(side="left", padx=2)

        tk.Button(
            toolbar,
            text="⬆",
            bg=THEME["surface"],
            fg=THEME["text"],
            relief="flat",
            padx=8,
            command=self.go_up,
        ).pack(side="left", padx=2)

        tk.Button(
            toolbar,
            text="🔄",
            bg=THEME["surface"],
            fg=THEME["text"],
            relief="flat",
            padx=8,
            command=lambda: self.load_directory(self.current_dir),
        ).pack(side="left", padx=2)

        self.path_var = tk.StringVar()
        tk.Entry(
            toolbar,
            textvariable=self.path_var,
            bg=THEME["bg"],
            fg=THEME["text"],
            insertbackground=THEME["text"],
            relief="flat",
        ).pack(side="left", fill="x", expand=True, padx=8)

        tk.Button(
            toolbar,
            text="Go",
            bg=THEME["primary"],
            fg=THEME["bg"],
            relief="flat",
            padx=12,
            command=self.open_path,
        ).pack(side="left", padx=2)

        tk.Button(
            toolbar,
            text="📁 New Folder",
            bg=THEME["surface"],
            fg=THEME["text"],
            relief="flat",
            padx=8,
            command=self.new_folder,
        ).pack(side="left", padx=2)

        tk.Button(
            toolbar,
            text="🗑 Delete",
            bg=THEME["danger"],
            fg=THEME["text"],
            relief="flat",
            padx=8,
            command=self.delete_item,
        ).pack(side="left", padx=2)

    def _build_sidebar(self) -> None:
        sidebar = tk.Frame(self.root, bg=THEME["surface"], width=160)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        tk.Label(
            sidebar,
            text="Places",
            fg=THEME["muted"],
            bg=THEME["surface"],
            font=("Segoe UI", 10, "bold"),
        ).pack(anchor="w", padx=12, pady=(12, 4))

        places = [
            ("🏠 Home", Path.home()),
            ("📄 Documents", Path.home() / "Documents"),
            ("🖼 Pictures", Path.home() / "Pictures"),
            ("🎵 Music", Path.home() / "Music"),
            ("🎬 Videos", Path.home() / "Videos"),
            ("⬇ Downloads", Path.home() / "Downloads"),
        ]
        for label, path in places:
            tk.Button(
                sidebar,
                text=label,
                bg=THEME["surface"],
                fg=THEME["text"],
                activebackground=THEME["border"],
                activeforeground=THEME["text"],
                relief="flat",
                borderwidth=0,
                anchor="w",
                padx=12,
                pady=6,
                font=("Segoe UI", 10),
                command=lambda p=path: self.load_directory(p),
            ).pack(fill="x")

    def _build_file_list(self) -> None:
        frame = tk.Frame(self.root, bg=THEME["bg"])
        frame.pack(side="left", fill="both", expand=True, padx=(0, 8), pady=4)

        self.tree = ttk.Treeview(
            frame,
            columns=("type", "size"),
            show="tree headings",
            selectmode="browse",
        )
        self.tree.heading("#0", text="Name")
        self.tree.heading("type", text="Type")
        self.tree.heading("size", text="Size")
        self.tree.column("#0", width=320)
        self.tree.column("type", width=120)
        self.tree.column("size", width=100)

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
        self.tree.bind("<Double-1>", self.on_double_click)

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

    def load_directory(self, path: Path) -> None:
        """Load a directory into the file list."""
        try:
            path = Path(path)
            if not path.is_dir():
                return
            self.current_dir = path
            self.path_var.set(str(path))
            self.tree.delete(*self.tree.get_children())

            items = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
            for item in items:
                if item.is_dir():
                    self.tree.insert("", "end", text=f"📁 {item.name}", values=("Folder", ""))
                else:
                    size = item.stat().st_size
                    size_str = self._format_size(size)
                    self.tree.insert("", "end", text=f"📄 {item.name}", values=("File", size_str))

            count = len(items)
            self.status.config(text=f"{count} items • {path}")
        except PermissionError:
            self.status.config(text="Permission denied", fg=THEME["danger"])

    def open_path(self) -> None:
        path = Path(self.path_var.get())
        self.load_directory(path)

    def go_back(self) -> None:
        self.load_directory(self.current_dir.parent)

    def go_up(self) -> None:
        self.load_directory(self.current_dir.parent)

    def on_double_click(self, event) -> None:
        selection = self.tree.selection()
        if not selection:
            return
        item = self.tree.item(selection[0])
        name = item["text"].split(" ", 1)[1] if " " in item["text"] else item["text"]
        path = self.current_dir / name
        if path.is_dir():
            self.load_directory(path)

    def new_folder(self) -> None:
        name = "New Folder"
        path = self.current_dir / name
        counter = 1
        while path.exists():
            path = self.current_dir / f"New Folder ({counter})"
            counter += 1
        path.mkdir()
        self.load_directory(self.current_dir)

    def delete_item(self) -> None:
        selection = self.tree.selection()
        if not selection:
            return
        item = self.tree.item(selection[0])
        name = item["text"].split(" ", 1)[1] if " " in item["text"] else item["text"]
        path = self.current_dir / name

        if messagebox.askyesno("Delete", f"Delete '{name}'?"):
            try:
                if path.is_dir():
                    shutil.rmtree(path)
                else:
                    path.unlink()
                self.load_directory(self.current_dir)
            except OSError as e:
                messagebox.showerror("Error", str(e))

    @staticmethod
    def _format_size(size: int) -> str:
        for unit in ["B", "KB", "MB", "GB"]:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} TB"


def run_files() -> None:
    root = tk.Tk()
    CripFilesWindow(root)
    root.mainloop()


if __name__ == "__main__":
    run_files()