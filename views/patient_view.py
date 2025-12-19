import os
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QPixmap
from views.ui_files.patient_ui import Ui_Login


class PatientView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setWindowTitle("CareLine - Patient Dashboard")
        self.setup_tables()
        self.load_images()
        self.add_action_buttons()

    def setup_tables(self):
        if hasattr(self.ui, 'MyAppointments_3'):
            self.ui.MyAppointments_3.setColumnCount(4)
            self.ui.MyAppointments_3.setHorizontalHeaderLabels(["Date", "Time", "Doctor", "Status"])
            self.ui.MyAppointments_3.horizontalHeader().setStretchLastSection(True)

    def load_images(self):
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        images_dir = os.path.join(current_dir, "images")

        logo_path = os.path.join(images_dir, "logoremover.png")
        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path).scaled(151, 111)
            for label in [self.ui.label_5, self.ui.label_6, self.ui.label_7, self.ui.label_9]:
                if hasattr(self.ui, label.objectName()):
                    label.setPixmap(pixmap)

        doctor_img = os.path.join(images_dir, "doctor.png")
        if os.path.exists(doctor_img):
            pixmap = QPixmap(doctor_img).scaled(121, 131)
            self.ui.picDrLevi.setPixmap(pixmap)
            self.ui.picDrChancee.setPixmap(pixmap)

    def add_action_buttons(self):
        # Logic extracted from add_patient_appointment_actions
        self.patient_appointment_action_frame = QtWidgets.QFrame(parent=self.ui.frame_3)
        self.patient_appointment_action_frame.setGeometry(QtCore.QRect(500, 10, 231, 31))
        self.patient_appointment_action_frame.setStyleSheet("background-color: transparent;")

        self.update_btn = QtWidgets.QPushButton("Update", parent=self.patient_appointment_action_frame)
        self.update_btn.setGeometry(QtCore.QRect(0, 0, 70, 30))
        self.update_btn.setStyleSheet("QPushButton { background-color: #3B82F6; color: white; border-radius: 6px; }")

        self.cancel_btn = QtWidgets.QPushButton("Cancel", parent=self.patient_appointment_action_frame)
        self.cancel_btn.setGeometry(QtCore.QRect(80, 0, 70, 30))
        self.cancel_btn.setStyleSheet("QPushButton { background-color: #EF4444; color: white; border-radius: 6px; }")

        self.details_btn = QtWidgets.QPushButton("Details", parent=self.patient_appointment_action_frame)
        self.details_btn.setGeometry(QtCore.QRect(160, 0, 70, 30))
        self.details_btn.setStyleSheet("QPushButton { background-color: #6B7280; color: white; border-radius: 6px; }")