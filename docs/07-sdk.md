# CripOS SDK

## Overview

The CripOS SDK allows developers to build applications for CripOS using Python. It provides clean, simple APIs for system access, UI components, widgets, and themes.

## Installation

```python
# Add the CripOS repo root to your path
import sys
sys.path.insert(0, "/opt/cripos")

# Now you can import the SDK
from sdk.cripapi import system_info
from sdk.cripui import button
from sdk.cripwidgets import card
from sdk.cripthemes import get_theme
```

## cripapi — System API

### `system_status()`
Returns the current system status.

```python
from sdk.cripapi import system_status

status = system_status()
# {'name': 'CripOS', 'status': 'ready'}
```

### `system_info()`
Returns detailed system information.

```python
from sdk.cripapi import system_info

info = system_info()
# {
#   'name': 'CripOS',
#   'version': 'Alpha 0.1',
#   'codename': 'Creeper',
#   'base': 'Debian 13 (Trixie)',
#   'desktop': 'Cinnamon',
#   'kernel': 'Linux',
#   'architecture': 'x86_64',
# }
```

### `get_apps()`
Returns the list of installed CripOS applications.

```python
from sdk.cripapi import get_apps

apps = get_apps()
# ['Crip Welcome', 'Crip Launcher', 'Crip Center', ...]
```

### `get_version()`
Returns the CripOS version string.

```python
from sdk.cripapi import get_version

version = get_version()
# 'CripOS 0.1 Alpha'
```

## cripui — UI Components

### `button(text)`
Creates a button element.

```python
from sdk.cripui import button

button("Click Me")
# '[button] Click Me'
```

### `label(text)`
Creates a label element.

### `input_field(placeholder)`
Creates an input field.

### `checkbox(text, checked)`
Creates a checkbox (default: unchecked).

```python
checkbox("Enable VPN", checked=True)
# '[checkbox] [x] Enable VPN'
```

### `dropdown(options)`
Creates a dropdown with options.

### `progress_bar(value, maximum)`
Creates a progress bar (default maximum: 100).

```python
progress_bar(50)
# '[progress] █████░░░░░ 50%'
```

## cripwidgets — Composite Widgets

### `card(title)`
Creates a card container.

### `window(title, width, height)`
Creates a window (default: 640x480).

### `dialog(title, message)`
Creates a dialog box.

### `toast(message)`
Creates a toast notification.

### `sidebar(items)`
Creates a sidebar with navigation items.

### `toolbar(items)`
Creates a toolbar with action items.

## cripthemes — Themes

### `default_theme()`
Returns the Crip Dark theme (default).

### `light_theme()`
Returns the Crip Light theme.

### `minecraft_theme()`
Returns the Minecraft theme.

### `get_theme(name)`
Returns a theme by name. Falls back to default if not found.

```python
from sdk.cripthemes import get_theme

dark = get_theme("crip-dark")
light = get_theme("crip-light")
mc = get_theme("minecraft")
```

## Example App

```python
#!/usr/bin/env python3
"""Example CripOS SDK app."""

from sdk.cripui import button
from sdk.cripapi import system_status


def main():
    status = system_status()
    print(button(f"Hello from {status['name']}"))
    print(f"Status: {status['status']}")


if __name__ == "__main__":
    main()
```

Run from `sdk/examples/hello_app.py` for a working example.

## Best Practices

1. Always add CripOS repo root to `sys.path`
2. Use `cripui` for simple UI elements, `cripwidgets` for composites
3. Handle missing themes with `get_theme()` fallback
4. Test your app with the CripOS test framework