"""
Main Streamlit Application
Hydraulic Drill Machine Performance & Efficiency Analyzer
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import json
from analyzer import HydraulicDrillAnalyzer, DRILL_TYPES
from bit_analyzer import DrillBitAnalyzer, BIT_TYPES
from data_manager import DataManager
from report_generator import ReportGenerator

# Page configuration
st.set_page_config(
    page_title="Hydraulic Drill Analyzer",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None
if "bit_analysis_result" not in st.session_state:
    st.session_state.bit_analysis_result = None
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# Initialize managers
data_manager = DataManager()
report_generator = ReportGenerator()

# Custom CSS for better styling
def apply_custom_css():
    css = """
    <style>
    .main-header {
        font-size: 3em;
        color: #1f4788;
        text-align: center;
        margin-bottom: 20px;
        font-weight: bold;
    }
    .subheader {
        color: #1f4788;
        font-size: 1.5em;
        margin-bottom: 15px;
        font-weight: bold;
    }
    .metric-card {
        background-color: #f0f0f0;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 10px;
        border-left: 5px solid #1f4788;
    }
    .efficiency-excellent {
        background-color: #e8f5e9;
        border-left-color: #00aa00;
    }
    .efficiency-good {
        background-color: #fff3e0;
        border-left-color: #ffff00;
    }
    .efficiency-poor {
        background-color: #ffe0e0;
        border-left-color: #ff0000;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

apply_custom_css()

# Sidebar for theme and settings
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    theme = st.selectbox("Theme", ["Light", "Dark"], index=0)
    st.session_state.theme = theme.lower()
    
    st.divider()
    
    st.markdown("### 📊 Application Info")
    st.info("""
    **Hydraulic Drill Machine Performance & Efficiency Analyzer**
    
    Version: 1.0
    
    This application analyzes hydraulic drill machine performance and provides:
    - Real-time efficiency calculations
    - Machine health assessment
    - Intelligent diagnostics
    - Optimization recommendations
    - Professional reporting
    """)

# Main title
st.markdown('<div class="main-header">⛏️ HYDRAULIC DRILL MACHINE ANALYZER</div>', unsafe_allow_html=True)
st.markdown("---")

# Tab interface
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Analysis", 
    "📈 History", 
    "📋 Diagnostics",
    "🔧 Optimization",
    "📄 Reports",
    "🔬 Bit Life"
])

