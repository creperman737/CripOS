# CripOS API

## Overview

The CripOS API layer (`api/`) provides shared backend logic used by applications. It's the bridge between the application layer and the system layer.

## Modules

### `api/settings.py`

Settings sections for Crip Center.

```python
from api.settings import get_settings_sections

sections = get_settings_sections()
# ['Appearance', 'Language', 'Network', 'Privacy', 'Security', 'Display',
#  'Sound', 'Keyboard', 'Mouse', 'Gaming', 'Updates', 'Storage', 'About CripOS']
```

### `api/store.py`

Store categories for Crip Store.

```python
from api.store import get_store_categories

categories = get_store_categories()
# ['Featured', 'New Apps', 'Games', 'Development', 'Office', 'Internet',
#  'Multimedia', 'Utilities', 'Installed', 'Updates']
```

### `api/system.py`

System information.

```python
from api.system import get_system_info

info = get_system_info()
# {'name': 'CripOS', 'version': 'Alpha 0.1', 'status': 'development'}
```

### `api/system_api.py`

System API with CripCore integration.

```python
from api.system_api import SystemAPI

api = SystemAPI()
status = api.get_status()
# {'name': 'CripOS', 'version': 'Alpha 0.1', 'status': 'running'}
```

### `api/updates.py`

Update status for Crip Update.

```python
from api.updates import get_update_status

status = get_update_status()
# {'available': 0, 'installed': 1, 'channel': 'alpha'}
```

### `api/users.py`

User management.

```python
from api.users import get_default_user

user = get_default_user()
# 'cripuser'
```

### `api/launcher.py`

Launcher items for Crip Launcher.

```python
from api.launcher import get_launcher_items

items = get_launcher_items()
# ['Files', 'Browser', 'Terminal', 'Settings', 'Store', 'Updates', 'Games']
```

## Usage in Applications

### Import Pattern

```python
import sys
from pathlib import Path

# Add repo root to path
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

# Now import API modules
from api.system import get_system_info
from api.updates import get_update_status
```

### Example: Crip Update

```python
from api.updates import get_update_status

def show_updates():
    status = get_update_status()
    if status["available"] > 0:
        print(f"{status['available']} updates available")
    else:
        print("System is up to date")
```

## API Conventions

1. All API functions return `dict` or `list` types
2. Functions are pure — no side effects unless documented
3. Modules are importable without GUI dependencies
4. Thread-safe for background operations