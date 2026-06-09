# User Manual

## Hydraulic Drill Machine Performance & Efficiency Analyzer

### Complete User Guide with Practical Examples

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Interface Overview](#interface-overview)
3. [Running Your First Analysis](#running-your-first-analysis)
4. [Understanding Results](#understanding-results)
5. [Working with History](#working-with-history)
6. [Diagnostics Interpretation](#diagnostics-interpretation)
7. [Optimization Recommendations](#optimization-recommendations)
8. [Generating Reports](#generating-reports)
9. [Tips & Best Practices](#tips--best-practices)
10. [Troubleshooting](#troubleshooting)

---

## Getting Started

### System Requirements

**Minimum:**
- Windows 7+, macOS 10.12+, or Ubuntu 16.04+
- 2GB RAM
- Internet browser (Chrome, Firefox, Safari, or Edge)

**Recommended:**
- Windows 10+, macOS 10.15+, or Ubuntu 18.04+
- 4-8GB RAM
- Modern browser with JavaScript enabled

### Installation Quick Start

1. **Install Python 3.8+** from https://www.python.org
2. **Download the application** to your desired folder
3. **Run the quick-start script**:
   - Windows: Double-click `run.bat`
   - macOS/Linux: Run `chmod +x run.sh && ./run.sh`
4. **Wait for browser to open** - typically within 30 seconds
5. **Accept local connection** if prompted by firewall

---

## Interface Overview

### Main Dashboard Areas

```
┌─────────────────────────────────────────────────────────┐
│ ⛏️ HYDRAULIC DRILL MACHINE ANALYZER                      │
├─────────────────────────────────────────────────────────┤
│ [📊 Analysis] [📈 History] [📋 Diagnostics] [🔧 Optimization] [📄 Reports] │
├──────────────────────────────┬──────────────────────────┤
│   LEFT: INPUT PARAMETERS     │  RIGHT: QUICK SUMMARY    │
│   ├─ Drill Type Selection    │  ├─ Efficiency Gauge     │
│   ├─ Pressure Slider         │  ├─ Health Meter         │
│   ├─ Flow Rate Slider        │  └─ Quick Stats          │
│   ├─ RPM Slider              │                          │
│   ├─ Temperature Slider       │  MAIN AREA:              │
│   ├─ Piston Diameter Slider   │  ├─ Metrics Cards       │
│   ├─ Drill Bit Diameter       │  ├─ Engineering Values  │
│   └─ ANALYZE MACHINE Button   │  ├─ Performance Radar   │
│                              │  └─ Detailed Results    │
└──────────────────────────────┴──────────────────────────┘
```

### Sidebar Menu

- **Theme Selection**: Switch between Light and Dark modes
- **Application Info**: Version and feature overview

---

## Running Your First Analysis

### Step-by-Step Tutorial

#### Step 1: Select Drill Type

1. Click on the **"Select Drill Type"** dropdown
2. Choose your machine type from the 12 available options:
   - Hydraulic Drill Machine (standard choice)
   - Underground Mining Jumbo Drill
   - Heavy-Duty Rock Drill
   - etc.

**💡 Tip:** If unsure, start with "Hydraulic Drill Machine" - the software will adjust calculations based on your selection.

#### Step 2: Set Input Parameters

Adjust the sliders for your current operating conditions:

**Hydraulic Pressure (50-500 bar)**
- Drag the slider to match your system pressure gauge
- Typical range: 200-300 bar
- Example value: 250 bar

**Flow Rate (10-300 L/min)**
- Match your pump's flow rating
- Typical range: 80-150 L/min
- Example value: 120 L/min

**Rotation Speed (10-1000 RPM)**
- Current drill rotation speed
- Typical range: 200-400 RPM
- Example value: 300 RPM

**Oil Temperature (-20 to 120°C)**
- Monitor from the hydraulic oil temperature gauge
- Optimal range: 40-60°C
- Example value: 45°C

**Piston Diameter (5-200 mm)**
- Check your hydraulic cylinder specifications
- Typical range: 80-120 mm
- Example value: 100 mm

**Drill Bit Diameter (1-300 mm)**
- Size of the drill bit being used
- Typical range: 100-200 mm
- Example value: 150 mm

#### Step 3: Run Analysis

1. Click the **"🔍 ANALYZE MACHINE"** button (blue button)
2. Wait 2-3 seconds for calculations to complete
3. Results will appear automatically on the dashboard

### Practical Example

**Scenario:** You're operating a Hydraulic Drill Machine in a limestone quarry.

**Current Readings:**
- Pressure gauge: 240 bar
- Flow meter: 110 L/min
- Tachometer: 280 RPM
- Oil thermometer: 52°C
- Cylinder specs: 95mm piston
- Bit size: 160mm

**Input these values:**

1. Drill Type: "Hydraulic Drill Machine" ✓
2. Pressure: 240 (drag slider)
3. Flow Rate: 110 (drag slider)
4. RPM: 280 (drag slider)
5. Temperature: 52 (drag slider)
6. Piston Diameter: 95 (drag slider)
7. Drill Bit Diameter: 160 (drag slider)
8. Click "ANALYZE MACHINE"

**Expected Results:**
- Efficiency: ~78% (Good)
- Health Score: ~80% (Stable)
- Hydraulic Power: ~44 kW
- Hydraulic Force: ~180,000 N

---

## Understanding Results

### Metrics Explained

#### 1. Efficiency Percentage

**What it means:** Overall machine performance (0-100%)

| Value | Meaning | Action |
|-------|---------|--------|
| 90-100% | ✅ Excellent | Continue monitoring |
| 80-89% | ✅ Very Good | Routine maintenance |
| 70-79% | ⚠️ Good | Schedule maintenance |
| 60-69% | ⚠️ Fair | Optimize settings |
| 50-59% | ❌ Poor | Urgent attention needed |
| < 50% | ❌ Critical | Stop and investigate |

#### 2. Machine Health Score

**What it means:** Overall machine condition (0-100%)

Considers:
- Pressure system health
- Flow delivery health
- Rotation system health
- Thermal stability
- Combined efficiency

#### 3. Hydraulic Power (kW)

**What it means:** Actual power being delivered to the drill

**Formula:** Power = (Pressure × Flow Rate) / 600

**Example:** (250 × 120) / 600 = 50 kW

**Interpretation:**
- Higher power = more drilling capability
- Typical range: 30-100 kW

#### 4. Piston Area (mm²)

**What it means:** Effective area of the hydraulic piston

**Formula:** Area = π × (Diameter²) / 4

**Example:** π × (100²) / 4 = 7,854 mm²

**Interpretation:**
- Larger area = more force
- Critical for force calculations

#### 5. Hydraulic Force (N)

**What it means:** Drilling force generated

**Formula:** Force = Pressure (Pa) × Piston Area (m²)

**Example:** 25 MPa × 0.00785 m² ≈ 196,350 N

**Interpretation:**
- Higher force = better drilling performance
- Typical range: 100,000 - 500,000 N

### Performance Radar Chart

A visual representation of all parameters normalized to 0-100:

```
         Pressure (250 bar)
              ★ 95%
           ╱    ╲
   Piston ★ 70%  ★ 95% Bit Size
         ╱          ╲
    RPM ★─────────────★ 90% Temperature
      90%      ╲ ╱
          80% ★ 85% Flow Rate
```

**How to read it:**
- Points near the outer circle = strong parameter
- Points near center = weak parameter
- Balanced shape = good overall performance
- Unbalanced shape = parameter needs adjustment

---

## Working with History

### Accessing History Tab

1. Click the **"📈 History"** tab at the top
2. View statistics and trends from all your analyses

### Statistics Dashboard

**Summary Cards Show:**
- Total Analyses: Count of all analyses performed
- Average Efficiency: Mean efficiency across all analyses
- Average Health Score: Mean health score
- Drill Types Analyzed: Number of different drill types used

### Trend Graph

**Shows:** Efficiency and health trends over time

**How to use:**
- Identify efficiency degradation patterns
- Check if interventions improved performance
- Plan preventive maintenance based on trends

### Drill Type Distribution

**Shows:** Pie chart of which drill types you've used most

**How to use:**
- Track equipment utilization
- Compare performance across different machines
- Plan maintenance scheduling

### History Table

**Shows:** Detailed list of last 50 analyses

**Columns:**
- Timestamp: When analysis was run
- Drill Type: Which machine was analyzed
- Efficiency %: Performance score
- Health Score: Condition indicator
- Category: Efficiency rating (Excellent, Good, etc.)

**How to use:**
- Click any row to view full details
- Sort by clicking column headers
- Search using Ctrl+F

### Exporting Data

#### Export to CSV

1. Scroll to "Export Options" section
2. Click **"📥 Export to CSV"** button
3. File saves automatically to `data/` folder
4. Open in Excel, Google Sheets, or any spreadsheet app

#### Clear History

1. Click **"🗑️ Clear History"** button
2. Click again to confirm
3. All historical data will be deleted (cannot undo)

---

## Diagnostics Interpretation

### Accessing Diagnostics

1. Click the **"📋 Diagnostics"** tab
2. View all system alerts and recommendations

### Alert Levels

#### 🚨 CRITICAL (Red)

**Immediate action required - Operation at risk**

Example:
```
🚨 CRITICAL: Hydraulic Oil Temperature
Message: Oil temperature is excessively high (85°C)
Recommendation: Immediately inspect cooling system, 
                oil condition, filters, and heat exchanger
```

**What to do:**
1. Stop heavy drilling operations
2. Investigate cooling system
3. Check oil filter condition
4. Verify heat exchanger operation
5. Allow system to cool if needed

#### ⚠️ WARNING (Orange)

**Attention required - Performance degradation likely**

Example:
```
⚠️ WARNING: Hydraulic Pressure
Message: Pressure is below recommended operating range (175 bar)
Recommendation: Increase hydraulic pressure or inspect 
                the hydraulic pump and check for leakage
```

**What to do:**
1. Schedule maintenance within 24-48 hours
2. Implement recommended checks
3. Monitor parameter closely
4. Reduce operational intensity if possible

#### ℹ️ INFO (Blue)

**Informational - Optimization opportunity**

Example:
```
ℹ️ INFO: Overall Performance
Message: Machine is operating at excellent efficiency
Recommendation: Continue with regular maintenance schedule
```

**What to do:**
1. Maintain current operation
2. Follow routine maintenance
3. Document current settings for reference

---

## Optimization Recommendations

### Accessing Optimization Tab

1. Click the **"🔧 Optimization"** tab
2. View actionable recommendations for improvement

### Understanding Recommendations

Each recommendation shows:

**Current Value**
- Your current parameter setting

**Recommended Value**
- Suggested new setting for improvement

**Efficiency Gain**
- Percentage point improvement expected

**Expected New Efficiency**
- Projected efficiency after implementing change

### Example Optimization Scenario

```
Current Status:
- Efficiency: 63%
- Health Score: 72%
- Status: Fair

Recommendations:

1. 📈 Hydraulic Pressure
   Current: 190 bar
   Recommended: 250 bar
   Gain: +12%
   New Efficiency: 75%
   Action: Increase hydraulic pressure to approximately 250 bar

2. 🌡️ Oil Temperature
   Current: 68°C
   Recommended: 45°C
   Gain: +15%
   New Efficiency: 90%
   Action: Service cooling system and reduce ambient heat

3. ⚙️ Rotation Speed
   Current: 220 RPM
   Recommended: 350 RPM
   Gain: +8%
   New Efficiency: 98%
   Action: Increase drill rotation speed to 350 RPM
```

### Prioritized Implementation

**Recommended Order of Changes:**

1. **First:** Address temperature issues (fastest, safest)
2. **Second:** Adjust pressure settings (requires gradual increase)
3. **Third:** Modify RPM settings (requires motor adjustment)

### Expected Results

Following all recommendations in the example:
- Current efficiency: 63%
- After optimization: 98% ✅
- Improvement: +35 percentage points

---

## Generating Reports

### Accessing Reports Tab

1. Click the **"📄 Reports"** tab
2. Choose report format (PDF or Excel)

### PDF Report

**Contains:**
- Executive summary
- Performance metrics table
- Engineering calculations
- Diagnostics and alerts
- Professional formatting for printing

**To download:**
1. Click **"📥 Download PDF Report"** button
2. Choose location to save
3. Open in Adobe Reader or browser
4. Print if needed

**Use cases:**
- Maintenance documentation
- Regulatory compliance
- Equipment history
- Sharing with service technicians

### Excel Report

**Contains:**
- Summary information
- Input parameters
- Calculated values
- Diagnostic listing
- Formatted for further analysis

**To download:**
1. Click **"📊 Download Excel Report"** button
2. Choose location to save
3. Open in Excel, Google Sheets, etc.
4. Modify if needed

**Use cases:**
- Data analysis
- Trend comparison
- Sharing with analytics team
- Integration with other systems

---

## Tips & Best Practices

### Input Accuracy

**For Best Results:**

1. **Use Recent Readings**
   - Get values during current operation, not historical data
   - Check gauges are calibrated

2. **Record Conditions**
   - Note ambient temperature
   - Record loading conditions
   - Note material being drilled

3. **Consistent Measurement**
   - Same drill and location for comparisons
   - Similar operational duration
   - Comparable drilling conditions

### Regular Analysis Schedule

**Recommended Frequency:**

- **Daily**: Critical/high-use installations
- **Weekly**: Standard operating environments
- **Monthly**: Baseline performance tracking
- **Before/After**: Major maintenance

### Tracking Efficiency Trends

**Best Practices:**

1. Run same analysis weekly/monthly
2. Note any changes in readings
3. Look for gradual efficiency decline
4. Plan maintenance before critical issues

5. Document any interventions performed
6. Compare results before and after repairs

### Maintenance Planning

**Use diagnostics to:**

1. Prioritize maintenance tasks
2. Schedule preventive work
3. Plan spare parts procurement
4. Budget for equipment
5. Justify interventions to management

### Temperature Management

**Critical for efficiency:**

1. Check cooling system regularly
2. Change oil filters on schedule
3. Monitor ambient temperature effects
4. Ensure adequate ventilation
5. Consider supplemental cooling if needed

---

## Troubleshooting

### Application Won't Start

**Problem:** Browser doesn't open or "connection refused"

**Solutions:**
```bash
# Solution 1: Clear cache
streamlit cache clear
streamlit run app.py

# Solution 2: Use different port
streamlit run app.py --server.port 8502

# Solution 3: Check Python installation
python --version  # Should be 3.8+
```

### Analysis Produces Unexpected Results

**Problem:** Efficiency seems wrong or unrealistic

**Checklist:**
1. ✓ Verify input parameter values are correct
2. ✓ Check that values are in reasonable ranges
3. ✓ Confirm drill type selection is correct
4. ✓ Check for any input validation errors (red messages)

### Reports Won't Generate

**Problem:** "PDF generation not available" or "Excel not available"

**Solution:**
```bash
# Reinstall required packages
pip install reportlab openpyxl --force-reinstall
```

### History Data Missing

**Problem:** Previous analyses aren't showing

**Possible Causes:**
- History was cleared
- Browser cache was cleared
- Data file corrupted

**Recovery:**
- Check `data/analysis_history.json` exists
- If corrupted, export CSV backup and recreate

### Performance Issues

**Problem:** Application is slow

**Solutions:**
1. Close other applications to free RAM
2. Clear Streamlit cache: `streamlit cache clear`
3. Reduce browser tabs and extensions
4. Try different browser

### Port Already in Use

**Problem:** "Address already in use" error

**Solution:**
```bash
# Find and stop existing process
# Windows:
netstat -ano | findstr :8501
taskkill /PID <process_id> /F

# macOS/Linux:
lsof -i :8501
kill -9 <process_id>
```

---

## Frequently Asked Questions

**Q: What units does the software use?**
A: Metric - bar, L/min, RPM, °C, mm, kW, Newtons

**Q: Can I change the input ranges?**
A: Yes, edit the validation ranges in `analyzer.py` if needed

**Q: How often should I run analyses?**
A: Weekly for monitoring, daily for critical systems

**Q: Is my data backed up?**
A: Data is stored locally. Export CSV for backup

**Q: Can multiple users share data?**
A: Not currently - each installation has independent data

**Q: What's the maximum number of analyses stored?**
A: Last 100 analyses (older ones overwrite)

**Q: Can I export reports to other formats?**
A: Currently PDF and Excel; CSV export also available

**Q: How accurate are the calculations?**
A: Within ±5% for typical drilling conditions

---

## Support Resources

### Getting Help

1. Check the **README.md** for overview
2. Read **ENGINEER_GUIDE.md** for technical details
3. Review inline code comments
4. Check configuration in **config.py**

### Performance Baseline

For your specific equipment, establish baselines:

1. Record 3-5 analyses during optimal operation
2. Calculate average efficiency
3. Use as comparison point for future analyses
4. Alert if efficiency drops below 80% of baseline

---

## Quick Reference Card

### Normal Operating Parameters

```
Pressure:     220-280 bar (Good)
Flow Rate:    80-120 L/min (Good)
RPM:          200-350 (Good)
Temperature:  40-60°C (Optimal)
Piston Dia:   80-120 mm (Standard)
Bit Diameter: 100-200 mm (Typical)
```

### Key Thresholds

```
Efficiency:
  ✅ > 80%  : Acceptable
  ⚠️  70-80%: Action needed
  ❌ < 70% : Urgent attention

Health:
  ✅ > 75% : Healthy
  ⚠️  60-75%: Attention required
  ❌ < 60% : Maintenance required
```

---

**User Manual Version**: 1.0  
**Last Updated**: 2024  
**Status**: Ready for Use ✅

---

*For additional support, refer to the comprehensive documentation or contact your equipment manufacturer.*
