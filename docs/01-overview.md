# CripOS Overview

## What is CripOS?

CripOS is a modern Debian-based operating system built with Python and modular components. It is designed for gaming, development, and everyday use with a unique Minecraft-inspired identity.

## Core Identity

- **Codename:** Creeper
- **Tagline:** Never Give Up.
- **Base:** Debian 13 (Trixie)
- **Desktop:** Cinnamon
- **Kernel:** Linux
- **Architecture:** x86_64

## Key Features

- Gaming Ready (Steam, Proton, Wine)
- Development Environment (Git, GCC, Python, VS Code)
- Office Suite and Everyday Tools
- Built-in AI Assistant (planned)
- Cloud Integration (OneDrive, Google Drive, Dropbox)
- Security (Firewall, Automatic Updates, Secure Boot)

## Application Family

CripOS first-party applications use the **Crip** prefix:

| Application | Purpose | Status |
|---|---|---|
| Crip Welcome | First-run setup wizard | ✅ Complete |
| Crip Launcher | Start menu and app launcher | ✅ Complete |
| Crip Center | System settings center | ✅ Complete |
| Crip Store | Application store | 🚧 In Development |
| Crip Files | File manager | 🚧 In Development |
| Crip Terminal | Terminal emulator | ✅ Complete |
| Crip Update | System updates | ✅ Complete |
| Crip Monitor | System monitoring | ✅ Complete |
| Crip Installer | System installer | ✅ Complete |

## Architecture Layers

```
CripOS/
│
├── apps/          # First-party applications
├── sdk/           # Software Development Kit
├── api/           # Internal API layer
├── system/        # System modules (boot, login, security...)
├── services/      # Background services
├── libs/          # Shared libraries
├── themes/        # GTK themes
├── locales/       # Language files
└── docs/          # Documentation
```

## Development Status

**Current Phase:** Alpha 0.1

- ✅ Boot
- ✅ Login
- ✅ Crip Welcome
- ✅ Crip Launcher
- ✅ Crip Center
- ✅ Crip Terminal
- ✅ Crip Update
- ✅ Crip Installer
- 📋 Theme & Wallpapers
- 🚧 Store, Files, Monitor

See [02-roadmap.md](02-roadmap.md) for the full roadmap.