# ============================================
# TAB 1: ANALYSIS
# ============================================
with tab1:
    st.markdown('<div class="subheader">Machine Performance Analysis</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Drill type selection
        drill_type = st.selectbox(
            "Select Drill Type",
            list(DRILL_TYPES.keys()),
            help="Choose the hydraulic drill machine type"
        )
        
        st.markdown("### Input Parameters")
        
        col_input1, col_input2, col_input3 = st.columns(3)
        
        with col_input1:
            pressure = st.slider(
                "Hydraulic Pressure (bar)",
                min_value=50, max_value=500, value=250,
                step=10, help="Operating hydraulic pressure"
            )
            flow_rate = st.slider(
                "Flow Rate (L/min)",
                min_value=10, max_value=300, value=120,
                step=5, help="Hydraulic flow rate"
            )
            
        with col_input2:
            rpm = st.slider(
                "Rotation Speed (RPM)",
                min_value=10, max_value=1000, value=300,
                step=10, help="Drill rotation speed"
            )
            temperature = st.slider(
                "Oil Temperature (°C)",
                min_value=-20, max_value=120, value=45,
                step=2, help="Hydraulic oil temperature"
            )
            
        with col_input3:
            piston_diameter = st.slider(
                "Piston Diameter (mm)",
                min_value=5, max_value=200, value=100,
                step=5, help="Hydraulic piston diameter"
            )
            bit_diameter = st.slider(
                "Drill Bit Diameter (mm)",
                min_value=1, max_value=300, value=150,
                step=5, help="Drill bit diameter"
            )
        
        # Analyze button
        if st.button("🔍 ANALYZE MACHINE", use_container_width=True, type="primary"):
            try:
                analyzer = HydraulicDrillAnalyzer(drill_type)
                is_valid, errors = analyzer.validate_inputs(
                    pressure, flow_rate, rpm, temperature,
                    piston_diameter, bit_diameter
                )
                
                if not is_valid:
                    st.error("❌ Input Validation Errors:")
                    for error in errors:
                        st.error(f"• {error}")
                else:
                    # Run analysis
                    result = analyzer.run_analysis(
                        pressure, flow_rate, rpm, temperature,
                        piston_diameter, bit_diameter
                    )
                    
                    if result.get("valid"):
                        st.session_state.analysis_result = result
                        
                        # Auto-save to history
                        if data_manager.save_analysis(result):
                            st.success("✅ Analysis saved to history")
                    else:
                        st.error("Analysis failed")
                        
            except Exception as e:
                st.error(f"Error during analysis: {str(e)}")
    
    with col2:
        if st.session_state.analysis_result:
            result = st.session_state.analysis_result
            st.markdown("### Quick Summary")
            
            # Efficiency gauge
            efficiency = result.get("efficiency_percentage", 0)
            
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=efficiency,
                title={'text': "Efficiency (%)"},
                delta={'reference': 80},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': result.get("efficiency_color", "#1f4788")},
                    'steps': [
                        {'range': [0, 50], 'color': "#ffcccc"},
                        {'range': [50, 70], 'color': "#ffffcc"},
                        {'range': [70, 90], 'color': "#ccffcc"},
                        {'range': [90, 100], 'color': "#00aa00"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 90
                    }
                }
            ))
            fig_gauge.update_layout(height=300, margin=dict(l=0, r=0, t=30, b=0))
            st.plotly_chart(fig_gauge, use_container_width=True)
    
    # Display detailed results
    if st.session_state.analysis_result:
        result = st.session_state.analysis_result
        
        st.markdown("---")
        st.markdown("### 📊 Detailed Analysis Results")
        
        # Create metrics display
        col_metric1, col_metric2, col_metric3, col_metric4 = st.columns(4)
        
        with col_metric1:
            st.metric(
                "Efficiency",
                f"{result['efficiency_percentage']}%",
                delta=result['efficiency_category'],
                delta_color="off"
            )
        
        with col_metric2:
            st.metric(
                "Machine Health",
                f"{result['health_score']}%",
                delta=result['health_status'],
                delta_color="off"
            )
        
        with col_metric3:
            st.metric(
                "Hydraulic Power",
                f"{result['hydraulic_power_kw']} kW"
            )
        
        with col_metric4:
            st.metric(
                "Hydraulic Force",
                f"{result['hydraulic_force_n']:,.0f} N"
            )
        
        # Engineering values
        st.markdown("### ⚙️ Engineering Calculations")
        
        eng_col1, eng_col2, eng_col3 = st.columns(3)
        
        with eng_col1:
            st.info(f"""
            **Hydraulic Power**
            
            {result['hydraulic_power_kw']} kW
            """)
        
        with eng_col2:
            st.info(f"""
            **Piston Area**
            
            {result['piston_area_mm2']} mm²
            """)
        
        with eng_col3:
            st.info(f"""
            **Hydraulic Force**
            
            {result['hydraulic_force_n']:,.0f} N
            """)
        
        # Performance radar chart
        st.markdown("### 📡 Performance Profile")
        
        params = result['input_parameters']
        
        # Normalize parameters for radar chart
        pressure_norm = min(100, (params['pressure'] / 350) * 100)
        flow_norm = min(100, (params['flow_rate'] / 200) * 100)
        rpm_norm = min(100, (params['rpm'] / 500) * 100)
        temp_norm = min(100, (60 - abs(params['temperature'] - 50)) * 3.33)
        piston_norm = min(100, (params['piston_diameter'] / 150) * 100)
        bit_norm = min(100, (params['bit_diameter'] / 250) * 100)
        
        fig_radar = go.Figure(data=go.Scatterpolar(
            r=[pressure_norm, flow_norm, rpm_norm, temp_norm, piston_norm, bit_norm],
            theta=['Pressure', 'Flow Rate', 'RPM', 'Temperature', 'Piston Size', 'Bit Size'],
            fill='toself',
            name='Performance'
        ))
        
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            height=400
        )
        
        st.plotly_chart(fig_radar, use_container_width=True)

