# Crip Welcome

Crip Welcome is the localized first-run experience for CripOS Alpha 0.1.

## Flow

1. Welcome to CripOS
2. Choose Uzbek or English
3. Check internet without blocking setup
4. Review the Alpha update hand-off
5. Finish and open the system through Crip Launcher

The selected language and completion state are written to the current user's
XDG config directory (`~/.config/cripos/welcome.json` by default). This keeps
the application bundle under `/opt/cripos` read-only after installation.

Run it manually with:

```bash
python3 apps/crip-welcome/main.py --force
```

Run its focused test suite with:

```bash
python3 -m unittest discover -s apps/crip-welcome -p 'test_*.py' -v
```
