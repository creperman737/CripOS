# CripOS Applications

## Application Overview

All CripOS first-party applications use the **Crip** prefix and live in `apps/`.

---

## Crip Welcome

**Purpose:** First-run setup wizard for new CripOS installations.

| Attribute | Value |
|---|---|
| Directory | `apps/crip-welcome/` |
| Entry Point | `main.py` |
| Type | GUI (Tkinter) |
| Status | ✅ Complete |

**Features:**
- 5-step setup wizard (Intro → Language → Internet → Updates → Complete)
- Language selection (O'zbek / English)
- Internet connectivity check
- Config persistence to `~/.config/cripos/welcome.json`
- Full test suite (9 tests)

---

## Crip Launcher

**Purpose:** Start-menu-like application launcher.

| Attribute | Value |
|---|---|
| Directory | `apps/crip-launcher/` |
| Entry Point | `main.py` |
| Type | GUI (Tkinter) |
| Status | ✅ Complete |

**Features:**
- Core apps list (Files, Browser, Terminal, Settings, Store, Updates, Games)
- Search functionality (`search.py`)
- Power menu (`power.py`)
- Localization support (`locale_helper.py`)
- Theme stylesheet (`style.css`)

---

## Crip Center

**Purpose:** Central settings hub for the entire OS.

| Attribute | Value |
|---|---|
| Directory | `apps/crip-center/` |
| Entry Point | `main.py` |
| Type | GUI (Tkinter) |
| Status | ✅ Complete |

**Sections:**
- 🖌️ **Appearance** — theme selection (Crip Dark, Crip Light, Minecraft)
- 🌍 **Language** — O'zbek / English switch
- 🌐 **Network** — connection status
- 🔄 **Updates** — auto-update toggle, update check
- 🔒 **Security** — firewall toggle, secure boot status
- ℹ️ **About** — system information

**Features:**
- Sidebar navigation with emoji icons
- Toast notifications
- Config saved to `~/.config/cripos/center.json`
- Full bilingual UI

---

## Crip Store

**Purpose:** Application store with categories.

| Attribute | Value |
|---|---|
| Directory | `apps/crip-store/` |
| Entry Point | `main.py` |
| Type | GUI (Tkinter) |
| Status | 🚧 In Development |

**Features:**
- Category browsing (Featured, New Apps, Games, Development, Office, Internet, Multimedia, Utilities, Installed, Updates)
- App database (`database.json`)
- Search (`search.py`)
- Install/Remove scaffold (`install.py`, `remove.py`)

---

## Crip Files

**Purpose:** File manager for CripOS.

| Attribute | Value |
|---|---|
| Directory | `apps/crip-files/` |
| Entry Point | `main.py` |
| Type | GUI (Tkinter) |
| Status | 🚧 In Development |

**Features:**
- Directory tree view
- File/folder size and type display
- Path navigation
- Sidebar (`sidebar.py`), toolbar (`toolbar.py`), search (`search.py`), trash (`trash.py`), properties (`properties.py`)

---

## Crip Terminal

**Purpose:** Simple terminal emulator.

| Attribute | Value |
|---|---|
| Directory | `apps/crip-terminal/` |
| Entry Point | `main.py` |
| Type | GUI (Tkinter) |
| Status | ✅ Complete |

**Features:**
- Dark-themed text area
- Resizable window

---

## Crip Monitor

**Purpose:** Lightweight system monitoring dashboard.

| Attribute | Value |
|---|---|
| Directory | `apps/crip-monitor/` |
| Entry Point | `main.py` |
| Type | GUI (Tkinter) |
| Status | ✅ Complete |

**Features:**
- CPU, RAM, GPU, Disk, Network, Processes, Temperature metrics

---

## Crip Update

**Purpose:** System update manager.

| Attribute | Value |
|---|---|
| Directory | `apps/crip-update/` |
| Entry Point | `main.py` |
| Type | GUI (Tkinter) |
| Status | ✅ Complete |

**Features:**
- Check for updates button
- Install updates button
- Update status via `api/updates.py`
- Package list display

---

## Crip Installer

**Purpose:** System installer for CripOS.

| Attribute | Value |
|---|---|
| Directory | `apps/crip-installer/` |
| Entry Point | `main.py` |
| Type | GUI (Tkinter) |
| Status | ✅ Complete |

**Features:**
- Full / Minimal / Custom installation options
- Progress bar with installation steps
- Cancel button