# ============================================
# TAB 2: HISTORY
# ============================================
with tab2:
    st.markdown('<div class="subheader">Analysis History</div>', unsafe_allow_html=True)
    
    history = data_manager.load_history()
    
    if not history:
        st.info("No analysis history available. Run an analysis first!")
    else:
        # Display statistics
        col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
        
        with col_stat1:
            st.metric("Total Analyses", len(history))
        
        with col_stat2:
            avg_efficiency = sum(a.get('efficiency_percentage', 0) for a in history) / len(history)
            st.metric("Avg Efficiency", f"{avg_efficiency:.1f}%")
        
        with col_stat3:
            avg_health = sum(a.get('health_score', 0) for a in history) / len(history)
            st.metric("Avg Health Score", f"{avg_health:.1f}%")
        
        with col_stat4:
            drill_types = set(a.get('drill_type', '') for a in history)
            st.metric("Drill Types Analyzed", len(drill_types))
        
        st.divider()
        
        # Trend analysis
        st.markdown("### 📈 Efficiency Trend")
        
        df_history = pd.DataFrame([
            {
                'timestamp': a.get('timestamp', ''),
                'efficiency': a.get('efficiency_percentage', 0),
                'health': a.get('health_score', 0),
                'drill_type': a.get('drill_type', '')
            }
            for a in history[-30:]  # Last 30 analyses
        ])
        
        df_history['timestamp'] = pd.to_datetime(df_history['timestamp'])
        
        fig_trend = px.line(
            df_history,
            x='timestamp',
            y=['efficiency', 'health'],
            title='Efficiency and Health Trend',
            labels={'value': 'Score (%)', 'timestamp': 'Time'}
        )
        
        st.plotly_chart(fig_trend, use_container_width=True)
        
        # Drill type distribution
        st.markdown("### 🏗️ Drill Type Distribution")
        
        col_dist1, col_dist2 = st.columns(2)
        
        with col_dist1:
            drill_counts = {}
            for a in history:
                dt = a.get('drill_type', 'Unknown')
                drill_counts[dt] = drill_counts.get(dt, 0) + 1
            
            fig_dist = px.pie(
                values=list(drill_counts.values()),
                names=list(drill_counts.keys()),
                title="Analyses by Drill Type"
            )
            st.plotly_chart(fig_dist, use_container_width=True)
        
        with col_dist2:
            # Efficiency distribution
            efficiency_data = [a.get('efficiency_percentage', 0) for a in history]
            fig_hist = px.histogram(
                x=efficiency_data,
                nbins=20,
                title="Efficiency Distribution",
                labels={'x': 'Efficiency (%)', 'count': 'Frequency'}
            )
            st.plotly_chart(fig_hist, use_container_width=True)
        
        st.divider()
        
        # Detailed history table
        st.markdown("### 📋 Detailed History")
        
        display_cols = ['timestamp', 'drill_type', 'efficiency_percentage', 'health_score', 'efficiency_category']
        df_display = pd.DataFrame([
            {col: a.get(col, '') for col in display_cols}
            for a in reversed(history[-50:])  # Last 50 in reverse chronological order
        ])
        
        st.dataframe(df_display, use_container_width=True, hide_index=True)
        
        # Export options
        st.markdown("### 💾 Export Options")
        col_export1, col_export2, col_export3 = st.columns(3)
        
        with col_export1:
            if st.button("📥 Export to CSV", use_container_width=True):
                data_manager.export_to_csv()
                st.success("✅ Exported to CSV!")
        
        with col_export2:
            if st.button("🗑️ Clear History", use_container_width=True):
                if st.session_state.get("confirm_clear"):
                    data_manager.clear_history()
                    st.success("✅ History cleared!")
                    st.session_state.confirm_clear = False
                else:
                    st.session_state.confirm_clear = True
                    st.warning("Click again to confirm deletion")

