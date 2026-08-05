# Changelog

## [0.1-alpha] - 2026-08-05

### Added
- **Crip CLI** — unified command-line tool with 18 commands
  - `crip install/remove/search/packages/upgrade/clean` — package management
  - `crip theme/wallpaper/language` — system customization
  - `crip about/doctor/info/version/update` — system info
  - `crip center/welcome/store/files` — app launchers
- **Crip Center** — full settings app wired to real system managers
  - Appearance (themes), Wallpaper, Language, Network, Updates, Security, About
- **Crip Files** — full file manager
  - Browse, Open, Copy, Move, Rename, Delete, New Folder
- **Crip Launcher** — start-menu with search, favorites, recent, categories
- **Crip Store** — app store wired to real package manager (install/remove)
- **Crip Update** — update manager wired to system updates (check/install)
- **Language Manager** — `system/language_manager.py` (en/uz)
- **Wallpaper Manager** — `system/wallpaper_manager.py` with validation
- **Package Manager** — `upgrade_packages()` and `clean_packages()`
- **ISO Builder** — plymouth theme, GRUB branding, os-release, SHA256 checksum

### Fixed
- Wallpaper validation — invalid wallpapers now rejected
- Crip Center settings now persist to real system managers

### Tests
- 69 tests passing (unit, CLI, system modules, SDK, splash)

## [Unreleased]
- Repository structure and documentation initialized
- Added docs for roadmap, features, and branding
- Created assets, installer, packages, scripts, themes, wallpapers folders