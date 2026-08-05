# CripOS v0.1 Alpha — Release Notes

**Codename:** Creeper  
**Date:** 2026-08-05  
**Base:** Debian 13 (Trixie)  
**Desktop:** Cinnamon  
**Architecture:** x86_64

---

## 🎉 What's New

### 💻 Crip CLI (18 commands)
```
crip about          — CripOS haqida
crip doctor         — tizim salomatligi
crip version        — versiya
crip info           — tizim ma'lumoti
crip install <pkg>  — paket o'rnatish
crip remove <pkg>   — paket o'chirish
crip search <q>     — paket qidirish
crip packages       — o'rnatilgan paketlar
crip upgrade        — paketlarni yangilash
crip clean          — keshlarni tozalash
crip theme <name>   — tema almashtirish
crip wallpaper <n>  — fon rasmi
crip language <c>   — til almashtirish
crip center         — sozlamalar
crip welcome        — welcome wizard
crip store          — app store
crip files          — fayl menejeri
crip update         — yangilanishlar
```

### 🖥️ Crip Center
- Appearance (themes: crip-dark, crip-light, minecraft)
- Wallpaper (default, gaming, nature, dark)
- Language (en, uz)
- Network status
- Updates (auto-update toggle, check)
- Security (firewall)
- About (system info)

### 📁 Crip Files
- Browse folders
- Open files
- Copy / Move / Rename / Delete
- New Folder
- Sidebar places (Home, Documents, Pictures, Music, Videos, Downloads)

### 🖥️ Crip Launcher
- Search apps (real-time)
- Favorites (⭐)
- Recent apps
- Categories (All, System, Internet, Games)

### 🛒 Crip Store
- Browse apps by category
- Search
- Install / Remove (wired to real package manager)

### 🔄 Crip Update
- Check for updates
- Install updates
- Update channel display

---

## 🧪 Testing

- **69 tests** passing
- Unit tests, CLI tests, system module tests, SDK tests, splash tests
- 0 syntax errors across 489 Python files

---

## 📦 Installation

```bash
# From source
git clone https://github.com/creperman737/CripOS.git
cd CripOS
python crip.py doctor

# Run apps
python crip.py center
python crip.py files
python crip.py store
python crip.py welcome
```

---

## 🐛 Known Issues

- Alpha software — expect bugs
- Package manager requires apt (Linux)
- GUI apps require tkinter
- ISO builder requires xorriso/mkisofs (Linux)

---

## 🔮 Roadmap

- [ ] Live ISO
- [ ] Installer
- [ ] Boot Splash / Plymouth Theme
- [ ] QEMU / VirtualBox / VMware testing
- [ ] GitHub Release with SHA256

---

## 💚 Thank You

CripOS is built with 💚 by Criperman.  
Never Give Up.