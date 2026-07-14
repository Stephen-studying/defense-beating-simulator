[CmdletBinding()]
param(
    [ValidateSet("codex", "agents", "generic", "claude", "gemini", "copilot", "project")]
    [string]$Agent = "codex",
    [string]$Destination,
    [switch]$Force
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Destination)) {
    switch ($Agent) {
        "codex" {
            $codexHome = $env:CODEX_HOME
            if ([string]::IsNullOrWhiteSpace($codexHome)) {
                $codexHome = Join-Path $env:USERPROFILE ".codex"
            }
            $Destination = Join-Path $codexHome "skills"
        }
        { $_ -in @("agents", "generic") } {
            $agentHome = $env:AGENT_SKILLS_HOME
            if ([string]::IsNullOrWhiteSpace($agentHome)) {
                $agentHome = Join-Path $env:USERPROFILE ".agents\skills"
            }
            $Destination = $agentHome
        }
        "claude" { $Destination = Join-Path $env:USERPROFILE ".claude\skills" }
        "gemini" { $Destination = Join-Path $env:USERPROFILE ".gemini\skills" }
        "copilot" { $Destination = Join-Path $env:USERPROFILE ".copilot\skills" }
        "project" {
            throw "Project mode requires -Destination, for example: -Destination 'D:\YourProject\.agents\skills'"
        }
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
$comparison = [StringComparison]::OrdinalIgnoreCase
$sourcePrefix = $resolvedSource.TrimEnd([IO.Path]::DirectorySeparatorChar) + [IO.Path]::DirectorySeparatorChar
if ($resolvedDestination.Equals($resolvedSource, $comparison) -or $resolvedDestination.StartsWith($sourcePrefix, $comparison)) {
    throw "Destination must not be inside the source repository. Choose another project directory or a user-level skills directory."
}

$target = Join-Path $resolvedDestination $skillName
if (Test-Path -LiteralPath $target) {
    if (-not $Force) {
        throw "Target already exists: $target. Re-run with -Force to replace it."
    }
    $resolvedTarget = (Resolve-Path -LiteralPath $target).Path
    $targetParent = Split-Path -Parent $resolvedTarget
    if (-not $targetParent.Equals($resolvedDestination, $comparison)) {
        throw "Refusing to remove target outside destination: $resolvedTarget"
    }
    Get-ChildItem -LiteralPath $resolvedTarget -Recurse -Force -ErrorAction SilentlyContinue |
        ForEach-Object { $_.Attributes = "Normal" }
    Remove-Item -LiteralPath $resolvedTarget -Recurse -Force
}

New-Item -ItemType Directory -Path $target -Force | Out-Null
$runtimeEntries = @("SKILL.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md", "LICENSE", "agents", "references", "assets")
foreach ($entry in $runtimeEntries) {
    $item = Join-Path $source $entry
    if (-not (Test-Path -LiteralPath $item)) {
        throw "Required runtime entry is missing: $entry"
    }
    Copy-Item -LiteralPath $item -Destination $target -Recurse -Force
}

if (-not (Test-Path -LiteralPath (Join-Path $target "SKILL.md"))) {
    throw "Installation failed: SKILL.md was not copied to $target"
}

Write-Host "Installed $skillName for '$Agent' to:"
Write-Host $target
Write-Host ""
if ($Agent -eq "codex") {
    Write-Host "Restart Codex, then invoke `$defense-beating-simulator."
} else {
    Write-Host "Ask the agent to discover the installed skill or read:"
    Write-Host "  - $target\SKILL.md"
    Write-Host "  - $target\AGENTS.md when explicit routing is needed"
}
