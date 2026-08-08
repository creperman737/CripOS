# 💚 CripOS

**Never Give Up.**

Modern Debian-based Operating System built with Python.

Vision: Create a fast, modern, and user-friendly Debian-based Linux distribution optimized for gaming, developers, and everyday users. Prioritize performance, stability, and simplicity while remaining open-source and community-driven.

## Quick Overview

- **Base:** Debian 13 (Trixie)
- **Desktop:** XFCE (Live ISO) / Cinnamon (Vision)
- **Codename:** Creeper
- **Status:** 🚧 Alpha Development

## 📊 Project Dashboard

```text
CripOS Roadmap

v0.1 Alpha (Creeper)    █████████░ 90%
v0.2 Alpha              ░░░░░░░░░ 0%
v0.3 Beta               ░░░░░░░░░ 0%
v1.0 Stable             ░░░░░░░░░ 0%
```

### 📈 Statistics

```text
Commits      430+
Tests        78/78 ✅
Themes       4
Wallpapers   6
CLI Commands 18
Desktop Apps 8
Base         Debian 13
Desktop      Cinnamon
Status       Alpha
```

### 🏆 Progress by Area

```text
Foundation        ██████████ 100%
Documentation    ██████████ 100%
Core Desktop    ██████████ 100%
Core System    ██████████ 100%
CLI            ██████████ 100%
Themes/UI      ██████████ 100%
Testing        ██████████ 100%
Installer      ██████████ 100%
ISO Build      █████████░ 80%
```

## Features

- ✅ Boot & Login System
- ✅ First-run Welcome Wizard
- ✅ Crip Launcher
- ✅ Crip Center (Settings Hub)
- ✅ Crip Terminal
- ✅ Crip Update
- ✅ Crip Installer
- ✅ Developer SDK (cripapi, cripui, cripwidgets, cripthemes)
- ✅ Crip Store
- ✅ Crip Files
- ✅ Crip Monitor
- 🚧 Gaming Mode (planned)

## Installation

```bash
# Run the installer (Linux)
sudo bash installer/install.sh

# Build ISO (Linux)
bash scripts/build-iso.sh
```

## Quick Start (Development)

```bash
# Run all tests
python tests/test_alpha_apps.py
python tests/test_system_modules.py
python tests/test_sdk.py
python apps/crip-welcome/test_ui.py
```

## Documentation

| Document | Description |
|---|---|
| [01-overview.md](docs/01-overview.md) | Project overview and features |
| [02-roadmap.md](docs/02-roadmap.md) | Version roadmap |
| [03-development-plan.md](docs/03-development-plan.md) | Sprint plan |
| [04-architecture.md](docs/04-architecture.md) | Architecture layers |
| [05-design-system.md](docs/05-design-system.md) | Colors, typography, UI |
| [06-applications.md](docs/06-applications.md) | All Crip apps |
| [07-sdk.md](docs/07-sdk.md) | Developer SDK guide |
| [08-api.md](docs/08-api.md) | Internal API reference |
| [09-system.md](docs/09-system.md) | System modules |
| [10-testing.md](docs/10-testing.md) | Testing guide |
| [11-release.md](docs/11-release.md) | Release plan |
| [12-future.md](docs/12-future.md) | Future roadmap |

## Repository Structure

```
CripOS/
│
├── apps/          # First-party applications
├── sdk/           # Developer SDK
├── api/           # Internal API layer
├── system/        # System modules
├── services/      # Background services
├── libs/          # Shared libraries
├── themes/        # GTK themes
├── locales/       # Language files
├── branding/      # Brand assets & splash text
└── docs/          # Documentation
```

## Tests

**78/78 automated tests passing** covering:

- Application APIs
- System modules
- SDK packages
- Welcome wizard
- CLI tools
- JSON validation
- Python syntax

## License & Contributing

- See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines
- See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community standards
- See [CHANGELOG.md](CHANGELOG.md) for version history

---

💚 **CripOS** — *Never Give Up.*