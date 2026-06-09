#!/bin/bash

# Hydraulic Drill Machine Analyzer - Quick Start Script
# This script sets up the environment and runs the application

echo ""
echo "================================================"
echo "  HYDRAULIC DRILL MACHINE ANALYZER"
echo "  Quick Start Script"
echo "================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org"
    exit 1
fi

echo "[1/4] Python found: $(python3 --version)"

echo ""
echo "[2/4] Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created"
else
    echo "Virtual environment already exists"
fi

echo ""
echo "[3/4] Installing dependencies..."
source venv/bin/activate
pip install -q -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error installing dependencies"
    exit 1
fi
echo "Dependencies installed successfully"

echo ""
echo "[4/4] Starting Streamlit application..."
echo ""
echo "The application will open in your default browser at http://localhost:8501"
echo "Press Ctrl+C to stop the server"
echo ""

streamlit run app.py
