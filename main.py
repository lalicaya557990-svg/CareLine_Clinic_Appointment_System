import sys
import os

# --- PATH FIXER: Force Python to see the root directory ---
# This fixes "ModuleNotFoundError: No module named 'controllers'"
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
# -----------------------------------------------------------

from PyQt6 import QtWidgets
from controllers.login_controller import LoginController
from controllers.patient_controller import PatientController
from controllers.doctor_controller import DoctorController

class MainApp:
    """Main application controller that manages all windows"""

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)

        # Create ONLY the login controller initially
        self.login_controller = LoginController(self)

        # Other controllers should be None until needed
        self.patient_controller = None
        self.doctor_controller = None

        # Current user info
        self.current_user = None
        self.user_type = None

        # Start with login window
        self.show_login()

    def show_login(self):
        """Show login window"""
        print("Showing login window...")

        if self.patient_controller:
            self.patient_controller.hide()
        if self.doctor_controller:
            self.doctor_controller.hide()

        self.login_controller.show()

    def show_patient_dashboard(self):
        """Show patient dashboard"""
        print("Showing patient dashboard...")

        if not self.patient_controller:
            print("Creating new PatientController...")
            self.patient_controller = PatientController(self)

        self.login_controller.hide()
        if self.doctor_controller:
            self.doctor_controller.hide()

        self.patient_controller.show()
        print("Patient dashboard shown!")

    def show_doctor_dashboard(self):
        """Show doctor dashboard"""
        print("Showing doctor dashboard...")

        if not self.doctor_controller:
            print("Creating new DoctorController...")
            self.doctor_controller = DoctorController(self)

        self.login_controller.hide()
        if self.patient_controller:
            self.patient_controller.hide()

        self.doctor_controller.show()
        print("Doctor dashboard shown!")

    def handle_successful_login(self, user_type, user_data):
        """Handle successful login"""
        print(f"\n=== LOGIN SUCCESSFUL ===")
        print(f"User type: {user_type}")
        print(f"User data: {user_data}")
        print("=========================\n")

        self.user_type = user_type
        self.current_user = user_data

        if user_type == "patient":
            if not self.patient_controller:
                self.patient_controller = PatientController(self)
            self.patient_controller.set_user_data(user_data)
            self.show_patient_dashboard()
        elif user_type == "doctor":
            if not self.doctor_controller:
                self.doctor_controller = DoctorController(self)
            self.doctor_controller.set_user_data(user_data)
            self.show_doctor_dashboard()

    def handle_logout(self):
        """Handle logout"""
        print("Logging out...")

        self.current_user = None
        self.user_type = None

        # Close all windows and show login
        if self.patient_controller:
            self.patient_controller.hide()
        if self.doctor_controller:
            self.doctor_controller.hide()

        # Clear login fields
        self.login_controller.ui.lineEdit.clear()
        self.login_controller.ui.lineEdit_2.clear()
        self.login_controller.ui.checkBox.setChecked(False)

        # Show login window
        self.show_login()

    def run(self):
        """Run the application"""
        print("Starting CareLine Appointment System...")
        sys.exit(self.app.exec())


if __name__ == "__main__":
    print("Starting CareLine Appointment System...")
    main_app = MainApp()
    main_app.run()