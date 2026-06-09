"""
Hydraulic Drill Machine Performance & Efficiency Analyzer
Core Engineering Calculations Module
Version 1.0
Author: Mining Engineering Software Suite
"""

import math
from typing import Dict, List, Tuple
from dataclasses import dataclass
from datetime import datetime


@dataclass
class DrillSpecification:
    """Drill type specifications with operating parameters"""
    name: str
    min_pressure: int
    max_pressure: int
    min_flow_rate: int
    max_flow_rate: int
    min_rpm: int
    max_rpm: int
    optimal_temp_min: int
    optimal_temp_max: int
    type_factor: float


# Drill Type Database
DRILL_TYPES = {
    "Hydraulic Drill Machine": DrillSpecification(
        name="Hydraulic Drill Machine",
        min_pressure=180, max_pressure=350,
        min_flow_rate=50, max_flow_rate=180,
        min_rpm=100, max_rpm=450,
        optimal_temp_min=20, optimal_temp_max=60,
        type_factor=1.0
    ),
    "Underground Mining Jumbo Drill": DrillSpecification(
        name="Underground Mining Jumbo Drill",
        min_pressure=220, max_pressure=350,
        min_flow_rate=80, max_flow_rate=200,
        min_rpm=150, max_rpm=500,
        optimal_temp_min=25, optimal_temp_max=65,
        type_factor=1.1
    ),
    "Heavy-Duty Rock Drill": DrillSpecification(
        name="Heavy-Duty Rock Drill",
        min_pressure=280, max_pressure=400,
        min_flow_rate=100, max_flow_rate=220,
        min_rpm=180, max_rpm=550,
        optimal_temp_min=30, optimal_temp_max=70,
        type_factor=1.2
    ),
    "Rotary Drill": DrillSpecification(
        name="Rotary Drill",
        min_pressure=150, max_pressure=300,
        min_flow_rate=60, max_flow_rate=150,
        min_rpm=200, max_rpm=400,
        optimal_temp_min=20, optimal_temp_max=55,
        type_factor=0.9
    ),
    "Blast Hole Production Drill": DrillSpecification(
        name="Blast Hole Production Drill",
        min_pressure=200, max_pressure=350,
        min_flow_rate=70, max_flow_rate=180,
        min_rpm=120, max_rpm=480,
        optimal_temp_min=25, optimal_temp_max=65,
        type_factor=1.05
    ),
    "Light Drilling Machine": DrillSpecification(
        name="Light Drilling Machine",
        min_pressure=100, max_pressure=220,
        min_flow_rate=30, max_flow_rate=100,
        min_rpm=80, max_rpm=350,
        optimal_temp_min=15, optimal_temp_max=50,
        type_factor=0.7
    ),
    "Quarry Drilling Machine": DrillSpecification(
        name="Quarry Drilling Machine",
        min_pressure=180, max_pressure=320,
        min_flow_rate=50, max_flow_rate=160,
        min_rpm=100, max_rpm=420,
        optimal_temp_min=20, optimal_temp_max=60,
        type_factor=0.95
    ),
    "Core Drilling Machine": DrillSpecification(
        name="Core Drilling Machine",
        min_pressure=120, max_pressure=280,
        min_flow_rate=40, max_flow_rate=120,
        min_rpm=60, max_rpm=300,
        optimal_temp_min=20, optimal_temp_max=55,
        type_factor=0.85
    ),
    "Diamond Core Drill": DrillSpecification(
        name="Diamond Core Drill",
        min_pressure=100, max_pressure=250,
        min_flow_rate=30, max_flow_rate=100,
        min_rpm=50, max_rpm=250,
        optimal_temp_min=18, optimal_temp_max=50,
        type_factor=0.8
    ),
    "Exploration Drill": DrillSpecification(
        name="Exploration Drill",
        min_pressure=140, max_pressure=300,
        min_flow_rate=45, max_flow_rate=130,
        min_rpm=90, max_rpm=380,
        optimal_temp_min=20, optimal_temp_max=55,
        type_factor=0.9
    ),
    "DTH (Down-The-Hole) Drill": DrillSpecification(
        name="DTH (Down-The-Hole) Drill",
        min_pressure=220, max_pressure=400,
        min_flow_rate=100, max_flow_rate=250,
        min_rpm=200, max_rpm=600,
        optimal_temp_min=25, optimal_temp_max=70,
        type_factor=1.15
    ),
    "Top Hammer Drill": DrillSpecification(
        name="Top Hammer Drill",
        min_pressure=150, max_pressure=320,
        min_flow_rate=50, max_flow_rate=150,
        min_rpm=100, max_rpm=400,
        optimal_temp_min=20, optimal_temp_max=60,
        type_factor=1.0
    ),
}


