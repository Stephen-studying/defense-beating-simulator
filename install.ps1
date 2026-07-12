[CmdletBinding()]
param(
    [ValidateSet("codex", "generic", "project")]
    [string]$Agent = "codex",
    [string]$Destination,
    [switch]$Force
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Destination)) {
    if ($Agent -eq "codex") {
        $codexHome = $env:CODEX_HOME
        if ([string]::IsNullOrWhiteSpace($codexHome)) {
            $codexHome = Join-Path $env:USERPROFILE ".codex"
        }
        $Destination = Join-Path $codexHome "skills"
    } elseif ($Agent -eq "generic") {
        $agentHome = $env:AGENT_SKILLS_HOME
        if ([string]::IsNullOrWhiteSpace($agentHome)) {
            $agentHome = Join-Path $env:USERPROFILE ".agent-skills"
        }
        $Destination = $agentHome
    } else {
        throw "Project mode requires -Destination, for example: -Destination 'D:\YourProject\.agents\skills'"
    }
}

$source = Split-Path -Parent $MyInvocation.MyCommand.Path
$manifest = Join-Path $source "SKILL.md"
$skillName = "defense-beating-simulator"

if (-not (Test-Path -LiteralPath $manifest)) {
    throw "Cannot find SKILL.md at $manifest. Run this script from the repository root."
}

New-Item -ItemType Directory -Path $Destination -Force | Out-Null
$resolvedDestination = (Resolve-Path -LiteralPath $Destination).Path
$resolvedSource = (Resolve-Path -LiteralPath $source).Path
if ($resolvedDestination.StartsWith($resolvedSource)) {
    throw "Destination must not be inside the source repository. Choose another project directory or a user-level skills directory."
}
$target = Join-Path $resolvedDestination $skillName

if (Test-Path -LiteralPath $target) {
    if (-not $Force) {
        throw "Target already exists: $target. Re-run with -Force to replace it."
    }
    $resolvedTarget = (Resolve-Path -LiteralPath $target).Path
    if (-not $resolvedTarget.StartsWith($resolvedDestination)) {
        throw "Refusing to remove target outside destination: $resolvedTarget"
    }
    Get-ChildItem -LiteralPath $resolvedTarget -Recurse -Force -ErrorAction SilentlyContinue |
        ForEach-Object { $_.Attributes = "Normal" }
    Remove-Item -LiteralPath $resolvedTarget -Recurse -Force
}

New-Item -ItemType Directory -Path $target -Force | Out-Null
$excludedNames = @(".git", ".venv", "__pycache__", ".pytest_cache", "tmp-agent-install", ".agent-skills", "agent-skills")
Get-ChildItem -LiteralPath $source -Force |
    Where-Object { $excludedNames -notcontains $_.Name } |
    ForEach-Object {
        Copy-Item -LiteralPath $_.FullName -Destination $target -Recurse -Force
    }

Write-Host "Installed $skillName for '$Agent' to:"
Write-Host $target
Write-Host ""
if ($Agent -eq "codex") {
    Write-Host "Restart Codex, then use: Use `$defense-beating-simulator to analyze my project defense materials."
} else {
    Write-Host "Point your agent at one of these entrypoints:"
    Write-Host "  - $target\AGENTS.md"
    Write-Host "  - $target\SKILL.md"
    Write-Host "  - $target\CLAUDE.md or $target\GEMINI.md when your agent prefers those filenames"
}