# ============================================
# TAB 3: DIAGNOSTICS
# ============================================
with tab3:
    st.markdown('<div class="subheader">System Diagnostics</div>', unsafe_allow_html=True)
    
    if not st.session_state.analysis_result:
        st.info("No analysis available. Run an analysis first to see diagnostics!")
    else:
        result = st.session_state.analysis_result
        diagnostics = result.get('diagnostics', [])
        
        if not diagnostics:
            st.success("✅ All systems operating normally!")
        else:
            # Group diagnostics by type
            critical = [d for d in diagnostics if d.get('type') == 'CRITICAL']
            warnings = [d for d in diagnostics if d.get('type') == 'WARNING']
            info = [d for d in diagnostics if d.get('type') == 'INFO']
            
            # Display summary
            col_diag1, col_diag2, col_diag3 = st.columns(3)
            
            with col_diag1:
                st.metric("🚨 Critical", len(critical))
            
            with col_diag2:
                st.metric("⚠️ Warnings", len(warnings))
            
            with col_diag3:
                st.metric("ℹ️ Info", len(info))
            
            st.divider()
            
            # Critical Issues
            if critical:
                st.markdown("### 🚨 CRITICAL ISSUES")
                for diag in critical:
                    with st.container():
                        col_type, col_content = st.columns([1, 9])
                        with col_type:
                            st.error("CRITICAL")
                        with col_content:
                            st.markdown(f"**{diag.get('parameter')}**")
                            st.write(diag.get('message'))
                            st.warning(f"⚠️ {diag.get('recommendation')}")
                        st.divider()
            
            # Warnings
            if warnings:
                st.markdown("### ⚠️ WARNINGS")
                for diag in warnings:
                    with st.container():
                        col_type, col_content = st.columns([1, 9])
                        with col_type:
                            st.warning("WARNING")
                        with col_content:
                            st.markdown(f"**{diag.get('parameter')}**")
                            st.write(diag.get('message'))
                            st.info(f"💡 {diag.get('recommendation')}")
                        st.divider()
            
            # Info
            if info:
                st.markdown("### ℹ️ INFORMATION")
                for diag in info:
                    with st.container():
                        col_type, col_content = st.columns([1, 9])
                        with col_type:
                            st.info("INFO")
                        with col_content:
                            st.markdown(f"**{diag.get('parameter')}**")
                            st.write(diag.get('message'))
                            st.success(f"✓ {diag.get('recommendation')}")
                        st.divider()

# ============================================
# TAB 4: OPTIMIZATION
# ============================================
with tab4:
    st.markdown('<div class="subheader">Optimization Recommendations</div>', unsafe_allow_html=True)
    
    if not st.session_state.analysis_result:
        st.info("No analysis available. Run an analysis first to see optimization recommendations!")
    else:
        result = st.session_state.analysis_result
        
        # Create analyzer to get recommendations
        analyzer = HydraulicDrillAnalyzer(result['drill_type'])
        recommendations = analyzer.get_optimization_recommendations(result)
        
        if not recommendations:
            st.success("✅ Machine is operating at optimal efficiency!")
        else:
            st.markdown(f"""
            ### Current Efficiency: {result['efficiency_percentage']}%
            
            The following optimizations could improve your machine's performance:
            """)
            
            for i, rec in enumerate(recommendations, 1):
                with st.container():
                    col_num, col_content = st.columns([1, 9])
                    
                    with col_num:
                        st.markdown(f"### {i}")
                    
                    with col_content:
                        st.markdown(f"### {rec.get('category')}")
                        
                        col_opt1, col_opt2, col_opt3 = st.columns(3)
                        
                        with col_opt1:
                            st.metric(
                                "Current Value",
                                f"{rec.get('current_value')}",
                                delta=None
                            )
                        
                        with col_opt2:
                            st.metric(
                                "Recommended Value",
                                f"{rec.get('recommended_value')}"
                            )
                        
                        with col_opt3:
                            st.metric(
                                "Efficiency Gain",
                                f"+{rec.get('estimated_improvement')}%",
                                delta_color="off"
                            )
                        
                        st.info(f"**Action:** {rec.get('action')}")
                        st.success(f"**Expected New Efficiency:** {rec.get('new_efficiency')}%")
                    
                    st.divider()

