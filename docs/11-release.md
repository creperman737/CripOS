# CripOS Release Plan

## Release Channels

CripOS follows a structured release process with multiple channels:

| Channel | Purpose | Audience |
|---|---|---|
| **Alpha** | Development builds with latest features | Developers, testers |
| **Beta** | Feature-complete builds for testing | Early adopters |
| **RC** | Release candidates, bug fixes only | Final testers |
| **Stable** | Production-ready releases | All users |

## Versioning

CripOS uses semantic versioning: `MAJOR.MINOR.PATCH`

- **MAJOR** — Breaking changes (1.0, 2.0)
- **MINOR** — New features (0.1, 0.2)
- **PATCH** — Bug fixes (0.1.1)

## Current Release: Alpha 0.1

**Version:** 0.1 Alpha
**Codename:** Creeper
**Base:** Debian 13 (Trixie)

### Included Features
- ✅ Boot sequence
- ✅ Login manager
- ✅ Desktop environment
- ✅ Crip Welcome wizard
- ✅ Crip Launcher
- ✅ Crip Center (6 sections)
- ✅ Crip Terminal
- ✅ Crip Update
- ✅ Crip Installer
- ✅ SDK framework
- ✅ System modules (8)
- ✅ GTK themes (3)
- ✅ Test suite (41 tests)

### Known Limitations
- Crip Store not yet functional
- Crip Files basic only
- No gaming mode yet
- ISO builder requires manual setup
- Theme switching requires manual GTK config

## Release Process

### 1. Build

```bash
# Run all tests
python tests/test_alpha_apps.py
python tests/test_system_modules.py
python tests/test_sdk.py
python apps/crip-welcome/test_ui.py

# Verify code quality
python scripts/check_errors.py
python scripts/check_imports.py
python scripts/check_json.py
```

### 2. Package

```bash
# Build ISO (Linux)
bash scripts/build-iso.sh

# Build installer package
bash packages/cripos-base.sh
```

### 3. Version Increment

Update version in:
- `branding/version.txt`
- `api/system.py`
- `sdk/cripapi/__init__.py`
- `config/system.conf`

### 4. Changelog

Update `CHANGELOG.md` with:
- New features
- Bug fixes
- Breaking changes
- Migration notes

### 5. Tag & Release

```bash
git tag -a v0.1.0 -m "CripOS 0.1 Alpha Release"
git push origin v0.1.0
```

## Release Checklist

- [ ] All tests pass
- [ ] Code quality checks pass
- [ ] Version numbers consistent
- [ ] Changelog updated
- [ ] Documentation updated
- [ ] ISO builds successfully
- [ ] Installer works
- [ ] Release notes prepared

## Build Directories

The repo tracks build outputs by channel:

```
build/
├── alpha/    # Alpha builds
├── beta/     # Beta builds
├── stable/   # Stable releases
└── iso/      # ISO images
```

## Future Releases

### Alpha 0.2
- Crip Store functional
- Crip Files improved
- Crip Monitor expanded
- Package management

### Alpha 0.3
- Gaming Mode
- AI Assistant
- Performance tools
- Cloud integration

### Beta 1.0
- Feature complete
- Bug fixes focus
- Stable API

### Stable 1.0
- Production ready
- Full documentation
- Community support