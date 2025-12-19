import os
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QPixmap
from views.ui_files.doctor_ui import Ui_Login


class DoctorView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setWindowTitle("CareLine - Doctor Dashboard")
        self.setup_tables()
        self.load_images()
        self.add_kpi_buttons()
        self.add_action_buttons()
        self.add_noshow_buttons()

    def setup_tables(self):
        # Table setup logic from original DoctorWindow
        self.ui.tableTodayAppointments.setColumnCount(4)
        self.ui.tableTodayAppointments.setHorizontalHeaderLabels(["Time", "Patient", "Doctor", "Status"])
        self.ui.tableTodayAppointments.setColumnWidth(0, 150)
        self.ui.tableTodayAppointments.setColumnWidth(1, 200)

        self.ui.tableTodayAppointments_2.setColumnCount(6)
        self.ui.tableTodayAppointments_2.setHorizontalHeaderLabels(
            ["First Name", "Last Name", "Email", "Phone", "Date", "Time"])

        self.ui.tableTodayAppointments_3.setColumnCount(4)
        self.ui.tableTodayAppointments_3.setHorizontalHeaderLabels(["First Name", "Last Name", "Email", "Phone"])

    def load_images(self):
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        images_dir = os.path.join(current_dir, "images")

        logo_path = os.path.join(images_dir, "logoremover.png")
        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path).scaled(151, 111)
            for label in [self.ui.label_6, self.ui.label_7, self.ui.label_9, self.ui.label_12]:
                if hasattr(self.ui, label.objectName()):
                    label.setPixmap(pixmap)
            self.ui.label_5.setPixmap(QPixmap(logo_path).scaled(300, 111))

        # Load icons
        for icon, label_name in [("calendar.png", "picDrLevi"), ("completed.png", "picDrLevi_3"),
                                 ("audience.png", "picDrLevi_8")]:
            path = os.path.join(images_dir, icon)
            if os.path.exists(path) and hasattr(self.ui, label_name):
                getattr(self.ui, label_name).setPixmap(QPixmap(path).scaled(71, 71))

    def add_kpi_buttons(self):
        # Logic from kpi_ui_updates.py
        frames = [self.ui.frame, self.ui.frame_6, self.ui.frame_7, self.ui.frame_10]
        self.kpi_buttons = []
        for frame in frames:
            btn = QtWidgets.QPushButton("📊 KPI Reports", parent=frame)
            btn.setGeometry(QtCore.QRect(0, 330, 151, 41))
            btn.setStyleSheet(
                "QPushButton { background-color: transparent; color: black; border-radius: 15px; } QPushButton:hover { background-color: #D3D3D3; }")
            self.kpi_buttons.append(btn)

    def add_action_buttons(self):
        self.action_frame = QtWidgets.QFrame(parent=self.ui.frame_3)
        self.action_frame.setGeometry(QtCore.QRect(450, 10, 281, 31))
        self.action_frame.setStyleSheet("background-color: transparent;")

        self.confirm_btn = QtWidgets.QPushButton("Confirm", parent=self.action_frame)
        self.confirm_btn.setGeometry(QtCore.QRect(0, 0, 65, 30))
        self.confirm_btn.setStyleSheet("QPushButton { background-color: #10B981; color: white; border-radius: 6px; }")

        self.cancel_btn = QtWidgets.QPushButton("Cancel", parent=self.action_frame)
        self.cancel_btn.setGeometry(QtCore.QRect(70, 0, 65, 30))
        self.cancel_btn.setStyleSheet("QPushButton { background-color: #EF4444; color: white; border-radius: 6px; }")

        self.noshow_btn = QtWidgets.QPushButton("No Show", parent=self.action_frame)
        self.noshow_btn.setGeometry(QtCore.QRect(140, 0, 65, 30))
        self.noshow_btn.setStyleSheet("QPushButton { background-color: #F59E0B; color: white; border-radius: 6px; }")

        self.complete_btn = QtWidgets.QPushButton("Complete", parent=self.action_frame)
        self.complete_btn.setGeometry(QtCore.QRect(210, 0, 65, 30))
        self.complete_btn.setStyleSheet("QPushButton { background-color: #3B82F6; color: white; border-radius: 6px; }")

    def add_noshow_buttons(self):
        frames = [self.ui.frame, self.ui.frame_6, self.ui.frame_7, self.ui.frame_10]
        self.noshow_report_buttons = []
        for frame in frames:
            btn = QtWidgets.QPushButton("🚨 No-Show Reports", parent=frame)
            btn.setGeometry(QtCore.QRect(0, 380, 151, 41))
            btn.setStyleSheet(
                "QPushButton { background-color: transparent; color: black; border-radius: 15px; } QPushButton:hover { background-color: #D3D3D3; }")
            self.noshow_report_buttons.append(btn)