class HydraulicDrillAnalyzer:
    """Main analyzer class for hydraulic drill machine performance"""

    def __init__(self, drill_type: str):
        self.drill_type = drill_type
        self.spec = DRILL_TYPES.get(drill_type)
        if not self.spec:
            raise ValueError(f"Invalid drill type: {drill_type}")

    def validate_inputs(self, pressure: float, flow_rate: float, rpm: float,
                       temperature: float, piston_diameter: float,
                       bit_diameter: float) -> Tuple[bool, List[str]]:
        """Validate all input parameters"""
        errors = []

        # Pressure validation
        if not (50 <= pressure <= 500):
            errors.append("Pressure must be between 50-500 bar")

        # Flow rate validation
        if not (10 <= flow_rate <= 300):
            errors.append("Flow rate must be between 10-300 L/min")

        # RPM validation
        if not (10 <= rpm <= 1000):
            errors.append("RPM must be between 10-1000")

        # Temperature validation
        if not (-20 <= temperature <= 120):
            errors.append("Temperature must be between -20 and 120°C")

        # Piston diameter validation
        if not (5 <= piston_diameter <= 200):
            errors.append("Piston diameter must be between 5-200 mm")

        # Bit diameter validation
        if not (1 <= bit_diameter <= 300):
            errors.append("Drill bit diameter must be between 1-300 mm")

        return len(errors) == 0, errors

    def calculate_hydraulic_power(self, pressure: float, flow_rate: float) -> float:
        """
        Calculate hydraulic power in kW
        Formula: Power (kW) = (Pressure × Flow Rate) / 600
        """
        return (pressure * flow_rate) / 600

    def calculate_piston_area(self, piston_diameter: float) -> float:
        """
        Calculate piston area in mm²
        Formula: Area = π × (d²) / 4
        """
        diameter_mm = piston_diameter
        area = math.pi * (diameter_mm ** 2) / 4
        return area

    def calculate_hydraulic_force(self, pressure: float, piston_diameter: float) -> float:
        """
        Calculate hydraulic force in Newtons
        Formula: Force (N) = Pressure (Pa) × Piston Area (m²)
        """
        # Convert pressure from bar to Pa (1 bar = 100,000 Pa)
        pressure_pa = pressure * 100000

        # Convert piston diameter from mm to meters
        diameter_m = piston_diameter / 1000

        # Calculate area in m²
        area_m2 = math.pi * (diameter_m ** 2) / 4

        # Calculate force
        force = pressure_pa * area_m2

        return force

    def calculate_drill_performance_index(self, pressure: float, flow_rate: float,
                                         rpm: float, temperature: float,
                                         piston_diameter: float,
                                         bit_diameter: float) -> float:
        """
        Calculate Drill Performance Index (DPI) using weighted scoring
        Weight distribution:
        - Pressure: 25%
        - Flow Rate: 20%
        - RPM: 20%
        - Temperature: 20%
        - Piston Diameter: 5%
        - Bit Diameter: 5%
        - Drill Type Factor: 5%
        """

        # Normalize each parameter (0-100)
        pressure_score = self._normalize_parameter(pressure, 100, 400)
        flow_rate_score = self._normalize_parameter(flow_rate, 30, 250)
        rpm_score = self._normalize_parameter(rpm, 50, 700)
        temp_score = self._normalize_temperature(temperature)
        piston_score = self._normalize_parameter(piston_diameter, 10, 150)
        bit_score = self._normalize_parameter(bit_diameter, 10, 250)
        type_factor_score = self.spec.type_factor * 100

        # Apply weights
        dpi = (
            pressure_score * 0.25 +
            flow_rate_score * 0.20 +
            rpm_score * 0.20 +
            temp_score * 0.20 +
            piston_score * 0.05 +
            bit_score * 0.05 +
            type_factor_score * 0.05
        )

        return min(100, max(0, dpi))

    def _normalize_parameter(self, value: float, min_val: float, max_val: float) -> float:
        """Normalize a parameter to 0-100 scale"""
        if value < min_val:
            return (value / min_val) * 50  # Below min = 0-50
        elif value > max_val:
            return 50 + ((max_val / value) * 50)  # Above max = 50-100
        else:
            return 50 + ((value - min_val) / (max_val - min_val)) * 50

    def _normalize_temperature(self, temperature: float) -> float:
        """Normalize temperature to 0-100 scale"""
        optimal_min = self.spec.optimal_temp_min
        optimal_max = self.spec.optimal_temp_max
        optimal_mid = (optimal_min + optimal_max) / 2

        if optimal_min <= temperature <= optimal_max:
            return 100
        elif temperature < optimal_min:
            return max(0, 100 - ((optimal_min - temperature) * 5))
        else:
            return max(0, 100 - ((temperature - optimal_max) * 5))

    def get_efficiency_category(self, efficiency: float) -> str:
        """Get efficiency category from percentage"""
        if efficiency >= 90:
            return "Excellent"
        elif efficiency >= 80:
            return "Very Good"
        elif efficiency >= 70:
            return "Good"
        elif efficiency >= 60:
            return "Fair"
        elif efficiency >= 50:
            return "Poor"
        else:
            return "Critical"

    def get_efficiency_color(self, efficiency: float) -> str:
        """Get color code for efficiency"""
        if efficiency >= 90:
            return "#00AA00"  # Green
        elif efficiency >= 80:
            return "#88CC00"  # Light Green
        elif efficiency >= 70:
            return "#FFFF00"  # Yellow
        elif efficiency >= 60:
            return "#FF8800"  # Orange
        elif efficiency >= 50:
            return "#FF6600"  # Orange-Red
        else:
            return "#FF0000"  # Red

    def get_health_status(self, health_score: float) -> str:
        """Get machine health status"""
        if health_score >= 90:
            return "Healthy"
        elif health_score >= 75:
            return "Stable"
        elif health_score >= 60:
            return "Attention Required"
        elif health_score >= 40:
            return "Maintenance Required"
        else:
            return "Critical Condition"

    def run_analysis(self, pressure: float, flow_rate: float, rpm: float,
                    temperature: float, piston_diameter: float,
                    bit_diameter: float) -> Dict:
        """Run complete analysis and return all results"""

        # Validate inputs
        is_valid, errors = self.validate_inputs(pressure, flow_rate, rpm,
                                                 temperature, piston_diameter,
                                                 bit_diameter)
        if not is_valid:
            return {"valid": False, "errors": errors}

        # Calculate engineering parameters
        hydraulic_power = self.calculate_hydraulic_power(pressure, flow_rate)
        piston_area = self.calculate_piston_area(piston_diameter)
        hydraulic_force = self.calculate_hydraulic_force(pressure, piston_diameter)
        dpi = self.calculate_drill_performance_index(pressure, flow_rate, rpm,
                                                      temperature, piston_diameter,
                                                      bit_diameter)

        # Calculate efficiency (use DPI as base)
        efficiency = dpi

        # Perform diagnostics
        diagnostics = self.perform_diagnostics(pressure, flow_rate, rpm,
                                              temperature, piston_diameter,
                                              bit_diameter, efficiency)

        # Calculate health score
        health_score = self._calculate_health_score(pressure, flow_rate, rpm,
                                                    temperature, efficiency)

        results = {
            "valid": True,
            "drill_type": self.drill_type,
            "hydraulic_power_kw": round(hydraulic_power, 2),
            "piston_area_mm2": round(piston_area, 2),
            "hydraulic_force_n": round(hydraulic_force, 2),
            "efficiency_percentage": round(efficiency, 2),
            "efficiency_category": self.get_efficiency_category(efficiency),
            "efficiency_color": self.get_efficiency_color(efficiency),
            "health_score": round(health_score, 2),
            "health_status": self.get_health_status(health_score),
            "diagnostics": diagnostics,
            "input_parameters": {
                "pressure": pressure,
                "flow_rate": flow_rate,
                "rpm": rpm,
                "temperature": temperature,
                "piston_diameter": piston_diameter,
                "bit_diameter": bit_diameter
            },
            "timestamp": datetime.now().isoformat()
        }

        return results

    def perform_diagnostics(self, pressure: float, flow_rate: float, rpm: float,
                           temperature: float, piston_diameter: float,
                           bit_diameter: float, efficiency: float) -> List[Dict]:
        """Perform intelligent diagnostics"""
        diagnostics = []

        # Pressure diagnostics
        if pressure < 120:
            diagnostics.append({
                "type": "CRITICAL",
                "parameter": "Hydraulic Pressure",
                "message": "Hydraulic pressure is critically low. This severely reduces impact energy and drilling performance.",
                "recommendation": "Immediately inspect hydraulic pump, check for leakage, and verify system pressurization.",
                "priority": 1
            })
        elif pressure < 180:
            diagnostics.append({
                "type": "WARNING",
                "parameter": "Hydraulic Pressure",
                "message": "Hydraulic pressure is below the recommended operating range. This reduces impact energy and drilling performance.",
                "recommendation": "Increase hydraulic pressure or inspect the hydraulic pump and check for leakage points.",
                "priority": 2
            })
        elif pressure > 350:
            diagnostics.append({
                "type": "WARNING",
                "parameter": "Hydraulic Pressure",
                "message": "Hydraulic pressure exceeds safe operating limits. Risk of system damage and seal failures.",
                "recommendation": "Reduce pressure to the recommended range or check pressure relief valve setting.",
                "priority": 2
            })

        # Flow rate diagnostics
        if flow_rate < 50:
            diagnostics.append({
                "type": "WARNING",
                "parameter": "Hydraulic Flow Rate",
                "message": "Hydraulic flow rate is insufficient for optimal drilling performance.",
                "recommendation": "Inspect pump output, check valves, hoses, and verify hydraulic circuit for restrictions.",
                "priority": 2
            })
        elif flow_rate > 250:
            diagnostics.append({
                "type": "WARNING",
                "parameter": "Hydraulic Flow Rate",
                "message": "Flow rate is excessive and may cause system overload and premature wear.",
                "recommendation": "Reduce flow rate to the recommended operating range.",
                "priority": 2
            })

        # RPM diagnostics
        if rpm < 100:
            diagnostics.append({
                "type": "WARNING",
                "parameter": "Rotation Speed",
                "message": "Rotation speed is lower than the optimum operating range.",
                "recommendation": "Increase drill rotation speed according to the selected drill type and rock hardness.",
                "priority": 2
            })
        elif rpm > 500:
            diagnostics.append({
                "type": "WARNING",
                "parameter": "Rotation Speed",
                "message": "Rotation speed is too high and may increase drill bit wear and machine vibration.",
                "recommendation": "Reduce RPM to the recommended operating range for the selected drill type.",
                "priority": 2
            })

        # Temperature diagnostics
        if temperature < 15:
            diagnostics.append({
                "type": "INFO",
                "parameter": "Hydraulic Oil Temperature",
                "message": "Hydraulic oil temperature is below optimal. Oil viscosity is higher, reducing efficiency.",
                "recommendation": "Allow the system to warm up or check the heater functionality.",
                "priority": 3
            })
        elif temperature < 40:
            diagnostics.append({
                "type": "INFO",
                "parameter": "Hydraulic Oil Temperature",
                "message": "Hydraulic oil temperature is in the good operating range.",
                "recommendation": "Continue monitoring temperature during operation.",
                "priority": 3
            })
        elif temperature >= 75:
            diagnostics.append({
                "type": "CRITICAL",
                "parameter": "Hydraulic Oil Temperature",
                "message": "Hydraulic oil temperature is excessively high. Risk of fluid degradation and seal damage.",
                "recommendation": "Immediately inspect cooling system, oil condition, filters, and heat exchanger. Check for restricted oil flow.",
                "priority": 1
            })
        elif temperature >= 60:
            diagnostics.append({
                "type": "WARNING",
                "parameter": "Hydraulic Oil Temperature",
                "message": "Hydraulic oil temperature is elevated above optimal range.",
                "recommendation": "Inspect cooling system, oil condition, filters, and heat exchanger.",
                "priority": 2
            })

        # Piston diameter warning
        if piston_diameter < 10:
            diagnostics.append({
                "type": "INFO",
                "parameter": "Piston Diameter",
                "message": "Small piston diameter limits drilling force.",
                "recommendation": "Consider upgrading to a larger piston for increased performance.",
                "priority": 3
            })

        # Add positive feedback if no critical issues
        if not any(d["type"] == "CRITICAL" for d in diagnostics):
            if efficiency >= 80:
                diagnostics.append({
                    "type": "INFO",
                    "parameter": "Overall Performance",
                    "message": "Machine is operating at excellent efficiency levels.",
                    "recommendation": "Continue with regular maintenance schedule.",
                    "priority": 3
                })

        return sorted(diagnostics, key=lambda x: x["priority"])

    def _calculate_health_score(self, pressure: float, flow_rate: float,
                               rpm: float, temperature: float,
                               efficiency: float) -> float:
        """Calculate overall machine health score"""
        health_components = []

        # Pressure health (25%)
        if pressure < 180 or pressure > 350:
            pressure_health = 50
        elif pressure < 220 or pressure > 320:
            pressure_health = 75
        else:
            pressure_health = 100
        health_components.append(pressure_health * 0.25)

        # Flow rate health (25%)
        if flow_rate < 50 or flow_rate > 250:
            flow_health = 50
        elif flow_rate < 80 or flow_rate > 180:
            flow_health = 75
        else:
            flow_health = 100
        health_components.append(flow_health * 0.25)

        # RPM health (20%)
        if rpm < 100 or rpm > 500:
            rpm_health = 50
        elif rpm < 150 or rpm > 450:
            rpm_health = 75
        else:
            rpm_health = 100
        health_components.append(rpm_health * 0.20)

        # Temperature health (15%)
        if temperature < 15 or temperature >= 75:
            temp_health = 40
        elif temperature < 20 or temperature >= 60:
            temp_health = 65
        else:
            temp_health = 100
        health_components.append(temp_health * 0.15)

        # Efficiency component (15%)
        efficiency_health = efficiency
        health_components.append(efficiency_health * 0.15)

        return sum(health_components)

    def get_optimization_recommendations(self, analysis_results: Dict) -> List[Dict]:
        """Generate AI-style optimization recommendations"""
        recommendations = []

        if not analysis_results.get("valid"):
            return recommendations

        efficiency = analysis_results["efficiency_percentage"]
        pressure = analysis_results["input_parameters"]["pressure"]
        flow_rate = analysis_results["input_parameters"]["flow_rate"]
        temperature = analysis_results["input_parameters"]["temperature"]
        rpm = analysis_results["input_parameters"]["rpm"]

        # Pressure optimization
        if pressure < 220:
            estimated_improvement = min(15, (220 - pressure) / 10)
            new_efficiency = min(100, efficiency + estimated_improvement)
            recommendations.append({
                "category": "Hydraulic Pressure",
                "current_value": pressure,
                "recommended_value": 250,
                "estimated_improvement": round(estimated_improvement, 1),
                "new_efficiency": round(new_efficiency, 1),
                "action": f"Increase hydraulic pressure from {pressure} bar to approximately 250 bar"
            })

        # Temperature optimization
        if temperature > 60:
            estimated_improvement = min(20, (temperature - 55) / 2)
            new_efficiency = min(100, efficiency + estimated_improvement)
            recommendations.append({
                "category": "Oil Temperature",
                "current_value": temperature,
                "recommended_value": 45,
                "estimated_improvement": round(estimated_improvement, 1),
                "new_efficiency": round(new_efficiency, 1),
                "action": f"Reduce oil temperature from {temperature}°C to approximately 45°C. Service cooling system."
            })

        # Flow rate optimization
        if flow_rate < 100:
            estimated_improvement = min(10, (100 - flow_rate) / 5)
            new_efficiency = min(100, efficiency + estimated_improvement)
            recommendations.append({
                "category": "Hydraulic Flow Rate",
                "current_value": flow_rate,
                "recommended_value": 120,
                "estimated_improvement": round(estimated_improvement, 1),
                "new_efficiency": round(new_efficiency, 1),
                "action": f"Increase flow rate from {flow_rate} L/min to approximately 120 L/min"
            })

        # RPM optimization
        if rpm < 250:
            estimated_improvement = min(12, (250 - rpm) / 20)
            new_efficiency = min(100, efficiency + estimated_improvement)
            recommendations.append({
                "category": "Rotation Speed",
                "current_value": rpm,
                "recommended_value": 350,
                "estimated_improvement": round(estimated_improvement, 1),
                "new_efficiency": round(new_efficiency, 1),
                "action": f"Increase rotation speed from {rpm} RPM to approximately 350 RPM"
            })

        return recommendations
