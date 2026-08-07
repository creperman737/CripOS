#!/usr/bin/env python3
"""Unified CLI for CripOS: `crip <subcommand>`."""

import sys
import importlib.util
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from sdk.cripapi import get_version

COMMANDS = {
    "about": "Show CripOS branding and about info",
    "doctor": "Diagnose system health and structure",
    "update": "Check for system updates",
    "center": "Open Crip Center settings",
    "welcome": "Run Crip Welcome wizard",
    "store": "Open Crip Store",
    "files": "Open Crip Files manager",
    "version": "Display CripOS version",
    "info": "Display system information",
    "install": "Install a package (crip install <name>)",
    "remove": "Remove a package (crip remove <name>)",
    "search": "Search for packages (crip search <query>)",
    "packages": "List installed packages",
    "upgrade": "Upgrade all packages",
    "clean": "Clean package cache",
    "theme": "Switch theme (crip theme <name>)",
    "wallpaper": "Set wallpaper (crip wallpaper <name>)",
    "language": "Set language (crip language <code>)",
    "terminal": "Open Crip Terminal",
    "monitor": "Open Crip Monitor",
    "installer": "Open Crip Installer",
    "launcher": "Open Crip Launcher",
}


def _load_and_run(tool_name: str, func_name: str = "main", *args) -> None:
    path = REPO_ROOT / "tools" / f"{tool_name}.py"
    if not path.exists():
        print(f"Tool {tool_name} not found.")
        return
    spec = importlib.util.spec_from_file_location(tool_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    fn = getattr(module, func_name, None)
    if callable(fn):
        fn(*args)


def _list_args(manager_name: str, title: str, current_key: str, available_key: str) -> None:
    """List available items from a system manager with a marker on the current one."""
    module = importlib.import_module(manager_name)
    current = getattr(module, current_key)()
    items = getattr(module, available_key)()
    print(f"💚 CripOS {title}")
    print("=" * 35)
    if isinstance(items, dict):
        print(f"  Current : {current}")
        print("  Available:")
        for key, label in items.items():
            marker = "●" if key == current else "○"
            print(f"    {marker} {key} - {label}")
    else:
        print(f"  Current : {current}")
        print("  Available:")
        for item in items:
            marker = "●" if item == current else "○"
            print(f"    {marker} {item}")


def _cmd_install(args: list[str]) -> None:
    if not args:
        print("Usage: crip install <package-name>")
        return
    from system.package_manager import install_package
    name = args[0]
    if install_package(name):
        print(f"✅ Installed: {name}")
    else:
        print(f"❌ Failed to install: {name}")


def _cmd_remove(args: list[str]) -> None:
    if not args:
        print("Usage: crip remove <package-name>")
        return
    from system.package_manager import remove_package
    name = args[0]
    if remove_package(name):
        print(f"✅ Removed: {name}")
    else:
        print(f"❌ Failed to remove: {name}")


def _cmd_search(args: list[str]) -> None:
    if not args:
        print("Usage: crip search <query>")
        return
    from system.package_manager import search_packages
    query = args[0]
    results = search_packages(query)
    print(f"💚 Search results for '{query}':")
    print("=" * 35)
    if results:
        for pkg in results:
            print(f"  {pkg}")
    else:
        print("  No packages found.")
    print(f"  ({len(results)} results)")


def _cmd_packages(args: list[str]) -> None:
    from system.package_manager import list_installed
    installed = list_installed()
    print("💚 CripOS Installed Packages")
    print("=" * 35)
    if installed:
        for pkg in installed:
            print(f"  • {pkg}")
    else:
        print("  No packages recorded yet.")
    print(f"  ({len(installed)} packages)")


def _cmd_upgrade(args: list[str]) -> None:
    from system.package_manager import upgrade_packages
    print("💚 Upgrading packages...")
    if upgrade_packages():
        print("✅ Packages upgraded.")
    else:
        print("⚠️ Upgrade failed or apt unavailable. Use 'crip update' to refresh lists.")


def _cmd_clean(args: list[str]) -> None:
    from system.package_manager import clean_packages
    print("💚 Cleaning package cache...")
    if clean_packages():
        print("✅ Package cache cleaned.")
    else:
        print("⚠️ Package cache cleanup failed or apt unavailable.")


def _cmd_theme(args: list[str]) -> None:
    from system.theme_manager import get_current_theme, list_themes, set_theme
    if not args or args[0] in ("-h", "--help", "list"):
        _list_args("system.theme_manager", "Theme Manager", "get_current_theme", "list_themes")
        return
    name = args[0]
    if set_theme(name):
        print(f"✅ Theme set to: {name}")
    else:
        print(f"❌ Unknown theme: {name}")
        print(f"   Available: {', '.join(list_themes())}")


def _cmd_wallpaper(args: list[str]) -> None:
    from system.wallpaper_manager import (
        get_current_wallpaper,
        get_random_wallpaper,
        list_wallpapers,
        set_wallpaper,
    )
    if not args or args[0] in ("-h", "--help", "list"):
        _list_args("system.wallpaper_manager", "Wallpaper Manager", "get_current_wallpaper", "list_wallpapers")
        return
    name = args[0]
    if name == "random":
        name = get_random_wallpaper()
        print(f"🎲 Random wallpaper: {name}")
    if set_wallpaper(name):
        print(f"✅ Wallpaper set to: {name}")
    else:
        print(f"❌ Unknown wallpaper: {name}")
        print(f"   Available: {', '.join(list_wallpapers())}")


def _cmd_language(args: list[str]) -> None:
    from system.language_manager import get_current_language, list_languages, set_language
    if not args or args[0] in ("-h", "--help", "list"):
        _list_args("system.language_manager", "Language Manager", "get_current_language", "list_languages")
        return
    lang = args[0]
    if set_language(lang):
        print(f"✅ Language set to: {lang}")
    else:
        print(f"❌ Unknown language: {lang}")
        print(f"   Available: {', '.join(list_languages())}")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    if len(sys.argv) < 2 or sys.argv[1] in ["-h", "--help", "help"]:
        print("💚 CripOS CLI Control Tool")
        print("=" * 35)
        print("Usage: crip <command> [options]\n")
        print("Commands:")
        for cmd, desc in COMMANDS.items():
            print(f"  {cmd:<12} : {desc}")
        print("=" * 35)
        return

    cmd = sys.argv[1].lower()
    args = sys.argv[2:]

    if cmd == "version":
        print(get_version())
    elif cmd == "about":
        _load_and_run("crip-about")
    elif cmd == "doctor":
        _load_and_run("crip-doctor", "run_doctor")
    elif cmd == "info":
        _load_and_run("crip-info")
    elif cmd == "update":
        _load_and_run("crip-update")
    elif cmd == "welcome":
        _load_and_run("crip-welcome")
    elif cmd == "store":
        _load_and_run("crip-store")
    elif cmd == "center":
        _load_and_run("crip-center")
    elif cmd == "install":
        _cmd_install(args)
    elif cmd == "remove":
        _cmd_remove(args)
    elif cmd == "search":
        _cmd_search(args)
    elif cmd == "packages":
        _cmd_packages(args)
    elif cmd == "upgrade":
        _cmd_upgrade(args)
    elif cmd == "clean":
        _cmd_clean(args)
    elif cmd == "theme":
        _cmd_theme(args)
    elif cmd == "wallpaper":
        _cmd_wallpaper(args)
    elif cmd == "language":
        _cmd_language(args)
    elif cmd == "files":
        path = REPO_ROOT / "apps" / "crip-files" / "main.py"
        spec = importlib.util.spec_from_file_location("crip_files_main", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.run_files()
    elif cmd == "terminal":
        path = REPO_ROOT / "apps" / "crip-terminal" / "main.py"
        spec = importlib.util.spec_from_file_location("crip_terminal_main", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.run_terminal()
    elif cmd == "monitor":
        path = REPO_ROOT / "apps" / "crip-monitor" / "main.py"
        spec = importlib.util.spec_from_file_location("crip_monitor_main", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.run_monitor()
    elif cmd == "installer":
        path = REPO_ROOT / "apps" / "crip-installer" / "main.py"
        spec = importlib.util.spec_from_file_location("crip_installer_main", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.run_installer()
    elif cmd == "launcher":
        path = REPO_ROOT / "apps" / "crip-launcher" / "launcher.py"
        spec = importlib.util.spec_from_file_location("crip_launcher_main", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.launch_launcher()
    else:
        print(f"Unknown command: '{cmd}'")
        print("Run 'crip help' to see available commands.")


if __name__ == "__main__":
    main()
