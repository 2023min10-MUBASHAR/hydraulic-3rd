# Installation Guide

## Hydraulic Drill Machine Performance & Efficiency Analyzer

This guide provides step-by-step instructions for installing and running the application on Windows, macOS, and Linux.

## Prerequisites

- **Python 3.8 or higher** (Download from https://www.python.org/downloads/)
- **pip** (Python package manager, comes with Python)
- **At least 500MB of free disk space**
- **Modern web browser** (Chrome, Firefox, Safari, or Edge)

## Platform-Specific Installation

### Windows Installation

#### Method 1: Using the Quick Start Script (Easiest)

1. **Download the project** to your desired location
2. **Open Command Prompt** in the project directory
3. **Run the script**:
   ```cmd
   run.bat
   ```
4. The application will automatically:
   - Create a virtual environment
   - Install all dependencies
   - Start the Streamlit server
   - Open your browser

#### Method 2: Manual Installation

1. **Open Command Prompt** and navigate to the project directory:
   ```cmd
   cd "c:\Users\Prime Laptops\OneDrive\Documents\Desktop\hydraulic 3rd"
   ```

2. **Create virtual environment**:
   ```cmd
   python -m venv venv
   ```

3. **Activate virtual environment**:
   ```cmd
   venv\Scripts\activate
   ```
   
   (Your command prompt should now show `(venv)` at the beginning)

4. **Upgrade pip** (recommended):
   ```cmd
   python -m pip install --upgrade pip
   ```

5. **Install dependencies**:
   ```cmd
   pip install -r requirements.txt
   ```

6. **Run the application**:
   ```cmd
   streamlit run app.py
   ```

7. The browser should automatically open to `http://localhost:8501`

### macOS Installation

#### Method 1: Using the Quick Start Script (Easiest)

1. **Open Terminal** and navigate to the project directory
2. **Make the script executable**:
   ```bash
   chmod +x run.sh
   ```
3. **Run the script**:
   ```bash
   ./run.sh
   ```

#### Method 2: Manual Installation

1. **Open Terminal** and navigate to the project directory:
   ```bash
   cd /path/to/hydraulic_analyzer
   ```

2. **Check Python version**:
   ```bash
   python3 --version
   ```
   (Should be 3.8 or higher)

3. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   ```

4. **Activate virtual environment**:
   ```bash
   source venv/bin/activate
   ```
   
   (Your terminal should now show `(venv)` at the beginning)

5. **Upgrade pip** (recommended):
   ```bash
   python -m pip install --upgrade pip
   ```

6. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

7. **Run the application**:
   ```bash
   streamlit run app.py
   ```

### Linux Installation

#### Ubuntu/Debian

1. **Install Python and pip** (if not already installed):
   ```bash
   sudo apt-get update
   sudo apt-get install python3 python3-pip python3-venv
   ```

2. **Navigate to project directory**:
   ```bash
   cd /path/to/hydraulic_analyzer
   ```

3. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   ```

4. **Activate virtual environment**:
   ```bash
   source venv/bin/activate
   ```

5. **Upgrade pip**:
   ```bash
   python -m pip install --upgrade pip
   ```

6. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

7. **Run the application**:
   ```bash
   streamlit run app.py
   ```

#### CentOS/RHEL

1. **Install Python and pip**:
   ```bash
   sudo yum install python3 python3-pip
   ```

2. **Follow steps 2-7 from Ubuntu/Debian section above**

#### Fedora

1. **Install Python and pip**:
   ```bash
   sudo dnf install python3 python3-pip
   ```

2. **Follow steps 2-7 from Ubuntu/Debian section above**

## Verifying Installation

After installation, verify everything is working:

1. **Check Python version**:
   ```bash
   python --version  # or python3 --version
   ```
   Should show Python 3.8+

2. **Check pip packages** (with venv activated):
   ```bash
   pip list
   ```
   Should show streamlit, pandas, plotly, etc.

3. **Test the application**:
   ```bash
   streamlit run app.py
   ```
   Browser should open with the application

## Troubleshooting

### Issue: "Python command not found"

**Solution:**
- Ensure Python is installed: Download from https://www.python.org/downloads/
- On Windows, check "Add Python to PATH" during installation
- On macOS/Linux, Python might be `python3` instead of `python`

### Issue: "venv not found" or "Virtual environment activation fails"

**Solution:**
```bash
# Delete existing venv and recreate
rm -rf venv  # On Windows: rmdir /s venv
python -m venv venv
```

### Issue: "Module not found" errors

**Solution:**
- Ensure virtual environment is activated (should see `(venv)` in terminal)
- Reinstall dependencies:
```bash
pip install -r requirements.txt --force-reinstall
```

### Issue: "Address already in use" when starting the app

**Solution:**
Streamlit is already running on port 8501. Either:
- Close the other instance, or
- Run on a different port:
```bash
streamlit run app.py --server.port 8502
```

### Issue: Port 8501 blocked by firewall

**Solution:**
- Configure your firewall to allow local connections, or
- Use a different port as shown above

### Issue: Slow startup or high memory usage

**Solution:**
```bash
# Clear Streamlit cache
streamlit cache clear

# Run with minimal dependencies
streamlit run app.py --client.showErrorDetails=false
```

### Issue: PDF/Excel export not working

**Solution:**
Ensure required packages are installed:
```bash
pip install reportlab openpyxl --upgrade
```

### Issue: "Permission denied" on macOS/Linux

**Solution:**
```bash
chmod +x run.sh
chmod +x app.py
```

## Uninstalling

To completely remove the application and virtual environment:

**Windows:**
```cmd
rmdir /s venv
rmdir /s data
rmdir /s reports
REM Delete the project folder
```

**macOS/Linux:**
```bash
rm -rf venv
rm -rf data
rm -rf reports
# Delete the project folder
```

## Upgrading

To upgrade the application:

1. **Backup your data**:
   ```bash
   cp -r data data_backup  # macOS/Linux
   xcopy data data_backup /E /I  # Windows
   ```

2. **Download the latest version** and replace files (except `data/` directory)

3. **Update dependencies**:
   ```bash
   pip install -r requirements.txt --upgrade
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## System Requirements

### Minimum
- CPU: 2 GHz processor
- RAM: 2 GB
- Disk: 500 MB free space
- OS: Windows 7+, macOS 10.12+, Ubuntu 16.04+

### Recommended
- CPU: 2.5+ GHz processor
- RAM: 4-8 GB
- Disk: 1 GB free space
- OS: Windows 10+, macOS 10.15+, Ubuntu 18.04+

## Performance Optimization

For better performance:

1. **Use SSD** instead of HDD for faster file access

2. **Close unnecessary applications** to free up RAM

3. **Update your browser** to the latest version

4. **Clear Streamlit cache** periodically:
   ```bash
   streamlit cache clear
   ```

5. **Limit history retention**:
   - App automatically keeps last 100 analyses
   - Export and archive old data as needed

## Getting Help

If you encounter issues:

1. Check the Troubleshooting section above
2. Review error messages carefully
3. Check Python and pip versions
4. Ensure all dependencies are installed
5. Try clearing cache and reinstalling dependencies

## Next Steps

After successful installation:

1. Read the [README.md](README.md) for usage instructions
2. Review the [Features](#) section
3. Run your first analysis
4. Explore the dashboard features

---

**Version**: 1.0  
**Last Updated**: 2024  
**Status**: Ready for Production ✅
