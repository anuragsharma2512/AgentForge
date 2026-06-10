$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Python = Join-Path $ProjectRoot "venv\python.exe"

if (-not (Test-Path $Python)) {
    throw "Could not find Python at $Python"
}

Set-Location $ProjectRoot
& $Python -m streamlit run app.py
