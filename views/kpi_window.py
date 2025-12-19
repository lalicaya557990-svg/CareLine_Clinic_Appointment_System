import json
import os
import sys

from PyQt6 import QtWidgets, QtCore, QtGui, QtPrintSupport
from PyQt6.QtCore import QDate, Qt

# --- MATPLOTLIB IMPORTS FOR GRAPH ---
import matplotlib

matplotlib.use('QtAgg')
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
# ------------------------------------

# MVC Imports
from models.kpi_model import KPIReportGenerator
from models.database import DatabaseOperations


class KPICard(QtWidgets.QFrame):
    """
    Custom Clickable Widget for KPI.
    Requirement: Name on Top-Left, Value on Bottom-Right.
    """
    clicked = QtCore.pyqtSignal(object)

    def __init__(self, kpi_data):
        super().__init__()
        self.kpi_data = kpi_data
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMinimumHeight(140)
        self.setMaximumHeight(160)

        # Determine color based on status
        colors = {
            "good": "#10B981",  # Green
            "warning": "#F59E0B",  # Orange
            "critical": "#EF4444",  # Red
            "neutral": "#6B7280"  # Gray
        }
        accent_color = colors.get(kpi_data.status, "#6B7280")

        # Stylesheet
        self.setStyleSheet(f"""
            QFrame {{
                background-color: white;
                border: 1px solid #E5E7EB;
                border-radius: 12px;
                border-left: 6px solid {accent_color};
            }}
            QFrame:hover {{
                background-color: #F8FAFC;
                border: 1px solid {accent_color};
            }}
        """)

        # Layout
        layout = QtWidgets.QVBoxLayout(self)

        # 1. Top Left: String (Name)
        name_label = QtWidgets.QLabel(kpi_data.name)
        name_label.setStyleSheet(
            "border: none; background: transparent; font-size: 15px; font-weight: bold; color: #334155;")
        name_label.setWordWrap(True)
        name_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(name_label)

        layout.addStretch()

        # 2. Bottom Right: Numeric (Value)
        value_text = f"{kpi_data.current_value}{kpi_data.unit}"
        value_label = QtWidgets.QLabel(value_text)
        value_label.setStyleSheet(
            f"border: none; background: transparent; font-size: 32px; font-weight: 800; color: {accent_color};")
        value_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(value_label)

    def mousePressEvent(self, event):
        self.clicked.emit(self.kpi_data)
        super().mousePressEvent(event)


class KPIGraphWidget(FigureCanvasQTAgg):
    """
    Matplotlib Graph Widget to visualize KPI data
    """

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # Create Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)

        # Initialize Canvas
        super().__init__(self.fig)
        self.setParent(parent)

        # Initial Styling
        self.fig.patch.set_facecolor('#FFFFFF')  # White background
        self.axes.set_title("KPI Performance Overview", fontsize=12, pad=20, color='#334155', fontweight='bold')
        self.hide()  # Hide until data is loaded

    def update_chart(self, kpis_dict):
        self.axes.clear()
        self.show()

        # Filter: Only chart items with "%" unit to keep scale consistent
        # You can remove this filter if you want to chart everything
        names = []
        values = []
        colors = []

        for k in kpis_dict.values():
            if k.unit == "%":
                names.append(k.name.replace(" Rate", "").replace("Patient ", ""))  # Shorten names
                values.append(k.current_value)

                # Color based on status
                if k.status == 'good':
                    colors.append('#10B981')
                elif k.status == 'warning':
                    colors.append('#F59E0B')
                else:
                    colors.append('#EF4444')

        if not names:
            return

        # Create Bar Chart
        bars = self.axes.bar(names, values, color=colors, width=0.6)

        # Styling
        self.axes.set_ylabel('Percentage (%)', color='#64748B')
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['left'].set_color('#CBD5E1')
        self.axes.spines['bottom'].set_color('#CBD5E1')
        self.axes.tick_params(axis='x', colors='#334155', labelsize=9)
        self.axes.tick_params(axis='y', colors='#334155')

        # Add values on top of bars
        for bar in bars:
            height = bar.get_height()
            self.axes.text(bar.get_x() + bar.get_width() / 2., height + 1,
                           f'{height}%',
                           ha='center', va='bottom', fontsize=9, fontweight='bold', color='#334155')

        self.fig.tight_layout()
        self.draw()


