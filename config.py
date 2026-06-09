"""
Configuration Module
Advanced settings and customization for the Hydraulic Drill Analyzer
"""

# ============================================
# APPLICATION SETTINGS
# ============================================

APP_NAME = "Hydraulic Drill Machine Performance & Efficiency Analyzer"
APP_VERSION = "1.0"
APP_DESCRIPTION = "Professional mining engineering software for drilling machine analysis"

# ============================================
# DATA SETTINGS
# ============================================

DATA_RETENTION_DAYS = 365  # Keep analysis history for 1 year
MAX_HISTORY_ENTRIES = 100  # Maximum analyses to keep in memory
AUTO_SAVE_ENABLED = True
HISTORY_FILE = "data/analysis_history.json"
SETTINGS_FILE = "data/settings.json"

# ============================================
# PRESSURE RANGES (bar)
# ============================================

PRESSURE_RANGES = {
    "critical_low": 50,
    "poor": (120, 180),
    "fair": (180, 220),
    "good": (220, 280),
    "excellent": (280, 350),
    "critical_high": 350
}

# ============================================
# FLOW RATE RANGES (L/min)
# ============================================

FLOW_RATE_RANGES = {
    "poor": 50,
    "fair": (50, 80),
    "good": (80, 120),
    "excellent": (120, 180),
    "overload": 180
}

# ============================================
# RPM RANGES
# ============================================

RPM_RANGES = {
    "poor": 100,
    "fair": (100, 180),
    "good": (180, 300),
    "excellent": (300, 450),
    "excessive": 450
}

# ============================================
# TEMPERATURE RANGES (°C)
# ============================================

TEMPERATURE_RANGES = {
    "cold_start": 20,
    "good": (20, 40),
    "excellent": (40, 60),
    "fair": (60, 75),
    "poor": (75, 90),
    "critical": 90
}

# ============================================
# EFFICIENCY THRESHOLDS
# ============================================

EFFICIENCY_THRESHOLDS = {
    "excellent": 90,
    "very_good": 80,
    "good": 70,
    "fair": 60,
    "poor": 50,
    "critical": 0
}

# ============================================
# HEALTH SCORE THRESHOLDS
# ============================================

HEALTH_SCORE_THRESHOLDS = {
    "healthy": 90,
    "stable": 75,
    "attention_required": 60,
    "maintenance_required": 40,
    "critical_condition": 0
}

# ============================================
# COLOR CODES
# ============================================

COLOR_CODES = {
    "excellent": "#00aa00",      # Green
    "very_good": "#88cc00",      # Light Green
    "good": "#ffff00",           # Yellow
    "fair": "#ff8800",           # Orange
    "poor": "#ff6600",           # Orange-Red
    "critical": "#ff0000",       # Red
    "neutral": "#1f4788",        # Navy Blue
    "warning": "#ffa500",        # Warning Orange
    "info": "#0066cc"            # Info Blue
}

# ============================================
# WEIGHT DISTRIBUTION FOR DPI
# ============================================

DPI_WEIGHTS = {
    "pressure": 0.25,
    "flow_rate": 0.20,
    "rpm": 0.20,
    "temperature": 0.20,
    "piston_diameter": 0.05,
    "bit_diameter": 0.05,
    "drill_type_factor": 0.05
}

# ============================================
# HEALTH SCORE COMPONENTS
# ============================================

HEALTH_SCORE_WEIGHTS = {
    "pressure": 0.25,
    "flow_rate": 0.25,
    "rpm": 0.20,
    "temperature": 0.15,
    "efficiency": 0.15
}

# ============================================
# DIAGNOSTIC MESSAGE PRIORITY
# ============================================

DIAGNOSTIC_PRIORITY = {
    "CRITICAL": 1,
    "WARNING": 2,
    "INFO": 3
}

# ============================================
# REPORT SETTINGS
# ============================================

REPORT_SETTINGS = {
    "pdf": {
        "page_size": "letter",  # "letter" or "A4"
        "include_charts": True,
        "include_diagnostics": True,
        "include_recommendations": True
    },
    "excel": {
        "include_charts": False,
        "include_diagnostics": True,
        "max_diagnostics": 20
    },
    "csv": {
        "include_headers": True,
        "delimiter": ","
    }
}

# ============================================
# STREAMLIT UI SETTINGS
# ============================================

STREAMLIT_CONFIG = {
    "page_title": "Hydraulic Drill Analyzer",
    "page_icon": "⛏️",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
    "theme": {
        "primaryColor": "#1f4788",
        "backgroundColor": "#ffffff",
        "secondaryBackgroundColor": "#f0f0f0",
        "textColor": "#262730",
        "font": "sans serif"
    }
}

