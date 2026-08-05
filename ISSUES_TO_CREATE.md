# CripOS — Issues to create on GitHub

This file lists the issues to create for the v0.1 Alpha work. Use the provided PowerShell script `create_github_milestones_and_issues.ps1` to create milestones and issues automatically via the GitHub CLI (gh).

Instructions
1. Install GitHub CLI (gh) and authenticate: `gh auth login`.
2. From the repo root, run: `.uild\create_github_milestones_and_issues.ps1` (PowerShell)

Milestones and issues (one entry per issue):

# Milestone: Foundation (already complete)
(no issues created)

# Milestone: Core Applications
- [ ] Desktop Branding -- Add branding assets (logos, login theme, greeter). @design
- [ ] Wallpapers -- Provide default wallpapers for Dark/Light/Minecraft. @design
- [ ] Crip Launcher -- Implement launcher app and integrate with Welcome. @app
- [ ] Crip Center -- Settings hub, main configuration UI. @app
- [ ] Crip Files -- File manager polishing and integration. @app
- [ ] Crip Terminal -- Terminal application polish, default shell config. @app
- [ ] Crip Update -- Update manager UI and backend. @infra

# Milestone: Design
- [ ] Icons -- Design and include icon theme.
- [ ] Sounds -- Create system sounds pack.

# Milestone: System
- [ ] Package Manager -- Integrate package manager (frontend + backend).

# Milestone: Quality
- [ ] Integration Tests -- Add tests covering Welcome → Launcher → Center → Files → Terminal.
- [ ] Alpha Testing -- Coordinate testers and collect issues.

# Milestone: Release
- [ ] Build ISO -- Create automated ISO build pipeline/script.
- [ ] Release Notes -- Create release notes for v0.1 Alpha.
- [ ] GitHub Release -- Draft and publish GitHub release for v0.1 Alpha.


Notes
- The script expects `gh` to be installed and authenticated with push/create permissions on this repository.
- If `gh` is not available, the script prints the gh commands so they can be run manually.
