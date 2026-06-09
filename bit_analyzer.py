"""
Drill Bit Life & Wear Analysis Module
Predictive maintenance and bit wear estimation system
Version 1.0
"""

import math
from typing import Dict, List, Tuple
from dataclasses import dataclass
from datetime import datetime


@dataclass
class BitSpecification:
    """Drill bit specifications and wear characteristics"""
    name: str
    material: str
    typical_life_min: int      # Minimum life in hours
    typical_life_max: int      # Maximum life in hours
    optimal_rpm_min: int
    optimal_rpm_max: int
    optimal_pressure_min: int
    optimal_pressure_max: int
    optimal_temp_min: int
    optimal_temp_max: int
    wear_resistance_factor: float  # 0.5 to 1.5


# Drill Bit Type Database
BIT_TYPES = {
    "Tungsten Carbide Bit": BitSpecification(
        name="Tungsten Carbide Bit",
        material="Tungsten Carbide",
        typical_life_min=100, typical_life_max=150,
        optimal_rpm_min=150, optimal_rpm_max=300,
        optimal_pressure_min=220, optimal_pressure_max=280,
        optimal_temp_min=20, optimal_temp_max=60,
        wear_resistance_factor=0.8
    ),
    "Button Bit": BitSpecification(
        name="Button Bit",
        material="Steel with Button Inserts",
        typical_life_min=150, typical_life_max=250,
        optimal_rpm_min=180, optimal_rpm_max=350,
        optimal_pressure_min=240, optimal_pressure_max=300,
        optimal_temp_min=20, optimal_temp_max=60,
        wear_resistance_factor=1.0
    ),
    "Cross Bit": BitSpecification(
        name="Cross Bit",
        material="Steel Alloy",
        typical_life_min=80, typical_life_max=120,
        optimal_rpm_min=100, optimal_rpm_max=250,
        optimal_pressure_min=200, optimal_pressure_max=260,
        optimal_temp_min=20, optimal_temp_max=55,
        wear_resistance_factor=0.7
    ),
    "Chisel Bit": BitSpecification(
        name="Chisel Bit",
        material="Hardened Steel",
        typical_life_min=120, typical_life_max=180,
        optimal_rpm_min=120, optimal_rpm_max=280,
        optimal_pressure_min=210, optimal_pressure_max=270,
        optimal_temp_min=20, optimal_temp_max=58,
        wear_resistance_factor=0.75
    ),
    "DTH Bit": BitSpecification(
        name="DTH Bit",
        material="Tungsten Carbide Inserts",
        typical_life_min=200, typical_life_max=350,
        optimal_rpm_min=300, optimal_rpm_max=500,
        optimal_pressure_min=280, optimal_pressure_max=380,
        optimal_temp_min=30, optimal_temp_max=70,
        wear_resistance_factor=1.2
    ),
    "Tricone Bit": BitSpecification(
        name="Tricone Bit",
        material="Roller Cone Assembly",
        typical_life_min=300, typical_life_max=600,
        optimal_rpm_min=100, optimal_rpm_max=200,
        optimal_pressure_min=220, optimal_pressure_max=300,
        optimal_temp_min=25, optimal_temp_max=65,
        wear_resistance_factor=1.3
    ),
    "PDC Bit": BitSpecification(
        name="PDC Bit",
        material="Polycrystalline Diamond Compact",
        typical_life_min=500, typical_life_max=1000,
        optimal_rpm_min=250, optimal_rpm_max=400,
        optimal_pressure_min=260, optimal_pressure_max=340,
        optimal_temp_min=30, optimal_temp_max=70,
        wear_resistance_factor=1.4
    ),
    "Diamond Bit": BitSpecification(
        name="Diamond Bit",
        material="Industrial Diamond",
        typical_life_min=1000, typical_life_max=3000,
        optimal_rpm_min=200, optimal_rpm_max=350,
        optimal_pressure_min=240, optimal_pressure_max=320,
        optimal_temp_min=20, optimal_temp_max=60,
        wear_resistance_factor=1.5
    ),
    "Core Drill Bit": BitSpecification(
        name="Core Drill Bit",
        material="Diamond Crown with Steel Body",
        typical_life_min=300, typical_life_max=800,
        optimal_rpm_min=50, optimal_rpm_max=200,
        optimal_pressure_min=150, optimal_pressure_max=250,
        optimal_temp_min=20, optimal_temp_max=55,
        wear_resistance_factor=1.1
    ),
}


