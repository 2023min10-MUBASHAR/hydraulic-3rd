# Hydraulic Drill Machine Performance & Efficiency Analyzer

A professional engineering software application for analyzing hydraulic drill machine performance in mining, drilling, and rock excavation operations.

## Features

### Core Functionality
- **Real-time Performance Analysis**: Evaluates hydraulic drill machine efficiency (0-100%)
- **12 Drill Types**: Support for various drilling machine configurations
- **Engineering Calculations**: 
  - Hydraulic power (kW)
  - Piston area (mm²)
  - Hydraulic force (N)
  - Drill Performance Index (DPI)
- **Advanced Bit Life Analysis**: 
  - Drill bit wear percentage calculation
  - Remaining bit life estimation
  - Operating hours prediction
  - Bit health assessment

### Intelligent Diagnostics
- Parameter-specific analysis with actionable recommendations
- Critical, warning, and info-level alerts
- Identification of performance bottlenecks
- Machine health assessment (0-100%)

### Visualization & Reporting
- Real-time efficiency gauge meter
- Performance radar chart
- Health score visualization
- Historical trend analysis
- PDF and Excel report generation
- Analysis history tracking

### Advanced Features
- Dark/Light theme support
- Input validation with error handling
- Optimization advisor with efficiency predictions
- Historical data persistence
- Data export to CSV
- Professional engineering dashboard

## System Requirements

- Python 3.8+
- Windows, macOS, or Linux

## Installation

### 1. Clone or Download the Project
```bash
cd "c:\Users\Prime Laptops\OneDrive\Documents\Desktop\hydraulic 3rd"
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Application

### Start the Streamlit Server
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Alternative: Using Python directly
```bash
python -m streamlit run app.py
```

## Usage Guide

### 1. Analysis Tab
1. Select your drill type from the dropdown menu
2. Adjust the following parameters using sliders:
   - Hydraulic Pressure (50-500 bar)
   - Flow Rate (10-300 L/min)
   - Rotation Speed (10-1000 RPM)
   - Oil Temperature (-20 to 120°C)
   - Piston Diameter (5-200 mm)
   - Drill Bit Diameter (1-300 mm)
3. Click "ANALYZE MACHINE" to run the analysis
4. View the results including efficiency percentage and machine health score

### 2. History Tab
- View all previous analyses
- Track efficiency and health trends
- Filter by drill type or date
- Export analysis history to CSV

### 3. Diagnostics Tab
- Review system alerts and recommendations
- Identify critical issues requiring immediate attention
- Get parameter-specific guidance for optimization

### 4. Optimization Tab
- Receive AI-driven recommendations for improvement
- See estimated efficiency gains for each suggestion
- Get specific actions to implement improvements

### 5. Reports Tab
- Generate professional PDF reports
- Export data to Excel spreadsheets
- Download formatted analysis summaries

## Project Structure

```
hydraulic_analyzer/
├── app.py                      # Main Streamlit application
├── analyzer.py                 # Core engineering calculations
├── data_manager.py             # History and settings management
├── report_generator.py         # PDF and Excel report generation
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── data/                       # Auto-created directory for data
│   ├── analysis_history.json   # Analysis history storage
│   └── settings.json           # Application settings
└── reports/                    # Auto-created directory for reports
```

## Engineering Reference

### Drill Types Supported
1. Hydraulic Drill Machine
2. Underground Mining Jumbo Drill
3. Heavy-Duty Rock Drill
4. Rotary Drill
5. Blast Hole Production Drill
6. Light Drilling Machine
7. Quarry Drilling Machine
8. Core Drilling Machine
9. Diamond Core Drill
10. Exploration Drill
11. DTH (Down-The-Hole) Drill
12. Top Hammer Drill

### Efficiency Categories
- **90-100%**: Excellent (Green) ✅
- **80-89%**: Very Good (Light Green) ✅
- **70-79%**: Good (Yellow) ⚠️
- **60-69%**: Fair (Orange) ⚠️
- **50-59%**: Poor (Orange-Red) ❌
- **Below 50%**: Critical (Red) 🔴

### Machine Health Status
- **90-100%**: Healthy ✅
- **75-89%**: Stable ✅
- **60-74%**: Attention Required ⚠️
- **40-59%**: Maintenance Required ❌
- **Below 40%**: Critical Condition 🔴

## Calculation Formulas

### Hydraulic Power
```
Power (kW) = (Pressure × Flow Rate) / 600
```

### Piston Area
```
Area (mm²) = π × (Diameter²) / 4
```

### Hydraulic Force
```
Force (N) = Pressure (Pa) × Piston Area (m²)
```

### Drill Performance Index (DPI)
```
DPI = (0.25 × Pressure Score) + 
      (0.20 × Flow Rate Score) + 
      (0.20 × RPM Score) + 
      (0.20 × Temperature Score) + 
      (0.05 × Piston Diameter Score) + 
      (0.05 × Bit Diameter Score) + 
      (0.05 × Drill Type Factor)
