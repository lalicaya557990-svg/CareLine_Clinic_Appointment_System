import os
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QPixmap

# MVC Imports
from views.doctor_ui import Ui_Login as Ui_DoctorWindow
from views.notification_window import NotificationWindow, NotificationButton
from models.database import DatabaseOperations

# Import KPI and NoShow Windows
try:
    from views.kpi_window import KPIWindow

    KPI_AVAILABLE = True
except ImportError:
    KPI_AVAILABLE = False

try:
    from views.noshow_window import NoShowReportsWindow

    NOSHOW_REPORTS_AVAILABLE = True
except ImportError:
    NOSHOW_REPORTS_AVAILABLE = False


class DoctorController(QtWidgets.QMainWindow):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.kpi_window = None
        self.db_ops = DatabaseOperations()
        self.current_user = None

        self.ui = Ui_DoctorWindow()
        self.ui.setupUi(self)

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.setup_connections()
        self.load_all_images(base_dir)
        self.setWindowTitle("CareLine - Doctor Dashboard")
        self.initialize_doctor_ui()
        self.add_appointment_action_buttons()
        if NOSHOW_REPORTS_AVAILABLE:
            self.add_noshow_reports_button()
        self.add_notification_button()

        # Auto-Refresh Notifications
        self.notif_timer = QtCore.QTimer(self)
        self.notif_timer.timeout.connect(self.update_notification_badge)
        self.notif_timer.start(5000)

    def set_user_data(self, user_data):
        self.current_user = user_data
        self.prefill_profile_data()
        self.update_notification_badge()

        # --- ADD THIS LINE ---
        # Now that we have the user data, trigger the dashboard load
        self.show_page(0)

    def prefill_profile_data(self):
        try:
            for attr_name in dir(self.ui):
                if not attr_name.startswith('_'):
                    attr = getattr(self.ui, attr_name)
                    if isinstance(attr, QtWidgets.QLineEdit):
                        placeholder = attr.placeholderText().lower() if attr.placeholderText() else ""
                        if "first" in placeholder or "firstname" in attr_name.lower():
                            if 'name' in self.current_user:
                                name_parts = self.current_user['name'].split()
                                if name_parts: attr.setText(name_parts[0])
                        elif "last" in placeholder or "lastname" in attr_name.lower():
                            if 'name' in self.current_user:
                                name_parts = self.current_user['name'].split()
                                if len(name_parts) > 1: attr.setText(' '.join(name_parts[1:]))
                        elif "email" in placeholder:
                            if 'email' in self.current_user: attr.setText(self.current_user['email'])
                        elif "phone" in placeholder:
                            if 'phone' in self.current_user: attr.setText(self.current_user['phone'])
                        elif "address" in placeholder:
                            if 'address' in self.current_user: attr.setText(self.current_user['address'])
        except Exception:
            pass

    def load_all_images(self, base_dir):
        images_dir = os.path.join(base_dir, "images")
        if not os.path.exists(images_dir): return

        logo_path = os.path.join(images_dir, "logoremover.png")
        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path)
            if hasattr(self.ui, 'label_6'): self.ui.label_6.setPixmap(pixmap.scaled(151, 111))
            if hasattr(self.ui, 'label_7'): self.ui.label_7.setPixmap(pixmap.scaled(151, 111))
            if hasattr(self.ui, 'label_9'): self.ui.label_9.setPixmap(pixmap.scaled(151, 111))
            if hasattr(self.ui, 'label_12'): self.ui.label_12.setPixmap(pixmap.scaled(151, 111))
            if hasattr(self.ui, 'label_5'): self.ui.label_5.setPixmap(pixmap.scaled(300, 111))

        calendar_path = os.path.join(images_dir, "calendar.png")
        completed_path = os.path.join(images_dir, "completed.png")
        audience_path = os.path.join(images_dir, "audience.png")

        if os.path.exists(calendar_path) and hasattr(self.ui, 'picDrLevi'):
            self.ui.picDrLevi.setPixmap(QPixmap(calendar_path).scaled(71, 71))
        if os.path.exists(completed_path) and hasattr(self.ui, 'picDrLevi_3'):
            self.ui.picDrLevi_3.setPixmap(QPixmap(completed_path).scaled(71, 71))
        if os.path.exists(audience_path) and hasattr(self.ui, 'picDrLevi_8'):
            self.ui.picDrLevi_8.setPixmap(QPixmap(audience_path).scaled(71, 71))

    def setup_connections(self):
        for attr_name in dir(self.ui):
            if not attr_name.startswith('_'):
                attr = getattr(self.ui, attr_name)
                if isinstance(attr, QtWidgets.QPushButton):
                    btn_text = attr.text().lower()
                    if "dashboard" in btn_text:
                        attr.clicked.connect(lambda: self.show_page(0))
                    elif "appointment" in btn_text and "list" not in btn_text:
                        attr.clicked.connect(lambda: self.show_page(1))
                    elif "total client" in btn_text or "all client" in btn_text:
                        attr.clicked.connect(lambda: self.show_page(2))
                    elif "profile" in btn_text or "my profile" in btn_text:
                        attr.clicked.connect(lambda: self.show_page(3))
                    elif "log out" in btn_text:
                        # Connect to local confirmation method instead of direct logout
                        attr.clicked.connect(self.confirm_logout)
                    elif "kpi" in btn_text or "📊" in btn_text:
                        attr.clicked.connect(self.show_kpi_report)

        if hasattr(self.ui, 'pushButton_10'): self.ui.pushButton_10.clicked.connect(self.save_profile_changes)
        if hasattr(self.ui, 'pushButton_4'): self.ui.pushButton_4.clicked.connect(lambda: self.show_page(0))

    def show_kpi_report(self):
        if KPI_AVAILABLE:
            try:
                self.kpi_window = KPIWindow(self.main_app)
                doc_id = self.current_user.get('doctor_id') or self.current_user.get('user_id') or 3
                self.kpi_window.set_doctor_id(doc_id)
                self.kpi_window.show()
            except Exception as e:
                QtWidgets.QMessageBox.warning(self, "Error", f"KPI Error: {e}")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "KPI not available")

    def show_page(self, page_index):
        if 0 <= page_index < self.ui.stackedWidget.count():
            self.ui.stackedWidget.setCurrentIndex(page_index)
            self.update_button_styles(page_index)
            if page_index == 0:
                self.load_data_from_database()
                self.update_dashboard_counters()
            elif page_index == 1:
                self.load_appointment_list()
            elif page_index == 2:
                self.load_total_clients()

    def update_button_styles(self, active_page_index):
        active_style = "QPushButton { background-color: #D3D3D3; color: black; border-radius: 15px; font-weight: bold; }"
        inactive_style = "QPushButton { background-color: transparent; color: black; border-radius: 15px; } QPushButton:hover { background-color: #E5E5E5; }"
        for attr_name in dir(self.ui):
            if not attr_name.startswith('_'):
                attr = getattr(self.ui, attr_name)
                if isinstance(attr, QtWidgets.QPushButton):
                    btn_text = attr.text().lower()
                    is_nav = False
                    page = -1
                    if "dashboard" in btn_text:
                        is_nav, page = True, 0
                    elif "appointment" in btn_text and "list" not in btn_text:
                        is_nav, page = True, 1
                    elif "total client" in btn_text or "all client" in btn_text:
                        is_nav, page = True, 2
                    elif "profile" in btn_text or "my profile" in btn_text:
                        is_nav, page = True, 3

                    if is_nav:
                        attr.setStyleSheet(active_style if page == active_page_index else inactive_style)

    def initialize_doctor_ui(self):
        self.setup_tables()
        self.show_page(0)

    def setup_tables(self):
        if hasattr(self.ui, 'tableTodayAppointments'):
            self.ui.tableTodayAppointments.setColumnCount(4)
            self.ui.tableTodayAppointments.setHorizontalHeaderLabels(["Time", "Patient", "Doctor", "Status"])
        if hasattr(self.ui, 'tableTodayAppointments_2'):
            self.ui.tableTodayAppointments_2.setColumnCount(6)
            self.ui.tableTodayAppointments_2.setHorizontalHeaderLabels(
                ["First Name", "Last Name", "Email", "Phone", "Date", "Time"])
        if hasattr(self.ui, 'tableTodayAppointments_3'):
            self.ui.tableTodayAppointments_3.setColumnCount(4)
            self.ui.tableTodayAppointments_3.setHorizontalHeaderLabels(["First Name", "Last Name", "Email", "Phone"])

    def load_data_from_database(self):
        if not self.current_user: return
        doctor_id = self.current_user.get('doctor_id') or self.current_user.get('user_id')
        if hasattr(self.ui, 'tableTodayAppointments'):
            appointments = self.db_ops.get_todays_appointments_for_doctor(doctor_id)
            if appointments:
                self.ui.tableTodayAppointments.setRowCount(len(appointments))
                for row, appointment in enumerate(appointments):
                    self.ui.tableTodayAppointments.setItem(row, 0, QtWidgets.QTableWidgetItem(
                        str(appointment.get('AppointmentTime', ''))))
                    self.ui.tableTodayAppointments.setItem(row, 1, QtWidgets.QTableWidgetItem(
                        str(appointment.get('PatientName', ''))))
                    self.ui.tableTodayAppointments.setItem(row, 2, QtWidgets.QTableWidgetItem(
                        str(appointment.get('DoctorName', ''))))
                    status_item = QtWidgets.QTableWidgetItem(str(appointment.get('Status', '')))
                    self.ui.tableTodayAppointments.setItem(row, 3, status_item)

                    st = appointment.get('Status', '').lower()
                    if st == 'accepted':
                        status_item.setForeground(QtGui.QColor("#10B981"))
                    elif st == 'pending':
                        status_item.setForeground(QtGui.QColor("#F59E0B"))
                    elif st == 'completed':
                        status_item.setForeground(QtGui.QColor("#3B82F6"))
                    elif st == 'cancelled':
                        status_item.setForeground(QtGui.QColor("#EF4444"))
                    elif st == 'noshow':
                        status_item.setForeground(QtGui.QColor("#8B5CF6"))
            else:
                self.ui.tableTodayAppointments.setRowCount(0)

    def load_appointment_list(self):
        if not self.current_user: return
        doctor_id = self.current_user.get('doctor_id') or self.current_user.get('user_id')
        apps = self.db_ops.get_all_appointments_for_doctor(doctor_id)
        if hasattr(self.ui, 'tableTodayAppointments_2') and apps:
            self.ui.tableTodayAppointments_2.setRowCount(len(apps))
            for row, app in enumerate(apps):
                name = app.get('PatientName', '').split()
                fn = name[0] if name else ''
                ln = ' '.join(name[1:]) if len(name) > 1 else ''
                self.ui.tableTodayAppointments_2.setItem(row, 0, QtWidgets.QTableWidgetItem(fn))
                self.ui.tableTodayAppointments_2.setItem(row, 1, QtWidgets.QTableWidgetItem(ln))
                self.ui.tableTodayAppointments_2.setItem(row, 2,
                                                         QtWidgets.QTableWidgetItem(app.get('PatientEmail', '')))
                self.ui.tableTodayAppointments_2.setItem(row, 3,
                                                         QtWidgets.QTableWidgetItem(app.get('PatientPhone', '')))
                self.ui.tableTodayAppointments_2.setItem(row, 4, QtWidgets.QTableWidgetItem(
                    str(app.get('AppointmentDate', ''))))
                self.ui.tableTodayAppointments_2.setItem(row, 5, QtWidgets.QTableWidgetItem(
                    str(app.get('AppointmentTime', ''))))

    def load_total_clients(self):
        clients = self.db_ops.get_all_clients()
        if hasattr(self.ui, 'tableTodayAppointments_3') and clients:
            self.ui.tableTodayAppointments_3.setRowCount(len(clients))
            for row, client in enumerate(clients):
                name = client.get('PatientName', '').split()
                fn = name[0] if name else ''
                ln = ' '.join(name[1:]) if len(name) > 1 else ''
                self.ui.tableTodayAppointments_3.setItem(row, 0, QtWidgets.QTableWidgetItem(fn))
                self.ui.tableTodayAppointments_3.setItem(row, 1, QtWidgets.QTableWidgetItem(ln))
                self.ui.tableTodayAppointments_3.setItem(row, 2, QtWidgets.QTableWidgetItem(client.get('Email', '')))
                self.ui.tableTodayAppointments_3.setItem(row, 3, QtWidgets.QTableWidgetItem(client.get('Phone', '')))

    def update_dashboard_counters(self):
        if not self.current_user: return
        doc_id = self.current_user.get('doctor_id') or self.current_user.get('user_id')
        today = self.db_ops.get_todays_appointments_for_doctor(doc_id)
        if hasattr(self.ui, 'textDrLevi_2'): self.ui.textDrLevi_2.setText(str(len(today) if today else 0))
        completed = sum(1 for a in today if a.get('Status', '').lower() == 'completed') if today else 0
        if hasattr(self.ui, 'textDrLevi_5'): self.ui.textDrLevi_5.setText(str(completed))
        clients = self.db_ops.get_all_clients()
        if hasattr(self.ui, 'textDrLevi_15'): self.ui.textDrLevi_15.setText(str(len(clients) if clients else 0))

    def save_profile_changes(self):
        if not self.current_user: return
        fn = self.ui.lineEdit_7.text()
        ln = self.ui.lineEdit_8.text()
        ph = self.ui.lineEdit_9.text()
        em = self.ui.lineEdit_10.text()
        ad = self.ui.lineEdit_11.text()
        if not all([fn, ln, em]):
            QtWidgets.QMessageBox.warning(self, "Error", "Fill required fields")
            return
        res = self.db_ops.update_user_profile(self.current_user['user_id'], fn, ln, em, ph, ad)
        if res:
            self.current_user.update({'name': f"{fn} {ln}", 'email': em, 'phone': ph, 'address': ad})
            QtWidgets.QMessageBox.information(self, "Success", "Profile Updated")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Failed to save")

    # --- NOTIFICATIONS (RED THINGY) ---
    def add_notification_button(self):
        """Adds the bell button to the top right"""
        if hasattr(self.ui, 'centralwidget'):
            self.notif_btn = NotificationButton(self.ui.centralwidget)
            self.notif_btn.move(856, 30)
            self.notif_btn.clicked.connect(self.show_notifications)
            self.notif_btn.show()
            self.notif_btn.raise_()

    def update_notification_badge(self):
        if self.current_user and hasattr(self, 'notif_btn'):
            uid = self.current_user.get('doctor_id') or self.current_user.get('user_id')
            count = self.db_ops.get_unread_notification_count(uid)
            self.notif_btn.set_count(count)

    def show_notifications(self):
        if not self.current_user: return
        uid = self.current_user.get('doctor_id') or self.current_user.get('user_id')
        self.notif_win = NotificationWindow(uid, self)
        self.notif_win.exec()
        self.update_notification_badge()

    # --- APPOINTMENT ACTIONS ---
    def add_appointment_action_buttons(self):
        if not hasattr(self.ui, 'tableTodayAppointments'): return

        # --- FIXED GEOMETRY: Moved X to 390 and Width to 300 to fit all buttons ---
        self.appointment_action_frame = QtWidgets.QFrame(parent=self.ui.frame_3)
        self.appointment_action_frame.setGeometry(QtCore.QRect(390, 10, 300, 31))
        self.appointment_action_frame.setStyleSheet("background-color: transparent;")
        self.appointment_action_frame.raise_()
        self.appointment_action_frame.show()

        x, w, sp = 0, 70, 5  # Increased width slightly for text fit

        # --- CONFIRM (Green) ---
        self.confirm_btn = QtWidgets.QPushButton("Confirm", parent=self.appointment_action_frame)
        self.confirm_btn.setObjectName("confirm_btn")
        self.confirm_btn.setGeometry(QtCore.QRect(x, 0, w, 30));
        x += w + sp
        self.confirm_btn.setStyleSheet("""
            QPushButton { background-color: #10B981; color: white; border-radius: 6px; }
            QPushButton:hover { background-color: #059669; }
            QPushButton:disabled { background-color: #D1D5DB; color: #9CA3AF; }
        """)
        self.confirm_btn.clicked.connect(self.handle_confirm_appointment)
        self.confirm_btn.show()

        # --- CANCEL (Red) ---
        self.cancel_btn = QtWidgets.QPushButton("Cancel", parent=self.appointment_action_frame)
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.setGeometry(QtCore.QRect(x, 0, w, 30));
        x += w + sp
        self.cancel_btn.setStyleSheet("""
            QPushButton { background-color: #EF4444; color: white; border-radius: 6px; }
            QPushButton:hover { background-color: #DC2626; }
            QPushButton:disabled { background-color: #D1D5DB; color: #9CA3AF; }
        """)
        self.cancel_btn.clicked.connect(self.handle_cancel_appointment)
        self.cancel_btn.show()

        # --- NO SHOW (Yellow/Orange) ---
        self.noshow_btn = QtWidgets.QPushButton("No Show", parent=self.appointment_action_frame)
        self.noshow_btn.setObjectName("noshow_btn")
        self.noshow_btn.setGeometry(QtCore.QRect(x, 0, w, 30));
        x += w + sp
        self.noshow_btn.setStyleSheet("""
            QPushButton { background-color: #F59E0B; color: white; border-radius: 6px; }
            QPushButton:hover { background-color: #D97706; }
            QPushButton:disabled { background-color: #D1D5DB; color: #9CA3AF; }
        """)
        self.noshow_btn.clicked.connect(self.handle_noshow_appointment)
        self.noshow_btn.show()

        # --- COMPLETE (Blue) ---
        self.complete_btn = QtWidgets.QPushButton("Complete", parent=self.appointment_action_frame)
        self.complete_btn.setObjectName("complete_btn")
        self.complete_btn.setGeometry(QtCore.QRect(x, 0, w, 30))
        self.complete_btn.setStyleSheet("""
            QPushButton { background-color: #3B82F6; color: white; border-radius: 6px; }
            QPushButton:hover { background-color: #2563EB; }
            QPushButton:disabled { background-color: #D1D5DB; color: #9CA3AF; }
        """)
        self.complete_btn.clicked.connect(self.handle_complete_appointment)
        self.complete_btn.show()

        self.ui.tableTodayAppointments.itemSelectionChanged.connect(self.update_appointment_action_buttons)
        self.update_appointment_action_buttons()

    def update_appointment_action_buttons(self):
        """Enable/Disable buttons based on selection and appointment status"""
        if not hasattr(self, 'confirm_btn'): return
        row = self.ui.tableTodayAppointments.currentRow()

        # Default: Disable all
        for btn in [self.confirm_btn, self.cancel_btn, self.noshow_btn, self.complete_btn]:
            btn.setEnabled(False)

        if row != -1:
            status_item = self.ui.tableTodayAppointments.item(row, 3)
            if status_item:
                st = status_item.text().lower()

                # Logic:
                # Confirm: Only if 'pending'
                if st == "pending":
                    self.confirm_btn.setEnabled(True)

                # Cancel / NoShow: If pending, accepted, or confirmed (not if already completed/cancelled)
                if st in ["pending", "accepted", "confirmed"]:
                    self.cancel_btn.setEnabled(True)
                    self.noshow_btn.setEnabled(True)

                # Complete: If accepted or confirmed
                if st in ["accepted", "confirmed"]:
                    self.complete_btn.setEnabled(True)

    def get_appointment_id(self, row):
        try:
            time = self.ui.tableTodayAppointments.item(row, 0).text()
            pat = self.ui.tableTodayAppointments.item(row, 1).text()
            doc_id = self.current_user.get('doctor_id') or self.current_user.get('user_id')
            return self.db_ops.get_appointment_by_row_data(doc_id, pat, time)
        except:
            return None

    def handle_confirm_appointment(self):
        row = self.ui.tableTodayAppointments.currentRow()
        if row == -1: return
        pat = self.ui.tableTodayAppointments.item(row, 1).text()

        if QtWidgets.QMessageBox.question(self, "Confirm", f"Confirm {pat}?",
                                          QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No) == QtWidgets.QMessageBox.StandardButton.Yes:
            aid = self.get_appointment_id(row)
            if aid:
                self.db_ops.update_appointment_status(aid, 'accepted')
                self.ui.tableTodayAppointments.item(row, 3).setText("accepted")
                self.ui.tableTodayAppointments.item(row, 3).setForeground(QtGui.QColor("#10B981"))

                # NOTIFY PATIENT
                pid = self.db_ops.get_patient_id_from_appointment(aid)
                if pid: self.db_ops.create_notification(pid,
                                                        f"Your appointment with Dr. {self.current_user['name']} was CONFIRMED.")

                self.update_dashboard_counters()
                self.update_appointment_action_buttons()

    def handle_cancel_appointment(self):
        row = self.ui.tableTodayAppointments.currentRow()
        if row == -1: return
        reason, ok = QtWidgets.QInputDialog.getText(self, "Reason", "Reason:")
        if ok:
            aid = self.get_appointment_id(row)
            if aid:
                self.db_ops.update_appointment_status(aid, 'cancelled')
                self.ui.tableTodayAppointments.item(row, 3).setText("cancelled")
                self.ui.tableTodayAppointments.item(row, 3).setForeground(QtGui.QColor("#EF4444"))

                # NOTIFY PATIENT
                pid = self.db_ops.get_patient_id_from_appointment(aid)
                if pid: self.db_ops.create_notification(pid, f"Your appointment was CANCELLED. Reason: {reason}")

                self.update_dashboard_counters()
                self.update_appointment_action_buttons()

    def handle_noshow_appointment(self):
        row = self.ui.tableTodayAppointments.currentRow()
        if row == -1: return
        reason, ok = QtWidgets.QInputDialog.getText(self, "No-Show", "Reason:", text="Patient absent")
        if ok:
            aid = self.get_appointment_id(row)
            if aid:
                doc_id = self.current_user.get('doctor_id') or self.current_user.get('user_id')
                self.db_ops.mark_appointment_as_noshow(aid, doc_id, reason)
                self.ui.tableTodayAppointments.item(row, 3).setText("noshow")
                self.ui.tableTodayAppointments.item(row, 3).setForeground(QtGui.QColor("#F59E0B"))
                self.update_dashboard_counters()
                self.update_appointment_action_buttons()

    def handle_complete_appointment(self):
        row = self.ui.tableTodayAppointments.currentRow()
        if row == -1: return
        if QtWidgets.QMessageBox.question(self, "Complete", "Mark completed?",
                                          QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No) == QtWidgets.QMessageBox.StandardButton.Yes:
            aid = self.get_appointment_id(row)
            if aid:
                self.db_ops.update_appointment_status(aid, 'completed')
                self.ui.tableTodayAppointments.item(row, 3).setText("completed")
                self.ui.tableTodayAppointments.item(row, 3).setForeground(QtGui.QColor("#3B82F6"))
                self.update_dashboard_counters()
                self.update_appointment_action_buttons()

    def add_noshow_reports_button(self):
        frames = [
            (self.ui.frame, 380),
            (self.ui.frame_6, 380),
            (self.ui.frame_7, 380),
            (self.ui.frame_10, 380)
        ]
        for frame, y in frames:
            if hasattr(frame, 'geometry'):
                btn = QtWidgets.QPushButton(parent=frame)
                btn.setGeometry(QtCore.QRect(0, y, 151, 41))
                btn.setStyleSheet(
                    "QPushButton { background-color: transparent; color: black; border-radius: 15px; } QPushButton:hover { background-color: #D3D3D3; }")
                btn.setText("🚨 No-Show Reports")
                btn.clicked.connect(self.show_noshow_reports)

    def show_noshow_reports(self):
        try:
            doc_id = self.current_user.get('doctor_id') or self.current_user.get('user_id')
            self.noshow_window = NoShowReportsWindow(doc_id, self)
            self.noshow_window.show()
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def confirm_logout(self):
        """Show confirmation dialog before logging out"""
        reply = QtWidgets.QMessageBox.question(
            self,
            "Confirm Logout",
            "Are you sure you want to log out?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
            QtWidgets.QMessageBox.StandardButton.No
        )

        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            self.main_app.handle_logout()