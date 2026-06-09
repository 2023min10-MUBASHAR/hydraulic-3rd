"""
Data Persistence and History Management Module
Handles saving and loading analysis history
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict


class DataManager:
    """Manages data persistence and history"""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.history_file = self.data_dir / "analysis_history.json"
        self.settings_file = self.data_dir / "settings.json"

    def save_analysis(self, analysis_result: Dict) -> bool:
        """Save analysis result to history"""
        try:
            history = self.load_history()
            history.append(analysis_result)

            # Keep only last 100 analyses
            if len(history) > 100:
                history = history[-100:]

            with open(self.history_file, 'w') as f:
                json.dump(history, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving analysis: {e}")
            return False

    def load_history(self) -> List[Dict]:
        """Load analysis history"""
        if not self.history_file.exists():
            return []

        try:
            with open(self.history_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading history: {e}")
            return []

    def get_analysis_by_date(self, date_str: str) -> List[Dict]:
        """Get analyses from a specific date"""
        history = self.load_history()
        return [a for a in history if a.get("timestamp", "").startswith(date_str)]

    def get_analysis_by_drill_type(self, drill_type: str) -> List[Dict]:
        """Get analyses for a specific drill type"""
        history = self.load_history()
        return [a for a in history if a.get("drill_type") == drill_type]

    def clear_history(self) -> bool:
        """Clear all history"""
        try:
            if self.history_file.exists():
                self.history_file.unlink()
            return True
        except Exception as e:
            print(f"Error clearing history: {e}")
            return False

    def save_settings(self, settings: Dict) -> bool:
        """Save application settings"""
        try:
            with open(self.settings_file, 'w') as f:
                json.dump(settings, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving settings: {e}")
            return False

    def load_settings(self) -> Dict:
        """Load application settings"""
        default_settings = {
            "theme": "light",
            "units": "metric",
            "auto_save": True,
            "language": "en"
        }

        if not self.settings_file.exists():
            self.save_settings(default_settings)
            return default_settings

        try:
            with open(self.settings_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading settings: {e}")
            return default_settings

    def export_to_csv(self, filename: str = None) -> bool:
        """Export analysis history to CSV"""
        import csv

        try:
            if filename is None:
                filename = f"hydraulic_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

            history = self.load_history()
            if not history:
                return False

            filepath = self.data_dir / filename

            with open(filepath, 'w', newline='') as f:
                fieldnames = [
                    'timestamp', 'drill_type', 'efficiency_percentage',
                    'health_score', 'pressure', 'flow_rate', 'rpm',
                    'temperature', 'hydraulic_power_kw'
                ]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()

                for analysis in history:
                    if analysis.get("valid"):
                        row = {
                            'timestamp': analysis.get('timestamp'),
                            'drill_type': analysis.get('drill_type'),
                            'efficiency_percentage': analysis.get('efficiency_percentage'),
                            'health_score': analysis.get('health_score'),
                            'pressure': analysis.get('input_parameters', {}).get('pressure'),
                            'flow_rate': analysis.get('input_parameters', {}).get('flow_rate'),
                            'rpm': analysis.get('input_parameters', {}).get('rpm'),
                            'temperature': analysis.get('input_parameters', {}).get('temperature'),
                            'hydraulic_power_kw': analysis.get('hydraulic_power_kw')
                        }
                        writer.writerow(row)

            return True
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False