# ============================================
# CHART SETTINGS
# ============================================

CHART_SETTINGS = {
    "plot_bgcolor": "rgba(240, 240, 240, 0.5)",
    "paper_bgcolor": "rgba(255, 255, 255, 1)",
    "font_family": "Arial, sans-serif",
    "height": 400,
    "showlegend": True,
    "hovermode": "x unified"
}

# ============================================
# OPTIMIZATION THRESHOLDS
# ============================================

OPTIMIZATION_THRESHOLDS = {
    "min_pressure_improvement": 220,
    "max_temperature_improvement": 45,
    "min_flow_rate_improvement": 100,
    "min_rpm_improvement": 250
}

# ============================================
# EXPORT SETTINGS
# ============================================

EXPORT_SETTINGS = {
    "reports_dir": "reports",
    "data_dir": "data",
    "timestamp_format": "%Y%m%d_%H%M%S",
    "max_file_size_mb": 100
}

# ============================================
# UNITS CONFIGURATION
# ============================================

UNITS = {
    "pressure": "bar",
    "flow_rate": "L/min",
    "rpm": "RPM",
    "temperature": "°C",
    "power": "kW",
    "force": "N",
    "area": "mm²",
    "diameter": "mm"
}

# ============================================
# LANGUAGE SETTINGS
# ============================================

LANGUAGE = "en"  # English

# ============================================
# LOGGING SETTINGS
# ============================================

LOGGING_CONFIG = {
    "level": "INFO",  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": "logs/analyzer.log",
    "max_size_mb": 10,
    "backup_count": 5
}

# ============================================
# VALIDATION SETTINGS
# ============================================

VALIDATION_CONFIG = {
    "strict_mode": False,  # Enable strict validation
    "warn_on_edge_cases": True,
    "auto_correct_common_errors": True
}

# ============================================
# PERFORMANCE SETTINGS
# ============================================

PERFORMANCE_CONFIG = {
    "cache_enabled": True,
    "cache_ttl_seconds": 3600,  # 1 hour
    "max_concurrent_analyses": 10,
    "history_pagination_size": 50
}

# ============================================
# SECURITY SETTINGS
# ============================================

SECURITY_CONFIG = {
    "enable_data_encryption": False,
    "require_authentication": False,
    "session_timeout_minutes": 120,
    "audit_logging": True
}

# ============================================
# FEATURE FLAGS
# ============================================

FEATURES = {
    "real_time_analysis": True,
    "historical_tracking": True,
    "pdf_export": True,
    "excel_export": True,
    "csv_export": True,
    "dark_mode": True,
    "optimization_advisor": True,
    "predictive_analytics": False,  # Future feature
    "cloud_sync": False,  # Future feature
    "multi_language": False  # Future feature
}

# ============================================
# API SETTINGS
# ============================================

API_CONFIG = {
    "enable_rest_api": False,  # Future feature
    "api_port": 8000,
    "api_version": "v1"
}

# ============================================
# ADVANCED CALCULATION SETTINGS
# ============================================

CALCULATION_CONFIG = {
    "precision_decimal_places": 2,
    "use_scientific_notation": False,
    "round_method": "standard",  # standard, ceil, floor
    "safety_factor": 1.0
}

# ============================================
# DIAGNOSTIC RULES
# ============================================

DIAGNOSTIC_RULES = {
    "pressure_low_threshold": 180,
    "pressure_high_threshold": 350,
    "temperature_warning_threshold": 60,
    "temperature_critical_threshold": 75,
    "rpm_low_threshold": 100,
    "rpm_high_threshold": 500,
    "flow_rate_low_threshold": 50,
    "flow_rate_high_threshold": 250
}

# ============================================
# NOTIFICATION SETTINGS
# ============================================

NOTIFICATIONS = {
    "enabled": True,
    "show_critical_alerts": True,
    "show_warnings": True,
    "show_info": True,
    "auto_dismiss_seconds": 0  # 0 = manual dismiss
}

# ============================================
# DEFAULT VALUES
# ============================================

DEFAULT_VALUES = {
    "pressure": 250,
    "flow_rate": 120,
    "rpm": 300,
    "temperature": 45,
    "piston_diameter": 100,
    "bit_diameter": 150,
    "drill_type": "Hydraulic Drill Machine"
}

# ============================================
# END OF CONFIGURATION
# ============================================
