# CripOS System

## Overview

The CripOS system layer (`system/`) contains the low-level OS components that handle boot, login, desktop, security, services, and updates.

## Modules

### `system/boot/boot.py`

Boot sequence manager.

```python
from system.boot.boot import check_disk_space, check_memory, run_boot

run_boot()
# CripOS booting...
# CripOS boot complete.
```

**Functions:**
- `check_disk_space()` — Verify at least 1GB free
- `check_memory()` — Verify at least 512MB available
- `start_services()` — Start core systemd services
- `run_boot()` — Execute full boot sequence

---

### `system/login/login.py`

Login and user management.

```python
from system.login.login import create_user, authenticate, hash_password

create_user("cripuser", "mypassword")
authenticate("cripuser", "mypassword")  # True
```

**Functions:**
- `create_user(username, password)` — Create new user
- `authenticate(username, password)` — Verify credentials
- `hash_password(password)` — SHA-256 hash
- `run_login()` — Interactive login flow

**Storage:** `/etc/cripos/users.json`

---

### `system/desktop/desktop.py`

Desktop environment manager.

```python
from system.desktop.desktop import start_desktop, install_desktop_entry

start_desktop()
```

**Functions:**
- `start_desktop()` — Launch desktop environment
- `generate_desktop_entry(app_name, exec_path, icon_path)` — Create .desktop content
- `install_desktop_entry(app_name, exec_path, icon_path)` — Install .desktop file

---

### `system/recovery/recovery.py`

Recovery mode utilities.

```python
from system.recovery.recovery import repair_packages, reset_graphics

repair_packages()  # Fix broken packages
reset_graphics()   # Restart display manager
```

**Features:**
- Package repair via `apt-get install -f`
- Graphics driver reset
- System defaults restoration
- Recovery logging to `/var/log/cripos-recovery.log`

---

### `system/security/security.py`

Security manager.

```python
from system.security.security import (
    load_security_config, enable_firewall, run_security_check,
)

config = load_security_config()
results = run_security_check()
```

**Security features:**
- Firewall management (UFW)
- Secure boot status
- Auto-update policy
- Sudo requirement policy

**Storage:** `/etc/cripos/security.json`

---

### `system/services/services.py`

Service manager (systemctl wrapper).

```python
from system.services.services import list_services, start_service, restart_service

services = list_services()
start_service("crip-network.service")
```

**Managed services:**
- `crip-network.service`
- `crip-notify.service`
- `crip-power.service`
- `crip-update.service`
- `crip-wallpaper.service`
- `crip-ai.service`

---

### `system/startup/startup.py`

Startup applications manager.

```python
from system.startup.startup import get_startup_apps, set_startup_enabled

apps = get_startup_apps()
set_startup_enabled("crip-launcher", True)
```

**Storage:** `~/.config/cripos/startup.json`

**Defaults:**
- `crip-launcher`: enabled
- `crip-welcome`: disabled
- `crip-network`: enabled
- `crip-notify`: enabled

---

### `system/updates/updates.py`

Update manager (APT wrapper).

```python
from system.updates.updates import check_updates, install_updates, set_channel

status = check_updates()
install_updates()
set_channel("stable")
```

**Features:**
- Check available package updates
- Install updates via apt-get
- Multiple update channels (alpha, beta, stable)
- Auto-check and auto-install policies

**Storage:** `/etc/cripos/updates.json`

## System Initialization Flow

```
Power On
  ↓
BIOS/UEFI
  ↓
Bootloader (GRUB)
  ↓
system/boot/boot.py
  ├── Check disk space
  ├── Check memory
  └── Start services
      ↓
system/login/login.py
  ├── User authentication
  └── Password verification
      ↓
system/desktop/desktop.py
  └── Launch desktop environment
      ↓
system/startup/startup.py
  └── Start configured apps
```

## Services

Service units are defined in `services/`:

```
services/
├── crip-network.service
├── crip-notify.service
├── crip-power.service
├── crip-update.service
├── crip-wallpaper.service
└── crip-ai.service