# ============================================
# TAB 5: REPORTS
# ============================================
with tab5:
    st.markdown('<div class="subheader">Report Generation</div>', unsafe_allow_html=True)
    
    if not st.session_state.analysis_result:
        st.info("No analysis available. Run an analysis first to generate reports!")
    else:
        result = st.session_state.analysis_result
        
        st.markdown("### 📄 Generate Professional Reports")
        
        col_pdf, col_excel = st.columns(2)
        
        with col_pdf:
            st.markdown("#### PDF Report")
            st.write("Generate a professional PDF report with all analysis details, charts, and recommendations.")
            
            if st.button("📥 Download PDF Report", use_container_width=True):
                pdf_path = report_generator.generate_pdf_report(result)
                if pdf_path.endswith('.pdf'):
                    with open(pdf_path, 'rb') as f:
                        st.download_button(
                            label="📄 Click to download PDF",
                            data=f.read(),
                            file_name=pdf_path.split('\\')[-1],
                            mime="application/pdf",
                            use_container_width=True
                        )
                else:
                    st.error(pdf_path)
        
        with col_excel:
            st.markdown("#### Excel Report")
            st.write("Generate an Excel spreadsheet with all analysis data and calculations.")
            
            if st.button("📊 Download Excel Report", use_container_width=True):
                excel_path = report_generator.generate_excel_report(result)
                if excel_path.endswith('.xlsx'):
                    with open(excel_path, 'rb') as f:
                        st.download_button(
                            label="📊 Click to download Excel",
                            data=f.read(),
                            file_name=excel_path.split('\\')[-1],
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            use_container_width=True
                        )
                else:
                    st.error(excel_path)
        
        st.divider()
        
        st.markdown("### 📋 Report Preview")
        
        # Create a summary view
        st.markdown(f"""
        #### Analysis Summary
        
        | Parameter | Value |
        |-----------|-------|
        | **Drill Type** | {result['drill_type']} |
        | **Efficiency** | {result['efficiency_percentage']}% ({result['efficiency_category']}) |
        | **Machine Health** | {result['health_score']}% ({result['health_status']}) |
        | **Hydraulic Power** | {result['hydraulic_power_kw']} kW |
        | **Hydraulic Force** | {result['hydraulic_force_n']:,.0f} N |
        | **Report Generated** | {result['timestamp']} |
        
        #### Input Parameters
        
        | Parameter | Value |
        |-----------|-------|
        | Pressure | {result['input_parameters']['pressure']} bar |
        | Flow Rate | {result['input_parameters']['flow_rate']} L/min |
        | RPM | {result['input_parameters']['rpm']} |
        | Temperature | {result['input_parameters']['temperature']}°C |
        | Piston Diameter | {result['input_parameters']['piston_diameter']} mm |
        | Drill Bit Diameter | {result['input_parameters']['bit_diameter']} mm |
        """)

