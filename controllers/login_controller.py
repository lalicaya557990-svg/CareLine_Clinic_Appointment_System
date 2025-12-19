import os
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtGui import QPixmap

# MVC Imports
from views.login_ui import Ui_Login  # Was appointment_login_ui
from models.database import DatabaseOperations


class LoginController(QtWidgets.QMainWindow):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.db_ops = DatabaseOperations()

        # Initialize UI from the generated Python class
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        # FIX: Path calculation for MVC structure
        # Current file is in /controllers, so we need to go up one level to find /images
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Setup connections
        self.setup_connections()

        # Load all images
        self.load_all_images(base_dir)

        # Set window title
        self.setWindowTitle("CareLine - Appointment System")

        # Start on homepage
        self.ui.stackedWidget.setCurrentIndex(0)

    def load_all_images(self, base_dir):
        """Load all images for the application"""
        images_dir = os.path.join(base_dir, "images")

        # Check if images directory exists
        if not os.path.exists(images_dir):
            print(f"Warning: Images directory not found: {images_dir}")
            return

        # Load logo image
        logo_files = ["logo.png", "logoremover.png"]
        for logo_file in logo_files:
            logo_path = os.path.join(images_dir, logo_file)
            if os.path.exists(logo_path):
                pixmap = QPixmap(logo_path)
                pixmap = pixmap.scaled(121, 111)  # Match the label size
                self.ui.label_5.setPixmap(pixmap)
                break

        # Load homepage image
        login_img_path = os.path.join(images_dir, "loginxregister.png")
        if os.path.exists(login_img_path):
            pixmap = QPixmap(login_img_path)
            pixmap = pixmap.scaled(611, 341)
            self.ui.label_4.setPixmap(pixmap)
            self.ui.label_21.setPixmap(pixmap)

        # Load about us page image
        about_img_path = os.path.join(images_dir, "contactus.png")
        if os.path.exists(about_img_path):
            pixmap = QPixmap(about_img_path)
            pixmap = pixmap.scaled(750, 350)
            self.ui.label_2.setPixmap(pixmap)

        # Load contact us page image
        contact_img_path = os.path.join(images_dir, "contact us.png")
        if os.path.exists(contact_img_path):
            pixmap = QPixmap(contact_img_path)
            pixmap = pixmap.scaled(661, 381)
            self.ui.label.setPixmap(pixmap)

    def setup_connections(self):
        """Setup navigation and authentication connections"""
        # Header navigation buttons
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))

        # Register button on login page
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

        # Login button on register page
        self.ui.pushButton_9.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

        # Login button (actual login functionality)
        self.ui.pushButton_2.clicked.connect(self.handle_login)

        # Register button (registration functionality)
        self.ui.pushButton_10.clicked.connect(self.handle_register)

        # Contact form send button
        self.ui.pushButton_7.clicked.connect(self.handle_contact_form)

    def handle_login(self):
        """Handle login attempt with database"""
        email = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if email and password:
            # Authenticate user from database
            user_data = self.db_ops.authenticate_user(email, password)

            if user_data:
                # Determine user type
                user_type = "doctor" if user_data['UserType'] == 'D' else "patient"

                # Store user data
                user_info = {
                    "user_id": user_data['UserID'],
                    "username": user_data['Email'],
                    "name": f"{user_data['FirstName']} {user_data['LastName']}",
                    "email": user_data['Email'],
                    "phone": user_data['Phone'],
                    "address": user_data['Address'],
                    "user_type": user_data['UserType']
                }

                # Add doctor-specific or patient-specific data
                if user_type == "doctor":
                    user_info["specialization"] = user_data.get('Specialization', '')
                    user_info["doctor_id"] = user_data['UserID']
                else:
                    user_info["date_of_birth"] = user_data.get('DateOfBirth', '')
                    user_info["gender"] = user_data.get('Gender', '')
                    user_info["patient_id"] = user_data['UserID']

                # Notify main app to switch to appropriate UI
                self.main_app.handle_successful_login(user_type, user_info)
            else:
                QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid email or password")
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Please enter email and password")

    def handle_register(self):
        """Handle registration with database"""
        first_name = self.ui.lineEdit_7.text()
        last_name = self.ui.lineEdit_8.text()
        email = self.ui.lineEdit_9.text()
        phone = self.ui.lineEdit_10.text()
        password = self.ui.lineEdit_11.text()
        confirm_password = self.ui.lineEdit_12.text()

        # Basic validation
        if not all([first_name, last_name, email, phone, password, confirm_password]):
            QtWidgets.QMessageBox.warning(self, "Registration Failed", "Please fill in all fields")
            return

        if password != confirm_password:
            QtWidgets.QMessageBox.warning(self, "Registration Failed", "Passwords do not match")
            return

        # Register patient in database
        result = self.db_ops.register_patient(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address="",
            password=password,
            date_of_birth=None,
            gender=None
        )

        if result and result["success"]:
            QtWidgets.QMessageBox.information(self, "Registration Successful", result["message"])
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.lineEdit.setText(email)
            self.ui.lineEdit_2.setText(password)
        else:
            QtWidgets.QMessageBox.warning(self, "Registration Failed",
                                          result["message"] if result else "Registration failed")

    def handle_contact_form(self):
        """Handle contact form submission"""
        name = self.ui.lineEdit_3.text()
        email = self.ui.lineEdit_4.text()
        phone = self.ui.lineEdit_5.text()
        note = self.ui.textEdit.toPlainText()

        if not all([name, email, phone, note]):
            QtWidgets.QMessageBox.warning(self, "Missing Information", "Please fill in all fields")
            return

        QtWidgets.QMessageBox.information(self, "Message Sent",
                                          "Thank you for your message! We'll get back to you soon.")