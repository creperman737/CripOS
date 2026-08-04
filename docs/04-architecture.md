# CripOS Architecture

## Overview

CripOS uses a modular, layered architecture built around Python. Each layer has a clear responsibility, making the system testable, extensible, and maintainable.

## Layer Structure

```
┌─────────────────────────────────────┐
│         Applications (apps/)        │
│  Welcome│Launcher│Center│Store│...  │
├─────────────────────────────────────┤
│         SDK (sdk/)                  │
│  cripapi│cripui│cripwidgets│themes  │
├─────────────────────────────────────┤
│         API (api/)                  │
│  settings│store│system│updates│users│
├─────────────────────────────────────┤
│         System (system/)            │
│  boot│login│desktop│security│...    │
├─────────────────────────────────────┤
│         Services (services/)        │
│  network│notify│power│update│...    │
├─────────────────────────────────────┤
│         Libraries (libs/)           │
│  cripcore│language│network│security │
└─────────────────────────────────────┘
```

## Directory Details

### `apps/` — Applications
First-party GUI and CLI applications, each in its own directory:
- `crip-welcome/` — First-run setup wizard
- `crip-launcher/` — Start menu / app launcher
- `crip-center/` — Settings center (Appearance, Language, Network, Updates, Security, About)
- `crip-store/` — Application store
- `crip-files/` — File manager
- `crip-terminal/` — Terminal emulator
- `crip-update/` — System updates
- `crip-monitor/` — System monitor
- `crip-installer/` — System installer

### `sdk/` — Software Development Kit
Public API for third-party developers:
- `cripapi/` — System API functions (system_info, get_apps, get_version)
- `cripui/` — UI component builders (button, label, input, checkbox, dropdown, progress_bar)
- `cripwidgets/` — Composite widgets (card, window, dialog, toast, sidebar, toolbar)
- `cripthemes/` — Theme definitions (dark, light, minecraft)

### `api/` — Internal API Layer
Shared backend logic used by applications:
- `settings.py` — Settings sections
- `store.py` — Store categories
- `system.py` — System information
- `system_api.py` — System API with CripCore integration
- `updates.py` — Update status
- `users.py` — User management
- `launcher.py` — Launcher items

### `system/` — System Modules
Low-level OS components:
- `boot/` — Boot sequence, disk/memory checks, service startup
- `login/` — User authentication, password hashing
- `desktop/` — Desktop entry generation, environment startup
- `recovery/` — Recovery mode, package repair
- `security/` — Firewall, secure boot, security checks
- `services/` — Service management (systemctl wrapper)
- `startup/` — Startup applications configuration
- `updates/` — APT-based update management

### `services/` — Background Services
systemd service units:
- `crip-network.service`
- `crip-notify.service`
- `crip-power.service`
- `crip-update.service`
- `crip-wallpaper.service`
- `crip-ai.service`

### `libs/` — Shared Libraries
Core utilities shared across all components:
- `cripcore.py` — CripCore base class (JSON read/write)
- `language/` — Language support (planned)
- `network/` — Network utilities (planned)
- `notifications/` — Notification helpers (planned)
- `security/` — Security utilities (planned)
- `settings/` — Settings helpers (planned)
- `ui/` — UI helpers (planned)
- `updates/` — Update helpers (planned)
- `utils/` — General utilities (planned)

## Data Flow

### Application Startup
```
boot system → login manager → desktop env → startup apps
```

### Settings Persistence
```
app → api/settings.py → ~/.config/cripos/*.json
```

### System Updates
```
Crip Update → api/updates.py → system/updates/ → apt-get
```

### Security
```
Crip Center → api/system.py → system/security/ → ufw
```

## Configuration

### System-wide configs (`/etc/cripos/`)
- `config.json` — Welcome configuration
- `security.json` — Security settings
- `updates.json` — Update settings
- `users.json` — User database

### User configs (`~/.config/cripos/`)
- `center.json` — Crip Center settings
- `startup.json` — Startup apps
- `welcome.json` — Welcome completion state