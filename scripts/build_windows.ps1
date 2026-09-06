<#
.SYNOPSIS
Construye un ejecutable de Windows de la Guía de Probabilidad.

.DESCRIPTION
Instala las herramientas de construcción declaradas por el proyecto y crea
dist/GuiaProbabilidad/GuiaProbabilidad.exe con los recursos visuales incluidos.
#>

$ErrorActionPreference = "Stop"

python -m pip install ".[build]"
python -m PyInstaller `
    --noconfirm `
    --clean `
    --windowed `
    --name GuiaProbabilidad `
    --collect-data guia_probabilidad `
    --collect-all pygame `
    -m guia_probabilidad

Write-Host "Ejecutable creado en dist/GuiaProbabilidad/GuiaProbabilidad.exe"