class KPIReportDialog(QtWidgets.QDialog):
    """Detailed Report Popup"""

    def __init__(self, kpi_data, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Report: {kpi_data.name}")
        self.setMinimumWidth(500)
        self.setStyleSheet("background-color: white;")

        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        # Header
        header = QtWidgets.QLabel(f"📊 Report: {kpi_data.name}")
        header.setStyleSheet(
            "font-size: 20px; font-weight: bold; color: #4F46E5; border-bottom: 2px solid #F1F5F9; padding-bottom: 15px;")
        layout.addWidget(header)

        # Stats Grid
        grid_frame = QtWidgets.QFrame()
        grid_frame.setStyleSheet("background-color: #F8FAFC; border-radius: 8px; padding: 15px;")
        grid = QtWidgets.QGridLayout(grid_frame)

        def add_stat(l, v, r, c, col="#1E293B"):
            lbl = QtWidgets.QLabel(l)
            lbl.setStyleSheet("font-size: 11px; color: #64748B; font-weight: bold; text-transform: uppercase;")
            val = QtWidgets.QLabel(str(v))
            val.setStyleSheet(f"font-size: 22px; font-weight: bold; color: {col};")
            grid.addWidget(lbl, r * 2, c)
            grid.addWidget(val, r * 2 + 1, c)

        add_stat("Current Value", f"{kpi_data.current_value}{kpi_data.unit}", 0, 0, "#4F46E5")
        add_stat("Target", f"{kpi_data.target_value}{kpi_data.unit}", 0, 1)

        t_sym = "⬆" if kpi_data.trend > 0 else "⬇" if kpi_data.trend < 0 else "-"
        t_col = "#10B981" if kpi_data.trend > 0 else "#EF4444"
        add_stat("Trend", f"{t_sym} {abs(kpi_data.trend)}{kpi_data.unit}", 1, 0, t_col)

        s_col = "#10B981" if kpi_data.status == "good" else "#F59E0B" if kpi_data.status == "warning" else "#EF4444"
        add_stat("Status", kpi_data.status.upper(), 1, 1, s_col)

        layout.addWidget(grid_frame)

        # Description
        desc_lbl = QtWidgets.QLabel("Metric Description:")
        desc_lbl.setStyleSheet("font-weight: bold; margin-top: 10px; color: #334155;")
        layout.addWidget(desc_lbl)

        desc = QtWidgets.QLabel(kpi_data.description)
        desc.setWordWrap(True)
        desc.setStyleSheet("color: #475569; margin-bottom: 10px;")
        layout.addWidget(desc)

        # Recommendations
        if kpi_data.recommendations:
            rec_lbl = QtWidgets.QLabel("💡 Recommendations:")
            rec_lbl.setStyleSheet("font-weight: bold; margin-top: 5px; color: #059669;")
            layout.addWidget(rec_lbl)

            for rec in kpi_data.recommendations:
                item = QtWidgets.QLabel(f"• {rec}")
                item.setWordWrap(True)
                item.setStyleSheet("margin-left: 10px; color: #334155;")
                layout.addWidget(item)

        btn_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.StandardButton.Close)
        btn_box.rejected.connect(self.accept)
        layout.addWidget(btn_box)


