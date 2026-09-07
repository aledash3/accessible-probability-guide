<#
.SYNOPSIS
Builds a standalone Windows executable for Accessible Probability Guide.

.DESCRIPTION
Installs project build dependencies and creates
dist/ProbabilityGuide/ProbabilityGuide.exe bundling all multimedia assets.
#>

$ErrorActionPreference = "Stop"

python -m pip install ".[build]"
python -m PyInstaller `
    --noconfirm `
    --clean `
    --windowed `
    --name ProbabilityGuide `
    --collect-data probability_guide `
    --collect-all pygame `
    -m probability_guide

Write-Host "Executable generated at dist/ProbabilityGuide/ProbabilityGuide.exe"