```

## Operating Ranges

### Hydraulic Pressure (bar)
- 120-180: Poor
- 180-220: Fair
- 220-280: Good
- 280-350: Excellent
- Above 350: Overload Warning

### Flow Rate (L/min)
- Below 50: Poor
- 50-80: Fair
- 80-120: Good
- 120-180: Excellent
- Above 180: Overload

### RPM
- Below 100: Poor
- 100-180: Fair
- 180-300: Good
- 300-450: Excellent
- Above 450: Excessive

### Oil Temperature (°C)
- Below 20: Cold Start
- 20-40: Good
- 40-60: Excellent
- 60-75: Fair
- 75-90: Poor
- Above 90: Critical

## Troubleshooting

### Application won't start
```bash
# Clear Streamlit cache
streamlit cache clear

# Try running with verbose output
streamlit run app.py --logger.level=debug
```

### Missing dependencies
```bash
# Reinstall all requirements
pip install -r requirements.txt --force-reinstall
```

### Data not saving
- Check that the `data/` directory has write permissions
- Ensure sufficient disk space is available

### PDF/Excel export not working
- Verify reportlab and openpyxl are installed: `pip install reportlab openpyxl`
- Check that the `reports/` directory exists and has write permissions

## API Reference

### HydraulicDrillAnalyzer Class

```python
from analyzer import HydraulicDrillAnalyzer

# Create analyzer for specific drill type
analyzer = HydraulicDrillAnalyzer("Hydraulic Drill Machine")

# Validate inputs
is_valid, errors = analyzer.validate_inputs(
    pressure=250, flow_rate=120, rpm=300,
    temperature=45, piston_diameter=100, bit_diameter=150
)

# Run complete analysis
result = analyzer.run_analysis(
    pressure=250, flow_rate=120, rpm=300,
    temperature=45, piston_diameter=100, bit_diameter=150
)

# Get optimization recommendations
recommendations = analyzer.get_optimization_recommendations(result)
```

## Performance Metrics

The application calculates:
- **Efficiency Percentage**: Overall machine performance (0-100%)
- **Health Score**: Machine condition assessment (0-100%)
- **Hydraulic Power**: Actual power generation
- **Hydraulic Force**: Force exerted by the drill
- **DPI Score**: Normalized performance index

## Data Privacy

- All analysis data is stored locally in the `data/` directory
- No data is transmitted to external servers
- Historical data can be cleared at any time from the History tab

## System Specifications

### Recommended Hardware
- CPU: 2+ GHz processor
- RAM: 4GB minimum, 8GB recommended
- Disk: 500MB free space
- Display: 1366×768 or higher

### Supported Operating Systems
- Windows 7+
- macOS 10.12+
- Linux (Ubuntu 18.04+, CentOS 7+, etc.)

## License

This software is provided for professional engineering and mining operations.

## Support & Documentation

For detailed engineering documentation and technical support, refer to the inline code comments in each module:
- `analyzer.py`: Engineering calculations
- `data_manager.py`: Data persistence
- `report_generator.py`: Report generation
- `app.py`: UI and user interface

## Version History

### Version 1.0 (Initial Release)
- Core performance analysis
- 12 drill types
- Real-time diagnostics
- History tracking
- PDF/Excel reporting
- Interactive dashboard

## Credits

**Hydraulic Drill Machine Performance & Efficiency Analyzer**
- Professional Mining Engineering Software Suite
- Built with Python, Streamlit, Plotly, and ReportLab

---

**Last Updated**: 2024
**Status**: Production Ready ✅
#   h y d r a u l i c - s y s t e m  
 