class KPIWindow(QtWidgets.QMainWindow):
    """Main KPI Window"""

    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.kpi_generator = KPIReportGenerator(main_app)
        self.doctor_id = None
        self.report_data = None

        self.setWindowTitle("CareLine - KPI Reports (Database)")
        self.setGeometry(100, 100, 1100, 850)
        self.set_app_icon()
        self.setup_ui()
        QtCore.QTimer.singleShot(100, self.generate_report)

    def set_app_icon(self):
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            icon_path = os.path.join(base_dir, "images", "logoremover.png")
            if os.path.exists(icon_path):
                self.setWindowIcon(QtGui.QIcon(icon_path))
        except:
            pass

    def setup_ui(self):
        central = QtWidgets.QWidget()
        self.setCentralWidget(central)
        main_layout = QtWidgets.QVBoxLayout(central)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        # Header
        header_frame = QtWidgets.QFrame()
        header_frame.setStyleSheet(
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #4F46E5, stop:1 #7C3AED); border-radius: 12px; padding: 5px;")
        header_layout = QtWidgets.QHBoxLayout(header_frame)
        title_label = QtWidgets.QLabel("📊 DATABASE KPI DASHBOARD")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: white; padding: 5px;")
        header_layout.addWidget(title_label)
        main_layout.addWidget(header_frame)

        # Controls
        ctrl_frame = QtWidgets.QFrame()
        ctrl_frame.setStyleSheet(
            "background-color: #F8FAFC; border-radius: 10px; border: 1px solid #E2E8F0; padding: 5px;")
        ctrl_layout = QtWidgets.QHBoxLayout(ctrl_frame)

        self.start_date = QtWidgets.QDateEdit(QDate.currentDate().addDays(-30))
        self.start_date.setCalendarPopup(True)
        self.end_date = QtWidgets.QDateEdit(QDate.currentDate())
        self.end_date.setCalendarPopup(True)

        gen_btn = QtWidgets.QPushButton("🔄 GENERATE")
        gen_btn.clicked.connect(self.generate_report)
        gen_btn.setStyleSheet(
            "background-color: #10B981; color: white; border-radius: 6px; padding: 6px 12px; font-weight: bold;")

        print_btn = QtWidgets.QPushButton("🖨️ PRINT")
        print_btn.clicked.connect(self.print_report)
        print_btn.setStyleSheet(
            "background-color: #6366F1; color: white; border-radius: 6px; padding: 6px 12px; font-weight: bold;")

        ctrl_layout.addWidget(QtWidgets.QLabel("From:"))
        ctrl_layout.addWidget(self.start_date)
        ctrl_layout.addWidget(QtWidgets.QLabel("To:"))
        ctrl_layout.addWidget(self.end_date)
        ctrl_layout.addWidget(gen_btn)
        ctrl_layout.addWidget(print_btn)
        main_layout.addWidget(ctrl_frame)

        # Scroll Area
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("border: none; background: transparent;")

        self.content_widget = QtWidgets.QWidget()
        self.content_layout = QtWidgets.QVBoxLayout(self.content_widget)
        self.content_layout.setSpacing(20)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.scroll_area.setWidget(self.content_widget)
        main_layout.addWidget(self.scroll_area)

        # 1. Cards Grid Layout
        self.cards_container = QtWidgets.QWidget()
        self.cards_grid = QtWidgets.QGridLayout(self.cards_container)
        self.cards_grid.setSpacing(15)
        self.cards_grid.setContentsMargins(0, 0, 0, 0)
        self.content_layout.addWidget(self.cards_container)

        # 2. Graph Widget (Hidden initially)
        self.graph_widget = KPIGraphWidget(self.content_widget)
        self.graph_widget.setMinimumHeight(350)  # Set height for graph
        self.content_layout.addWidget(self.graph_widget)

        # Status Bar
        self.status_bar = QtWidgets.QStatusBar()
        self.setStatusBar(self.status_bar)

    def set_doctor_id(self, doctor_id):
        self.doctor_id = doctor_id

    def generate_report(self):
        # Clear existing cards
        while self.cards_grid.count():
            item = self.cards_grid.takeAt(0)
            if item.widget(): item.widget().deleteLater()

        if not self.doctor_id: return

        start = self.start_date.date().toString("yyyy-MM-dd")
        end = self.end_date.date().toString("yyyy-MM-dd")

        self.report_data = self.kpi_generator.generate_report(self.doctor_id, start, end)

        if not self.report_data:
            self.status_bar.showMessage("No data found")
            return

        # --- Populate Cards ---
        kpis = list(self.report_data['kpis'].values())
        row, col = 0, 0

        for kpi in kpis:
            card = KPICard(kpi)
            card.clicked.connect(self.open_detailed_report)
            self.cards_grid.addWidget(card, row, col)

            col += 1
            if col > 1:  # 2 cards per row
                col = 0
                row += 1

        # --- Update Graph ---
        self.graph_widget.update_chart(self.report_data['kpis'])

        self.status_bar.showMessage("✅ Report Generated.")

    def open_detailed_report(self, kpi_data):
        dialog = KPIReportDialog(kpi_data, self)
        dialog.exec()

    def print_report(self):
        if not self.report_data: return
        html = "<h1>KPI Report</h1><hr>"
        html += f"<p><b>Period:</b> {self.start_date.text()} - {self.end_date.text()}</p>"
        html += "<h2>Metric Summary</h2><table border='1' cellspacing='0' cellpadding='5' width='100%'>"
        html += "<tr><th>Metric</th><th>Value</th><th>Target</th><th>Status</th></tr>"
        for k in self.report_data['kpis'].values():
            html += f"<tr><td>{k.name}</td><td>{k.current_value}{k.unit}</td><td>{k.target_value}{k.unit}</td><td>{k.status.upper()}</td></tr>"
        html += "</table>"

        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterMode.HighResolution)
        dialog = QtPrintSupport.QPrintDialog(printer, self)
        if dialog.exec() == QtPrintSupport.QPrintDialog.DialogCode.Accepted:
            doc = QtGui.QTextDocument()
            doc.setHtml(html)
            doc.print(printer)