class DrillBitAnalyzer:
    """Comprehensive drill bit wear and life analysis system"""

    def __init__(self, bit_type: str):
        self.bit_type = bit_type
        self.spec = BIT_TYPES.get(bit_type)
        if not self.spec:
            raise ValueError(f"Invalid bit type: {bit_type}")

    def validate_inputs(self, pressure: float, flow_rate: float, rpm: float,
                       temperature: float, piston_diameter: float,
                       bit_diameter: float, machine_efficiency: float) -> Tuple[bool, List[str]]:
        """Validate all input parameters"""
        errors = []

        if not (50 <= pressure <= 500):
            errors.append("Pressure must be between 50-500 bar")
        if not (10 <= flow_rate <= 300):
            errors.append("Flow rate must be between 10-300 L/min")
        if not (10 <= rpm <= 1000):
            errors.append("RPM must be between 10-1000")
        if not (-20 <= temperature <= 120):
            errors.append("Temperature must be between -20 and 120°C")
        if not (5 <= piston_diameter <= 200):
            errors.append("Piston diameter must be between 5-200 mm")
        if not (1 <= bit_diameter <= 300):
            errors.append("Drill bit diameter must be between 1-300 mm")
        if not (0 <= machine_efficiency <= 100):
            errors.append("Machine efficiency must be between 0-100%")

        return len(errors) == 0, errors

    def calculate_rpm_wear_factor(self, rpm: float) -> float:
        """
        Calculate wear factor based on RPM
        RPM Impact:
        100-180: Low Wear (20%)
        180-300: Normal Wear (50%)
        300-450: High Wear (80%)
        Above 450: Severe Wear (100%)
        """
        if rpm < 100:
            return 0.15  # Very low stress
        elif rpm < 180:
            return 0.20  # Low wear
        elif rpm < 300:
            return 0.50  # Normal wear
        elif rpm < 450:
            return 0.80  # High wear
        else:
            return 1.00  # Severe wear

    def calculate_temperature_wear_factor(self, temperature: float) -> float:
        """
        Calculate wear factor based on temperature
        20-60°C: Low Wear (20%)
        60-75°C: Moderate Wear (50%)
        75-90°C: High Wear (80%)
        Above 90°C: Severe Wear (100%)
        """
        if temperature < 20:
            return 0.10  # Very cold
        elif temperature < 60:
            return 0.20  # Low wear
        elif temperature < 75:
            return 0.50  # Moderate wear
        elif temperature < 90:
            return 0.80  # High wear
        else:
            return 1.00  # Severe wear

    def calculate_pressure_wear_factor(self, pressure: float) -> float:
        """
        Calculate wear factor based on pressure
        220-280 bar: Optimal (20%)
        280-350 bar: Moderate Wear (50%)
        Above 350 bar: High Wear (80%)
        Below 220 bar: Reduced wear (10%)
        """
        if pressure < 120:
            return 0.05
        elif pressure < 220:
            return 0.10  # Below optimal
        elif pressure < 280:
            return 0.20  # Optimal
        elif pressure < 350:
            return 0.50  # Moderate wear
        else:
            return 0.80  # High wear

    def calculate_efficiency_wear_factor(self, machine_efficiency: float) -> float:
        """
        Calculate wear factor based on machine efficiency
        Efficiency directly reflects system wear conditions
        """
        # Normalize efficiency (0-100%) to wear factor (0-1)
        # Low efficiency = high wear
        wear_factor = (100 - machine_efficiency) / 100
        return min(1.0, max(0.0, wear_factor))

    def calculate_bit_wear_index(self, pressure: float, flow_rate: float, rpm: float,
                                temperature: float, piston_diameter: float,
                                bit_diameter: float, machine_efficiency: float) -> float:
        """
        Calculate Bit Wear Index (BWI) using weighted factors
        
        Weight Distribution:
        - RPM Factor: 35%
        - Pressure Factor: 25%
        - Temperature Factor: 20%
        - Machine Efficiency Factor: 20%
        """
        # Calculate individual wear factors
        rpm_factor = self.calculate_rpm_wear_factor(rpm)
        pressure_factor = self.calculate_pressure_wear_factor(pressure)
        temperature_factor = self.calculate_temperature_wear_factor(temperature)
        efficiency_factor = self.calculate_efficiency_wear_factor(machine_efficiency)

        # Apply bit-specific wear resistance factor
        base_bwi = (
            rpm_factor * 0.35 +
            pressure_factor * 0.25 +
            temperature_factor * 0.20 +
            efficiency_factor * 0.20
        )

        # Apply bit wear resistance adjustment
        adjusted_bwi = base_bwi / self.spec.wear_resistance_factor

        # Convert to percentage (0-100)
        wear_percentage = adjusted_bwi * 100

        return min(100, max(0, wear_percentage))

    def get_wear_category(self, wear_percentage: float) -> str:
        """Get wear category from percentage"""
        if wear_percentage <= 20:
            return "Excellent"
        elif wear_percentage <= 40:
            return "Good"
        elif wear_percentage <= 60:
            return "Moderate Wear"
        elif wear_percentage <= 80:
            return "High Wear"
        else:
            return "Critical Wear"

    def get_wear_color(self, wear_percentage: float) -> str:
        """Get color code for wear level"""
        if wear_percentage <= 20:
            return "#00aa00"  # Green
        elif wear_percentage <= 40:
            return "#88cc00"  # Light Green
        elif wear_percentage <= 60:
            return "#ffff00"  # Yellow
        elif wear_percentage <= 80:
            return "#ff8800"  # Orange
        else:
            return "#ff0000"  # Red

    def calculate_remaining_life(self, wear_percentage: float) -> float:
        """Calculate remaining bit life percentage"""
        remaining_life = 100 - wear_percentage
        return max(0, remaining_life)

    def calculate_remaining_hours(self, wear_percentage: float) -> float:
        """Calculate estimated remaining operating hours"""
        # Use midpoint of typical life range
        typical_life_hours = (self.spec.typical_life_min + self.spec.typical_life_max) / 2
        remaining_life_percentage = self.calculate_remaining_life(wear_percentage)
        remaining_hours = typical_life_hours * (remaining_life_percentage / 100)
        return round(remaining_hours, 1)

    def get_bit_health_status(self, remaining_life_percentage: float) -> str:
        """Get bit health status"""
        if remaining_life_percentage >= 80:
            return "Excellent"
        elif remaining_life_percentage >= 60:
            return "Good"
        elif remaining_life_percentage >= 40:
            return "Moderate"
        elif remaining_life_percentage >= 20:
            return "Poor"
        else:
            return "Replace Immediately"

    def get_failure_risk_level(self, remaining_life_percentage: float) -> str:
        """Get failure risk level"""
        if remaining_life_percentage >= 70:
            return "Low Risk"
        elif remaining_life_percentage >= 50:
            return "Moderate Risk"
        elif remaining_life_percentage >= 30:
            return "High Risk"
        else:
            return "Critical Risk"

    def get_replacement_recommendation(self, remaining_life_percentage: float) -> str:
        """Get replacement recommendation"""
        if remaining_life_percentage >= 50:
            return "No Action - Continue operation and monitor"
        elif remaining_life_percentage >= 30:
            return "Plan replacement - Schedule within 50 operating hours"
        elif remaining_life_percentage >= 15:
            return "Urgent replacement - Schedule within 25 operating hours"
        else:
            return "IMMEDIATE REPLACEMENT - Stop operation, replace bit now"

    def get_replacement_priority(self, remaining_life_percentage: float) -> str:
        """Get replacement priority level"""
        if remaining_life_percentage >= 50:
            return "Low"
        elif remaining_life_percentage >= 30:
            return "Medium"
        elif remaining_life_percentage >= 15:
            return "High"
        else:
            return "Critical"

    def perform_bit_diagnostics(self, pressure: float, flow_rate: float, rpm: float,
                               temperature: float, machine_efficiency: float,
                               wear_percentage: float) -> List[Dict]:
        """Perform detailed bit wear diagnostics"""
        diagnostics = []

        # RPM diagnostics
        if rpm > self.spec.optimal_rpm_max:
            wear_impact = self.calculate_rpm_wear_factor(rpm)
            diagnostics.append({
                "type": "WARNING",
                "parameter": "Rotation Speed (RPM)",
                "message": f"RPM ({rpm}) exceeds optimal range ({self.spec.optimal_rpm_min}-{self.spec.optimal_rpm_max}). "
                          f"Excessive rotation causes accelerated bit wear and reduced lifespan.",
                "recommendation": f"Reduce RPM to {self.spec.optimal_rpm_min}-{self.spec.optimal_rpm_max} range",
                "wear_impact": f"{wear_impact*100:.0f}%",
                "priority": 1
            })

        # Temperature diagnostics
        if temperature > self.spec.optimal_temp_max:
            wear_impact = self.calculate_temperature_wear_factor(temperature)
            diagnostics.append({
                "type": "WARNING",
                "parameter": "Hydraulic Oil Temperature",
                "message": f"Temperature ({temperature}°C) exceeds optimal range ({self.spec.optimal_temp_min}-{self.spec.optimal_temp_max}°C). "
                          f"Heat accelerates bit material degradation.",
                "recommendation": f"Maintain temperature below {self.spec.optimal_temp_max}°C. Inspect cooling system.",
                "wear_impact": f"{wear_impact*100:.0f}%",
                "priority": 1
            })

        # Pressure diagnostics
        if pressure < self.spec.optimal_pressure_min or pressure > self.spec.optimal_pressure_max:
            wear_impact = self.calculate_pressure_wear_factor(pressure)
            diagnostics.append({
                "type": "WARNING",
                "parameter": "Hydraulic Pressure",
                "message": f"Pressure ({pressure} bar) outside optimal range ({self.spec.optimal_pressure_min}-{self.spec.optimal_pressure_max} bar). "
                          f"Improper pressure causes uneven bit wear.",
                "recommendation": f"Maintain pressure between {self.spec.optimal_pressure_min}-{self.spec.optimal_pressure_max} bar",
                "wear_impact": f"{wear_impact*100:.0f}%",
                "priority": 2
            })

        # Efficiency diagnostics
        if machine_efficiency < 70:
            diagnostics.append({
                "type": "WARNING",
                "parameter": "Machine Efficiency",
                "message": f"Machine efficiency ({machine_efficiency}%) is low, indicating system wear and inefficiency. "
                          f"This causes unnecessary bit stress.",
                "recommendation": "Optimize pressure, flow rate, and RPM. Perform maintenance on hydraulic system.",
                "wear_impact": f"{(100-machine_efficiency)/100*100:.0f}%",
                "priority": 2
            })

        # Positive feedback
        if wear_percentage < 30 and machine_efficiency >= 80:
            diagnostics.append({
                "type": "INFO",
                "parameter": "Bit Condition",
                "message": f"Drill bit is in excellent condition with minimal wear ({wear_percentage:.1f}%). "
                          f"Operating parameters are optimal for this bit type.",
                "recommendation": "Continue current operation and monitor regularly",
                "wear_impact": f"{wear_percentage:.1f}%",
                "priority": 3
            })

        return sorted(diagnostics, key=lambda x: x["priority"])

    def get_life_extension_recommendations(self, analysis_result: Dict) -> List[Dict]:
        """Generate recommendations to extend bit life"""
        recommendations = []

        pressure = analysis_result["input_parameters"]["pressure"]
        temperature = analysis_result["input_parameters"]["temperature"]
        rpm = analysis_result["input_parameters"]["rpm"]
        machine_efficiency = analysis_result["input_parameters"]["machine_efficiency"]
        wear_percentage = analysis_result["wear_percentage"]

        current_remaining_hours = self.calculate_remaining_hours(wear_percentage)

        # RPM optimization
        if rpm > self.spec.optimal_rpm_max:
            reduced_rpm = (self.spec.optimal_rpm_min + self.spec.optimal_rpm_max) / 2
            # Recalculate wear with reduced RPM
            reduced_wear = self.calculate_bit_wear_index(
                pressure, 0, reduced_rpm, temperature, 0, 0, machine_efficiency
            )
            extended_hours = self.calculate_remaining_hours(reduced_wear)
            life_extension = extended_hours - current_remaining_hours
            recommendations.append({
                "category": "Rotation Speed Reduction",
                "current_value": rpm,
                "recommended_value": reduced_rpm,
                "current_hours_remaining": round(current_remaining_hours, 1),
                "new_hours_remaining": round(extended_hours, 1),
                "hours_extension": round(life_extension, 1),
                "percentage_improvement": round((life_extension / current_remaining_hours * 100) if current_remaining_hours > 0 else 0, 1),
                "action": f"Reduce RPM from {rpm} to approximately {reduced_rpm:.0f}"
            })

        # Temperature optimization
        if temperature > self.spec.optimal_temp_max:
            optimal_temp = self.spec.optimal_temp_max
            reduced_wear = self.calculate_bit_wear_index(
                pressure, 0, rpm, optimal_temp, 0, 0, machine_efficiency
            )
            extended_hours = self.calculate_remaining_hours(reduced_wear)
            life_extension = extended_hours - current_remaining_hours
            recommendations.append({
                "category": "Temperature Control",
                "current_value": temperature,
                "recommended_value": optimal_temp,
                "current_hours_remaining": round(current_remaining_hours, 1),
                "new_hours_remaining": round(extended_hours, 1),
                "hours_extension": round(life_extension, 1),
                "percentage_improvement": round((life_extension / current_remaining_hours * 100) if current_remaining_hours > 0 else 0, 1),
                "action": f"Reduce temperature to {optimal_temp}°C. Service cooling system."
            })

        # Pressure optimization
        if pressure < self.spec.optimal_pressure_min:
            optimal_pressure = self.spec.optimal_pressure_min
            reduced_wear = self.calculate_bit_wear_index(
                optimal_pressure, 0, rpm, temperature, 0, 0, machine_efficiency
            )
            extended_hours = self.calculate_remaining_hours(reduced_wear)
            life_extension = extended_hours - current_remaining_hours
            recommendations.append({
                "category": "Pressure Adjustment",
                "current_value": pressure,
                "recommended_value": optimal_pressure,
                "current_hours_remaining": round(current_remaining_hours, 1),
                "new_hours_remaining": round(extended_hours, 1),
                "hours_extension": round(life_extension, 1),
                "percentage_improvement": round((life_extension / current_remaining_hours * 100) if current_remaining_hours > 0 else 0, 1),
                "action": f"Increase pressure to {optimal_pressure} bar"
            })

        # Machine efficiency optimization
        if machine_efficiency < 85:
            optimal_efficiency = 85
            reduced_wear = self.calculate_bit_wear_index(
                pressure, 0, rpm, temperature, 0, 0, optimal_efficiency
            )
            extended_hours = self.calculate_remaining_hours(reduced_wear)
            life_extension = extended_hours - current_remaining_hours
            recommendations.append({
                "category": "System Efficiency",
                "current_value": machine_efficiency,
                "recommended_value": optimal_efficiency,
                "current_hours_remaining": round(current_remaining_hours, 1),
                "new_hours_remaining": round(extended_hours, 1),
                "hours_extension": round(life_extension, 1),
                "percentage_improvement": round((life_extension / current_remaining_hours * 100) if current_remaining_hours > 0 else 0, 1),
                "action": "Optimize hydraulic system for improved efficiency"
            })

        return recommendations

    def predict_failure_time(self, remaining_hours: float) -> str:
        """Predict when bit will fail at current wear rate"""
        if remaining_hours > 100:
            return f"Over {remaining_hours:.0f} hours of remaining life"
        elif remaining_hours > 50:
            return f"Approximately {remaining_hours:.0f} hours remaining"
        elif remaining_hours > 20:
            return f"Only {remaining_hours:.0f} hours remaining - plan replacement soon"
        else:
            return f"Critical: Only {remaining_hours:.0f} hours until failure"

    def predict_extended_life(self, recommendations: List[Dict]) -> Dict:
        """Predict extended life if recommendations are followed"""
        if not recommendations:
            return {
                "total_extension_hours": 0,
                "total_extension_percentage": 0,
                "message": "Operating parameters are already optimal"
            }

        total_extension_hours = 0
        current_hours = recommendations[0]["current_hours_remaining"]

        for rec in recommendations:
            total_extension_hours += rec["hours_extension"]

        total_extension_percentage = (total_extension_hours / current_hours * 100) if current_hours > 0 else 0

        return {
            "total_extension_hours": round(total_extension_hours, 1),
            "total_extension_percentage": round(total_extension_percentage, 1),
            "message": f"By implementing all recommendations, bit life could be extended by {total_extension_hours:.0f} hours "
                      f"({total_extension_percentage:.1f}% improvement)"
        }

    def run_analysis(self, pressure: float, flow_rate: float, rpm: float,
                    temperature: float, piston_diameter: float,
                    bit_diameter: float, machine_efficiency: float) -> Dict:
        """Run complete bit life analysis"""

        # Validate inputs
        is_valid, errors = self.validate_inputs(pressure, flow_rate, rpm,
                                               temperature, piston_diameter,
                                               bit_diameter, machine_efficiency)
        if not is_valid:
            return {"valid": False, "errors": errors}

        # Calculate bit wear index
        wear_percentage = self.calculate_bit_wear_index(
            pressure, flow_rate, rpm, temperature,
            piston_diameter, bit_diameter, machine_efficiency
        )

        # Calculate remaining life
        remaining_life_percentage = self.calculate_remaining_life(wear_percentage)
        remaining_hours = self.calculate_remaining_hours(wear_percentage)

        # Get status indicators
        wear_category = self.get_wear_category(wear_percentage)
        health_status = self.get_bit_health_status(remaining_life_percentage)
        failure_risk = self.get_failure_risk_level(remaining_life_percentage)
        replacement_recommendation = self.get_replacement_recommendation(remaining_life_percentage)
        replacement_priority = self.get_replacement_priority(remaining_life_percentage)
        wear_color = self.get_wear_color(wear_percentage)

        # Perform diagnostics
        diagnostics = self.perform_bit_diagnostics(
            pressure, flow_rate, rpm, temperature,
            machine_efficiency, wear_percentage
        )

        # Get life extension recommendations
        input_params = {
            "pressure": pressure,
            "flow_rate": flow_rate,
            "rpm": rpm,
            "temperature": temperature,
            "piston_diameter": piston_diameter,
            "bit_diameter": bit_diameter,
            "machine_efficiency": machine_efficiency
        }

        temp_result = {
            "input_parameters": input_params,
            "wear_percentage": wear_percentage
        }

        life_extension_recs = self.get_life_extension_recommendations(temp_result)
        extended_life_prediction = self.predict_extended_life(life_extension_recs)

        # Compile results
        results = {
            "valid": True,
            "bit_type": self.bit_type,
            "bit_material": self.spec.material,
            "typical_life_hours": f"{self.spec.typical_life_min}-{self.spec.typical_life_max}",
            "typical_life_average": (self.spec.typical_life_min + self.spec.typical_life_max) / 2,
            "wear_percentage": round(wear_percentage, 2),
            "wear_category": wear_category,
            "wear_color": wear_color,
            "remaining_life_percentage": round(remaining_life_percentage, 2),
            "remaining_operating_hours": round(remaining_hours, 1),
            "bit_health_status": health_status,
            "failure_risk_level": failure_risk,
            "replacement_recommendation": replacement_recommendation,
            "replacement_priority": replacement_priority,
            "diagnostics": diagnostics,
            "life_extension_recommendations": life_extension_recs,
            "extended_life_prediction": extended_life_prediction,
            "failure_time_prediction": self.predict_failure_time(remaining_hours),
            "input_parameters": input_params,
            "timestamp": datetime.now().isoformat()
        }

        return results
