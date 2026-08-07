# CripOS Themes

This folder contains the GTK themes for CripOS.

## Available Themes

| Theme | Style | Description |
|-------|-------|-------------|
| `crip-dark` | Dark | Default dark theme — deep blue-gray background |
| `crip-light` | Light | Light theme — clean white background |
| `cripgreen` | Dark | Dark green modern look — deep forest green |
| `minecraft` | Dark | Minecraft-inspired accents — retro pixel style |

## Theme Structure

Each theme directory contains:
- `gtk.css` — GTK stylesheet

## Usage

```bash
# List available themes
python crip.py theme list

# Switch theme
python crip.py theme cripgreen
```

Themes are managed by `system/theme_manager.py`.

## Related UI Assets

| Asset | Location | Description |
|-------|----------|-------------|
| Wallpapers | `assets/wallpapers/` | 6 SVG wallpapers (forest, developer, gaming, minimal, inspiration, mascot) |
| Icons | `assets/icons/crip-icons.svg` | CripOS icon set |
| Cursors | `themes/crip-dark/cursors/` | Cursor theme |
| Plymouth | `assets/boot/plymouth/crip-plymouth/` | Boot splash animation |
| Login | `assets/login/lightdm/crip-login/` | LightDM login screen |
| Sounds | `sounds/index.theme` | System sound theme |