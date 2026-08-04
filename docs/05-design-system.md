# CripOS Design System

## Colors

### Crip Dark (Default)

| Token | Hex | Usage |
|---|---|---|
| `--crip-bg` | `#0D1117` | Main background |
| `--crip-surface` | `#161B22` | Cards, sidebars |
| `--crip-border` | `#30363D` | Borders, dividers |
| `--crip-text` | `#F0F6FC` | Primary text |
| `--crip-muted` | `#8B949E` | Secondary text |
| `--crip-primary` | `#39D353` | Primary actions, accents |
| `--crip-secondary` | `#2EA043` | Hover, active states |
| `--crip-danger` | `#F85149` | Errors, warnings |

### Crip Light

| Token | Hex | Usage |
|---|---|---|
| `--crip-bg` | `#FFFFFF` | Main background |
| `--crip-surface` | `#F6F8FA` | Cards, sidebars |
| `--crip-border` | `#D0D7DE` | Borders, dividers |
| `--crip-text` | `#1F2328` | Primary text |
| `--crip-muted` | `#656D76` | Secondary text |
| `--crip-primary` | `#1F883D` | Primary actions |
| `--crip-secondary` | `#2EA043` | Hover states |
| `--crip-danger` | `#CF222E` | Errors |

### Minecraft

| Token | Hex | Usage |
|---|---|---|
| `--crip-bg` | `#1D1D1D` | Main background |
| `--crip-surface` | `#2D2D2D` | Cards, sidebars |
| `--crip-border` | `#3D3D3D` | Borders |
| `--crip-text` | `#FFFFFF` | Primary text |
| `--crip-primary` | `#55FF55` | Primary actions |
| `--crip-secondary` | `#00AA00` | Hover states |
| `--crip-danger` | `#FF5555` | Errors |

## Typography

| Element | Font | Size | Weight |
|---|---|---|---|
| Headings | Segoe UI | 18-24px | Bold |
| Body | Segoe UI | 11-12px | Normal |
| Labels | Segoe UI | 10-11px | Semibold |
| Muted text | Segoe UI | 10px | Normal |
| Minecraft accent | Minecraft | 14px | Normal |

## Spacing

| Scale | Value |
|---|---|
| `space-1` | 4px |
| `space-2` | 8px |
| `space-3` | 12px |
| `space-4` | 16px |
| `space-5` | 20px |
| `space-6` | 24px |

## Icons

Applications use emoji as lightweight icons:

- 🖌️ Appearance
- 🌍 Language
- 🌐 Network
- 🔄 Updates
- 🔒 Security
- ℹ️ About

## Component Guidelines

### Buttons
- **Primary:** `#39D353` background, dark text, bold
- **Secondary:** `#30363D` background, light text
- **Flat:** no border, border-radius 0
- **Hover:** darken background
- **Active:** use primary green

### Cards
- Surface color background
- 1px border in border color
- 12px border radius (except Minecraft: 0)

### Forms
- Inputs: dark background, 1px border
- Focus: green border
- Checkboxes/Radios: green when selected

### Toasts
- Border color background
- Light text
- Auto-dismiss after 2 seconds

## Splash Text

CripOS features Minecraft-inspired random splash text shown at startup:

```
✨ Never Gives Up!
✨ Gaming Ready!
✨ Powered by Debian!
✨ Crafted with ❤️
✨ Hello, Criperman!
✨ Let's Build Something!
✨ Time to Play!
```

Splash texts are displayed in yellow/gold (`#FFAA00`) for that Minecraft feel.