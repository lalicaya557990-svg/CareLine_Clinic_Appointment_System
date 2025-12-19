import os
from PyQt6 import QtWidgets, QtGui, QtCore
from models.kpi_model import KPIReportGenerator  # Just for type hinting or logic usage


class KPIView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CareLine - KPI Reports")
        self.setGeometry(100, 100, 1200, 800)
        self.setup_ui()

    def setup_ui(self):
        central = QtWidgets.QWidget()
        self.setCentralWidget(central)
        self.main_layout = QtWidgets.QVBoxLayout(central)

        # Header
        header_frame = QtWidgets.QFrame()
        header_frame.setStyleSheet(
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #4F46E5, stop:1 #7C3AED); border-radius: 15px;")
        header_layout = QtWidgets.QHBoxLayout(header_frame)
        title = QtWidgets.QLabel("📊 KPI DASHBOARD")
        title.setStyleSheet("font-size: 26px; font-weight: bold; color: white;")
        header_layout.addWidget(title)
        self.main_layout.addWidget(header_frame)

        # Controls
        control_frame = QtWidgets.QFrame()
        control_layout = QtWidgets.QHBoxLayout(control_frame)

        self.start_date = QtWidgets.QDateEdit()
        self.start_date.setDate(QtCore.QDate.currentDate().addDays(-30))
        self.start_date.setCalendarPopup(True)

        self.end_date = QtWidgets.QDateEdit()
        self.end_date.setDate(QtCore.QDate.currentDate())
        self.end_date.setCalendarPopup(True)

        self.generate_btn = QtWidgets.QPushButton("🔄 GENERATE")
        self.export_btn = QtWidgets.QPushButton("📥 EXPORT")

        control_layout.addWidget(QtWidgets.QLabel("From:"))
        control_layout.addWidget(self.start_date)
        control_layout.addWidget(QtWidgets.QLabel("To:"))
        control_layout.addWidget(self.end_date)
        control_layout.addWidget(self.generate_btn)
        control_layout.addWidget(self.export_btn)
        self.main_layout.addWidget(control_frame)

        # Content Area
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.content_widget = QtWidgets.QWidget()
        self.content_layout = QtWidgets.QVBoxLayout(self.content_widget)
        self.scroll_area.setWidget(self.content_widget)
        self.main_layout.addWidget(self.scroll_area)