# ============================================
# TAB 6: BIT LIFE ANALYSIS
# ============================================
with tab6:
    st.markdown('<div class="subheader">Drill Bit Wear & Life Analysis</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Bit type selection
        bit_type = st.selectbox(
            "Select Drill Bit Type",
            list(BIT_TYPES.keys()),
            help="Choose the drill bit type",
            key="bit_type_select"
        )
        
        st.markdown("### Operating Parameters")
        
        col_bit1, col_bit2, col_bit3 = st.columns(3)
        
        with col_bit1:
            bit_pressure = st.slider(
                "Hydraulic Pressure (bar)",
                min_value=50, max_value=500, value=250,
                step=10, help="Operating hydraulic pressure", key="bit_pressure"
            )
            bit_flow_rate = st.slider(
                "Flow Rate (L/min)",
                min_value=10, max_value=300, value=120,
                step=5, help="Hydraulic flow rate", key="bit_flow"
            )
            
        with col_bit2:
            bit_rpm = st.slider(
                "Rotation Speed (RPM)",
                min_value=10, max_value=1000, value=300,
                step=10, help="Drill rotation speed", key="bit_rpm"
            )
            bit_temperature = st.slider(
                "Oil Temperature (°C)",
                min_value=-20, max_value=120, value=45,
                step=2, help="Hydraulic oil temperature", key="bit_temp"
            )
            
        with col_bit3:
            bit_piston_diameter = st.slider(
                "Piston Diameter (mm)",
                min_value=5, max_value=200, value=100,
                step=5, help="Hydraulic piston diameter", key="bit_piston"
            )
            bit_bit_diameter = st.slider(
                "Drill Bit Diameter (mm)",
                min_value=1, max_value=300, value=150,
                step=5, help="Drill bit diameter", key="bit_bit_dia"
            )
        
        bit_efficiency = st.slider(
            "Machine Efficiency (%)",
            min_value=0, max_value=100, value=80,
            step=5, help="Current machine efficiency from previous analysis", key="bit_eff"
        )
        
        # Analyze bit button
        if st.button("🔬 ANALYZE BIT LIFE", use_container_width=True, type="primary", key="analyze_bit"):
            try:
                bit_analyzer = DrillBitAnalyzer(bit_type)
                is_valid, errors = bit_analyzer.validate_inputs(
                    bit_pressure, bit_flow_rate, bit_rpm, bit_temperature,
                    bit_piston_diameter, bit_bit_diameter, bit_efficiency
                )
                
                if not is_valid:
                    st.error("❌ Input Validation Errors:")
                    for error in errors:
                        st.error(f"• {error}")
                else:
                    # Run bit analysis
                    bit_result = bit_analyzer.run_analysis(
                        bit_pressure, bit_flow_rate, bit_rpm, bit_temperature,
                        bit_piston_diameter, bit_bit_diameter, bit_efficiency
                    )
                    
                    if bit_result.get("valid"):
                        st.session_state.bit_analysis_result = bit_result
                        st.success("✅ Bit life analysis completed")
                    else:
                        st.error("Analysis failed")
                        
            except Exception as e:
                st.error(f"Error during bit analysis: {str(e)}")
    
    with col2:
        if st.session_state.get("bit_analysis_result"):
            result = st.session_state.bit_analysis_result
            st.markdown("### Bit Status")
            
            # Wear gauge
            wear = result.get("wear_percentage", 0)
            
            fig_wear = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=wear,
                title={'text': "Bit Wear (%)"},
                delta={'reference': 40},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': result.get("wear_color", "#1f4788")},
                    'steps': [
                        {'range': [0, 20], 'color': "#ccffcc"},
                        {'range': [20, 40], 'color': "#ffffcc"},
                        {'range': [40, 60], 'color': "#ffcccc"},
                        {'range': [60, 100], 'color': "#ff9999"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 80
                    }
                }
            ))
            fig_wear.update_layout(height=300, margin=dict(l=0, r=0, t=30, b=0))
            st.plotly_chart(fig_wear, use_container_width=True)
    
    # Display detailed results
    if st.session_state.get("bit_analysis_result"):
        result = st.session_state.bit_analysis_result
        
        st.markdown("---")
        st.markdown("### 📊 Bit Life Analysis Results")
        
        # Create metrics display
        col_metric1, col_metric2, col_metric3, col_metric4 = st.columns(4)
        
        with col_metric1:
            st.metric(
                "Bit Wear",
                f"{result['wear_percentage']}%",
                delta=result['wear_category'],
                delta_color="off"
            )
        
        with col_metric2:
            st.metric(
                "Remaining Life",
                f"{result['remaining_life_percentage']}%",
                delta=result['bit_health_status'],
                delta_color="off"
            )
        
        with col_metric3:
            st.metric(
                "Operating Hours",
                f"{result['remaining_operating_hours']} hrs"
            )
        
        with col_metric4:
            st.metric(
                "Failure Risk",
                result['failure_risk_level'],
                delta=result['replacement_priority'],
                delta_color="off"
            )
        
        # Bit information
        st.markdown("### ℹ️ Drill Bit Information")
        
        info_col1, info_col2, info_col3 = st.columns(3)
        
        with info_col1:
            st.info(f"""
            **Bit Type**
            
            {result['bit_type']}
            
            **Material**
            
            {result['bit_material']}
            """)
        
        with info_col2:
            st.info(f"""
            **Typical Life**
            
            {result['typical_life_hours']} hours
            
            **Average**
            
            {result['typical_life_average']:.0f} hours
            """)
        
        with info_col3:
            # Color-code the replacement recommendation
            priority = result['replacement_priority']
            if priority == "Critical":
                color = "🔴"
            elif priority == "High":
                color = "🟠"
            elif priority == "Medium":
                color = "🟡"
            else:
                color = "🟢"
            
            st.warning(f"""
            **Replacement Status**
            
            {color} {result['replacement_priority']}
            
            **Action**
            
            {result['replacement_recommendation'][:50]}...
            """)
        
        # Detailed metrics
        st.markdown("### 📈 Detailed Metrics")
        
        detail_col1, detail_col2, detail_col3, detail_col4 = st.columns(4)
        
        with detail_col1:
            st.metric("Wear Percentage", f"{result['wear_percentage']}%")
        
        with detail_col2:
            st.metric("Remaining Life %", f"{result['remaining_life_percentage']}%")
        
        with detail_col3:
            st.metric("Operating Hours", f"{result['remaining_operating_hours']:.1f}")
        
        with detail_col4:
            st.metric("Health Status", result['bit_health_status'])
        
        # Full replacement recommendation
        st.markdown("### 🔔 Replacement Recommendation")
        
        if result['replacement_priority'] == "Critical":
            st.error(f"🚨 {result['replacement_recommendation']}")
        elif result['replacement_priority'] == "High":
            st.warning(f"⚠️ {result['replacement_recommendation']}")
        elif result['replacement_priority'] == "Medium":
            st.info(f"💡 {result['replacement_recommendation']}")
        else:
            st.success(f"✅ {result['replacement_recommendation']}")
        
        # Diagnostics
        diagnostics = result.get('diagnostics', [])
        if diagnostics:
            st.markdown("### 🔍 Bit Wear Diagnostics")
            
            for diag in diagnostics[:5]:  # Show first 5 diagnostics
                diag_type = diag.get('type', 'INFO')
                param = diag.get('parameter', '')
                msg = diag.get('message', '')
                rec = diag.get('recommendation', '')
                wear_impact = diag.get('wear_impact', 'N/A')
                
                with st.container():
                    if diag_type == "WARNING":
                        st.warning(f"**⚠️ {param}** | Wear Impact: {wear_impact}")
                        st.write(msg)
                        st.caption(f"👉 {rec}")
                    else:
                        st.info(f"**ℹ️ {param}** | Wear Impact: {wear_impact}")
                        st.write(msg)
                        st.caption(f"👉 {rec}")
                    st.divider()
        
        # Life Extension Recommendations
        recommendations = result.get('life_extension_recommendations', [])
        if recommendations:
            st.markdown("### 🚀 Life Extension Recommendations")
            
            for i, rec in enumerate(recommendations, 1):
                with st.container():
                    col_num, col_content = st.columns([1, 9])
                    
                    with col_num:
                        st.markdown(f"### {i}")
                    
                    with col_content:
                        st.markdown(f"### {rec.get('category')}")
                        
                        col_ext1, col_ext2, col_ext3 = st.columns(3)
                        
                        with col_ext1:
                            st.metric(
                                "Current Value",
                                f"{rec.get('current_value'):.0f}",
                                delta=None
                            )
                        
                        with col_ext2:
                            st.metric(
                                "Recommended Value",
                                f"{rec.get('recommended_value'):.0f}"
                            )
                        
                        with col_ext3:
                            st.metric(
                                "Hours Extension",
                                f"+{rec.get('hours_extension'):.0f}",
                                delta_color="off"
                            )
                        
                        st.info(f"**Action:** {rec.get('action')}")
                        
                        ext_pct = rec.get('percentage_improvement', 0)
                        if ext_pct > 0:
                            st.success(f"**Potential Improvement:** {ext_pct:.1f}% increase in bit life")
                    
                    st.divider()
        
        # Extended Life Prediction
        extended_prediction = result.get('extended_life_prediction', {})
        if extended_prediction.get('total_extension_hours', 0) > 0:
            st.markdown("### 📊 Extended Life Prediction")
            st.success(f"""
            {extended_prediction.get('message')}
            
            **Total Possible Extension:** {extended_prediction.get('total_extension_hours'):.0f} hours 
            ({extended_prediction.get('total_extension_percentage'):.1f}% improvement)
            """)
        
        # Failure Time Prediction
        st.markdown("### ⏰ Failure Time Prediction")
        st.warning(extended_prediction.get('message', result.get('failure_time_prediction', 'Unknown')))

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p><strong>Hydraulic Drill Machine Performance & Efficiency Analyzer</strong></p>
    <p>Version 1.0 | Professional Mining Engineering Software</p>
    <p>© 2024 All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)
