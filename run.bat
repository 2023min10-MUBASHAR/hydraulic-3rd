@echo off
REM Hydraulic Drill Machine Analyzer - Quick Start Script
REM This script sets up the environment and runs the application

echo.
echo ================================================
echo   HYDRAULIC DRILL MACHINE ANALYZER
echo   Quick Start Script
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo [1/4] Python found. Creating virtual environment...
if not exist "venv" (
    python -m venv venv
    echo Virtual environment created
) else (
    echo Virtual environment already exists
)

echo.
echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [3/4] Installing dependencies...
pip install -q -r requirements.txt
if errorlevel 1 (
    echo Error installing dependencies
    pause
    exit /b 1
)
echo Dependencies installed successfully

echo.
echo [4/4] Starting Streamlit application...
echo.
echo The application will open in your default browser at http://localhost:8501
echo Press Ctrl+C to stop the server
echo.

streamlit run app.py

pause
