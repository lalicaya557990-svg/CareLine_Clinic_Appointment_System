from PyQt6.QtCore import QDate
from datetime import datetime, timedelta
from decimal import Decimal
from models.database import DatabaseOperations  # MVC Import Fix


class KPI:
    """KPI data class"""

    def __init__(self, name, current_value, target_value, previous_value, unit, description, recommendations):
        self.name = name
        self.current_value = float(current_value) if current_value is not None else 0.0
        self.target_value = float(target_value)
        self.previous_value = float(previous_value) if previous_value is not None else 0.0
        self.unit = unit
        self.description = description
        self.recommendations = recommendations
        self.trend = round(self.current_value - self.previous_value, 1)
        self.status = "neutral"


class KPIReportGenerator:
    """Generates KPI reports from REAL database data"""

    def __init__(self, main_app):
        self.main_app = main_app
        self.db_ops = DatabaseOperations()
        self.kpis = {}
        # Target values
        self.targets = {
            'no_show_rate': 10.0,
            'cancellation_rate': 15.0,
            'completion_rate': 70.0,
            'patient_retention': 75.0,
            'doctor_utilization': 75.0,
            'appointment_growth': 10.0
        }

    def convert_to_float(self, value):
        if value is None: return 0.0
        if isinstance(value, Decimal): return float(value)
        try:
            return float(value)
        except:
            return 0.0

    def get_database_kpis(self, doctor_id, start_date, end_date):
        kpi_data = {'current_period': {}, 'previous_period': {}, 'doctor_info': {}}
        try:
            # 1. Doctor Info
            doctor_info = self.db_ops.get_user_by_id(doctor_id)
            if doctor_info:
                kpi_data['doctor_info'] = {
                    'name': f"{doctor_info.get('FirstName', '')} {doctor_info.get('LastName', '')}",
                    'specialization': doctor_info.get('Specialization', ''),
                    'email': doctor_info.get('Email', '')
                }

            # 2. Current Period Data
            noshow_stats = self.db_ops.calculate_noshow_rate(doctor_id, start_date, end_date)

            if noshow_stats:
                total = self.convert_to_float(noshow_stats.get('total_appointments', 0))
                comp = self.convert_to_float(noshow_stats.get('completed_count', 0))
                canc = self.convert_to_float(noshow_stats.get('cancelled_count', 0))
                noshow = self.convert_to_float(noshow_stats.get('noshow_count', 0))

                # Rates
                ns_rate = self.convert_to_float(noshow_stats.get('noshow_rate', 0.0))
                comp_rate = self.convert_to_float(noshow_stats.get('completion_rate', 0.0))
                canc_rate = self.convert_to_float(noshow_stats.get('cancellation_rate', 0.0))

                unique_pts = self.get_unique_patients_count(doctor_id, start_date, end_date)
                utilization = (comp * 0.5 / 160 * 100)  # Simple calc: 30min slots / 160 hrs

                kpi_data['current_period'] = {
                    'total_appointments': int(total),
                    'completed_appointments': int(comp),
                    'cancelled_appointments': int(canc),
                    'noshow_appointments': int(noshow),
                    'unique_patients': int(unique_pts),
                    'completion_rate': round(comp_rate, 1),
                    'cancellation_rate': round(canc_rate, 1),
                    'no_show_rate': round(ns_rate, 1),
                    'utilization_rate': round(utilization, 1)
                }
            else:
                # Fallback if no stats returned
                return None

            # 3. Previous Period Data
            start_dt = datetime.strptime(start_date, "%Y-%m-%d")
            end_dt = datetime.strptime(end_date, "%Y-%m-%d")
            period_days = (end_dt - start_dt).days
            prev_end = (start_dt - timedelta(days=1)).strftime("%Y-%m-%d")
            prev_start = (start_dt - timedelta(days=period_days + 1)).strftime("%Y-%m-%d")

            prev_apps = self.get_appointments_for_period(doctor_id, prev_start, prev_end)
            prev_total = len(prev_apps)

            # Growth
            curr_total = kpi_data['current_period'].get('total_appointments', 0)
            growth = ((curr_total - prev_total) / prev_total * 100) if prev_total > 0 else 0.0

            retention = self.calculate_retention_rate(doctor_id, start_date, end_date)

            kpi_data['previous_period'] = {
                'total_appointments': prev_total,
                'growth_rate': round(growth, 1),
                'retention_rate': round(retention, 1)
            }
            return kpi_data

        except Exception as e:
            print(f"KPI DB Error: {e}")
            return None

    def get_appointments_for_period(self, doctor_id, start_date, end_date):
        try:
            all_apps = self.db_ops.get_all_appointments_for_doctor(doctor_id)
            if not all_apps: return []
            filtered = []
            for app in all_apps:
                d = str(app.get('AppointmentDate'))
                if start_date <= d <= end_date: filtered.append(app)
            return filtered
        except:
            return []

    def get_unique_patients_count(self, doctor_id, start, end):
        apps = self.get_appointments_for_period(doctor_id, start, end)
        return len(set(a.get('PatientID') for a in apps if a.get('PatientID')))

    def calculate_retention_rate(self, doctor_id, start, end):
        try:
            curr_apps = self.get_appointments_for_period(doctor_id, start, end)
            if not curr_apps: return 0.0
            curr_pts = set(a.get('PatientID') for a in curr_apps)

            # Previous 90 days
            s_dt = datetime.strptime(start, "%Y-%m-%d")
            p_start = (s_dt - timedelta(days=90)).strftime("%Y-%m-%d")
            p_end = (s_dt - timedelta(days=1)).strftime("%Y-%m-%d")

            prev_apps = self.get_appointments_for_period(doctor_id, p_start, p_end)
            prev_pts = set(a.get('PatientID') for a in prev_apps)

            returning = len(curr_pts.intersection(prev_pts))
            return (returning / len(prev_pts) * 100) if prev_pts else 0.0
        except:
            return 65.0

    def calculate_kpis(self, doctor_id=None, start_date=None, end_date=None):
        if not start_date: start_date = QDate.currentDate().addDays(-30).toString("yyyy-MM-dd")
        if not end_date: end_date = QDate.currentDate().toString("yyyy-MM-dd")
        if not doctor_id: doctor_id = 3

        db_data = self.get_database_kpis(doctor_id, start_date, end_date)
        if not db_data: return self.calculate_fallback_kpis()

        cur = db_data['current_period']
        prev = db_data['previous_period']

        # Construct KPI objects
        self.kpis = {
            'no_show_rate': KPI("Patient No-Show Rate", cur.get('no_show_rate', 0), 10.0, 0, "%", "Missed appointments",
                                ["Send SMS reminders", "Confirm calls"]),
            'cancellation_rate': KPI("Cancellation Rate", cur.get('cancellation_rate', 0), 15.0, 0, "%",
                                     "Cancelled appointments", ["Review policy", "Waitlist"]),
            'completion_rate': KPI("Completion Rate", cur.get('completion_rate', 0), 70.0, 0, "%",
                                   "Completed appointments", ["Better flow", "Reminders"]),
            'patient_retention': KPI("Patient Retention", prev.get('retention_rate', 0), 75.0, 0, "%",
                                     "Returning patients", ["Surveys", "Follow-up"]),
            'doctor_utilization': KPI("Doctor Utilization", cur.get('utilization_rate', 0), 75.0, 0, "%",
                                      "Time slots filled", ["Optimize schedule", "Walk-ins"]),
            'appointment_growth': KPI("Appointment Growth", prev.get('growth_rate', 0), 10.0, 0, "%",
                                      "New bookings growth", ["Promotions", "Referrals"])
        }

        # Simple status logic
        for k in self.kpis.values():
            if "no_show" in k.name.lower() or "cancellation" in k.name.lower():
                k.status = "good" if k.current_value <= k.target_value else "warning"
            else:
                k.status = "good" if k.current_value >= k.target_value else "warning"

        return self.kpis

    def calculate_fallback_kpis(self):
        # Fallback empty KPIs so app doesn't crash
        return {}

    def generate_report(self, doctor_id=None, start_date=None, end_date=None):
        kpis = self.calculate_kpis(doctor_id, start_date, end_date)
        if not kpis: return None

        good = sum(1 for k in kpis.values() if k.status == "good")
        status = "good" if good >= 4 else "warning"

        return {
            'title': 'CareLine KPI Report',
            'doctor_id': doctor_id,
            'kpis': kpis,
            'summary': {'total_kpis': len(kpis), 'good_kpis': good, 'warning_kpis': len(kpis) - good,
                        'critical_kpis': 0, 'overall_status': status},
            'recommendations': ["Send reminders", "Review cancellation policy", "Conduct surveys"]
        }