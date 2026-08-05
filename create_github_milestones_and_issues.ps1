# PowerShell script to create GitHub milestones and issues for CripOS
# Usage: Open PowerShell in the repo root and run: .\create_github_milestones_and_issues.ps1
# Requires: GitHub CLI (gh) installed and authenticated (gh auth login)

$ErrorActionPreference = 'Stop'

# Define milestones and issues
$milestones = @(
    @{ title = 'Core Applications'; description = 'Core apps required for v0.1 Alpha' },
    @{ title = 'Design'; description = 'Design work: icons, sounds, wallpapers' },
    @{ title = 'System'; description = 'System-level features and package manager' },
    @{ title = 'Quality'; description = 'Integration tests and alpha testing' },
    @{ title = 'Release'; description = 'ISO build and release tasks' }
)

$issues = @(
    @{ milestone = 'Core Applications'; title = 'Desktop Branding'; body = 'Add CripOS desktop branding: themes, logos, and login theme.' },
    @{ milestone = 'Core Applications'; title = 'Wallpapers'; body = 'Create and package default wallpapers for Dark/Light/Minecraft themes.' },
    @{ milestone = 'Core Applications'; title = 'Crip Launcher'; body = 'Implement and polish the Crip Launcher application.' },
    @{ milestone = 'Core Applications'; title = 'Crip Center'; body = 'Implement and polish the Crip Center application (settings hub).' },
    @{ milestone = 'Core Applications'; title = 'Crip Files'; body = 'Implement and polish the Crip Files file manager.' },
    @{ milestone = 'Core Applications'; title = 'Crip Terminal'; body = 'Implement and polish the Crip Terminal application.' },
    @{ milestone = 'Core Applications'; title = 'Crip Update'; body = 'Implement system update UI and backend.' },

    @{ milestone = 'Design'; title = 'Icons'; body = 'Design and include icon theme for CripOS.' },
    @{ milestone = 'Design'; title = 'Sounds'; body = 'Design and include system sounds and alerts.' },

    @{ milestone = 'System'; title = 'Package Manager'; body = 'Implement package manager integration for installing 3rd-party apps.' },

    @{ milestone = 'Quality'; title = 'Integration Tests'; body = 'Write integration tests to validate app flows (Welcome → Launcher → Center → Files → Terminal).' },
    @{ milestone = 'Quality'; title = 'Alpha Testing'; body = 'Coordinate Alpha testing sessions and gather feedback.' },

    @{ milestone = 'Release'; title = 'Build ISO'; body = 'Automate ISO building for CripOS v0.1 Alpha.' },
    @{ milestone = 'Release'; title = 'Release Notes'; body = 'Draft release notes template and populate for v0.1 Alpha.' },
    @{ milestone = 'Release'; title = 'GitHub Release'; body = 'Create GitHub release entry for v0.1 Alpha.' }
)

# Helper: run gh if available, otherwise print commands
function Run-GhOrPrint($args) {
    if (Get-Command gh -ErrorAction SilentlyContinue) {
        gh $args
    } else {
        Write-Host "gh $args"
    }
}

Write-Host "Creating milestones..."
foreach ($m in $milestones) {
    $title = $m.title
    $desc = $m.description
    Write-Host "- Creating milestone: $title"
    Run-GhOrPrint "milestone create --title \"$title\" --description \"$desc\""
}

Write-Host "Creating issues..."
foreach ($i in $issues) {
    $title = $i.title
    $body = $i.body
    $ms = $i.milestone
    Write-Host "- Creating issue: $title (milestone: $ms)"
    Run-GhOrPrint "issue create --title \"$title\" --body \"$body\" --milestone \"$ms\""
}

Write-Host "Done. If gh is installed and authenticated, milestones and issues should be created. If gh was not found, run the printed gh commands manually after installing/authenticating."