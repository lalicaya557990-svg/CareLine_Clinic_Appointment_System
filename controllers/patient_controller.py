import os
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QDate, QTime

# MVC Imports
from views.patient_ui import Ui_Login as Ui_PatientWindow
from views.notification_window import NotificationWindow, NotificationButton
from models.database import DatabaseOperations


class PatientController(QtWidgets.QMainWindow):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.current_page = 0
        self.db_ops = DatabaseOperations()
        self.current_user = None

        self.ui = Ui_PatientWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("CareLine - Patient Dashboard")
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.initialize_basics()
        self.load_all_images(base_dir)
        self.setup_connections()
        self.add_patient_appointment_actions()
        self.add_notification_button()

        # Auto-Refresh Notifications
        self.notif_timer = QtCore.QTimer(self)
        self.notif_timer.timeout.connect(self.update_notification_badge)
        self.notif_timer.start(5000)

    # controllers/patient_controller.py

    def set_user_data(self, user_data):
        self.current_user = user_data
        self.prefill_profile_data()
        self.update_notification_badge()

        # --- ADD THIS LINE ---
        # Ensure the view refreshes with the new user context
        self.switch_to_page(0)
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
            if hasattr(self.ui, 'label_5'): self.ui.label_5.setPixmap(pixmap.scaled(151, 111))
            if hasattr(self.ui, 'label_6'): self.ui.label_6.setPixmap(pixmap.scaled(151, 111))
            if hasattr(self.ui, 'label_7'): self.ui.label_7.setPixmap(pixmap.scaled(151, 111))
            if hasattr(self.ui, 'label_9'): self.ui.label_9.setPixmap(pixmap.scaled(151, 111))

        doctor_img_path = os.path.join(images_dir, "doctor.png")
        if os.path.exists(doctor_img_path):
            pix = QPixmap(doctor_img_path).scaled(121, 131)
            if hasattr(self.ui, 'picDrLevi'): self.ui.picDrLevi.setPixmap(pix)
            if hasattr(self.ui, 'picDrChancee'): self.ui.picDrChancee.setPixmap(pix)

    def setup_connections(self):
        try:
            if hasattr(self.ui, 'pushButton_4'): self.ui.pushButton_4.clicked.connect(
                lambda: self.ui.stackedWidget.setCurrentIndex(0))
            if hasattr(self.ui, 'pushButton_5'): self.ui.pushButton_5.clicked.connect(
                lambda: self.ui.stackedWidget.setCurrentIndex(2))
            if hasattr(self.ui, 'pushButton_6'): self.ui.pushButton_6.clicked.connect(
                lambda: self.ui.stackedWidget.setCurrentIndex(3))
        except Exception:
            pass

        for attr_name in dir(self.ui):
            if not attr_name.startswith('_'):
                try:
                    attr = getattr(self.ui, attr_name)
                    if isinstance(attr, QtWidgets.QPushButton):
                        btn_text = attr.text().lower() if hasattr(attr, 'text') else ""
                        if "new appointment" in btn_text:
                            attr.clicked.connect(lambda: self.switch_to_page(0))
                        elif "my appointment" in btn_text:
                            attr.clicked.connect(lambda: self.switch_to_page(1))
                        elif "my profile" in btn_text or "profile" in btn_text:
                            attr.clicked.connect(lambda: self.switch_to_page(2))
                        elif "log out" in btn_text.lower():
                            # Connect to local confirmation method
                            attr.clicked.connect(self.confirm_logout)
                except Exception:
                    pass

        if hasattr(self.ui, 'saveappointment'): self.ui.saveappointment.clicked.connect(self.handle_save_appointment)
        if hasattr(self.ui, 'pushButton_10'): self.ui.pushButton_10.clicked.connect(self.handle_save_profile)

    def switch_to_page(self, page_index):
        if page_index < 0 or page_index >= self.ui.stackedWidget.count(): return
        self.ui.stackedWidget.setCurrentIndex(page_index)
        self.current_page = page_index
        self.update_nav_button_styles()
        if page_index == 1: self.refresh_appointments_table()

    def update_nav_button_styles(self):
        # Adds visual feedback to side menu buttons
        active_style = "QPushButton { background-color: #D3D3D3; color: black; border-radius: 15px; font-weight: bold; }"
        inactive_style = "QPushButton { background-color: transparent; color: black; border-radius: 15px; } QPushButton:hover { background-color: #E5E5E5; }"

        for attr_name in dir(self.ui):
            if not attr_name.startswith('_'):
                attr = getattr(self.ui, attr_name)
                if isinstance(attr, QtWidgets.QPushButton):
                    btn_text = attr.text().lower() if hasattr(attr, 'text') else ""
                    page = -1
                    if "new appointment" in btn_text:
                        page = 0
                    elif "my appointment" in btn_text:
                        page = 1
                    elif "my profile" in btn_text or "profile" in btn_text:
                        page = 2

                    if page != -1:
                        attr.setStyleSheet(active_style if self.current_page == page else inactive_style)

    def initialize_basics(self):
        if hasattr(self.ui, 'dateEdit'): self.ui.dateEdit.setDate(QDate.currentDate())
        if hasattr(self.ui, 'timeEdit_2'): self.ui.timeEdit_2.setTime(QTime(9, 0))
        if hasattr(self.ui, 'MyAppointments_3'):
            self.ui.MyAppointments_3.setColumnCount(4)
            self.ui.MyAppointments_3.setHorizontalHeaderLabels(["Date", "Time", "Doctor", "Status"])
            self.ui.MyAppointments_3.horizontalHeader().setStretchLastSection(True)
        self.switch_to_page(0)

    def refresh_appointments_table(self):
        if not self.current_user: return
        patient_id = self.current_user.get('patient_id')
        try:
            appointments = self.db_ops.get_patient_appointments(patient_id)
            if appointments:
                if self.ui.MyAppointments_3.columnCount() != 4:
                    self.ui.MyAppointments_3.setColumnCount(4)
                    self.ui.MyAppointments_3.setHorizontalHeaderLabels(["Date", "Time", "Doctor", "Status"])
                self.ui.MyAppointments_3.setRowCount(len(appointments))
                for row, appointment in enumerate(appointments):
                    date_str = str(appointment['AppointmentDate'])
                    time_str = str(appointment['AppointmentTime'])
                    self.ui.MyAppointments_3.setItem(row, 0, QtWidgets.QTableWidgetItem(date_str))
                    self.ui.MyAppointments_3.setItem(row, 1, QtWidgets.QTableWidgetItem(time_str))
                    self.ui.MyAppointments_3.setItem(row, 2, QtWidgets.QTableWidgetItem(appointment['DoctorName']))
                    status_item = QtWidgets.QTableWidgetItem(appointment['Status'])
                    self.ui.MyAppointments_3.setItem(row, 3, status_item)

                    st = appointment['Status'].lower()
                    if st == 'completed':
                        status_item.setForeground(QtGui.QColor("#10B981"))
                    elif st == 'accepted':
                        status_item.setForeground(QtGui.QColor("#3B82F6"))
                    elif st == 'pending':
                        status_item.setForeground(QtGui.QColor("#F59E0B"))
                    elif st == 'cancelled':
                        status_item.setForeground(QtGui.QColor("#EF4444"))
                    elif st == 'noshow':
                        status_item.setForeground(QtGui.QColor("#8B5CF6"))
            else:
                self.ui.MyAppointments_3.setRowCount(0)
        except Exception:
            pass

    # --- NOTIFICATIONS (RED THINGY) ---
    def add_notification_button(self):
        if hasattr(self.ui, 'centralwidget'):
            self.notif_btn = NotificationButton(self.ui.centralwidget)
            self.notif_btn.move(830, 30)  # Position Top Right
            self.notif_btn.clicked.connect(self.show_notifications)
            self.notif_btn.show()
            self.notif_btn.raise_()

    def update_notification_badge(self):
        if self.current_user and hasattr(self, 'notif_btn'):
            count = self.db_ops.get_unread_notification_count(self.current_user['patient_id'])
            self.notif_btn.set_count(count)

    def show_notifications(self):
        if not self.current_user: return
        self.notif_win = NotificationWindow(self.current_user['patient_id'], self)
        self.notif_win.exec()
        self.update_notification_badge()

    def handle_save_appointment(self):
        if not self.current_user: return
        doctor_id = None
        for attr_name in dir(self.ui):
            if not attr_name.startswith('_'):
                attr = getattr(self.ui, attr_name)
                if isinstance(attr, QtWidgets.QRadioButton) and attr.isChecked():
                    if "Levi" in attr_name:
                        doctor_id = 3
                    elif "Chancee" in attr_name or "Chi" in attr_name:
                        doctor_id = 4
                    break
        if not doctor_id:
            QtWidgets.QMessageBox.warning(self, "Select Doctor", "Please select a doctor")
            return

        date = self.ui.dateEdit.date().toString("yyyy-MM-dd")
        time = self.ui.timeEdit_2.time().toString("HH:mm:ss")

        if self.db_ops.create_appointment(self.current_user['patient_id'], doctor_id, date, time):
            self.db_ops.create_notification(doctor_id,
                                            f"New appointment: {self.current_user['name']} on {date} at {time}.")
            QtWidgets.QMessageBox.information(self, "Success", "Appointment Booked & Doctor Notified!")
            self.refresh_appointments_table()
            self.switch_to_page(1)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Failed to save appointment")

    def handle_save_profile(self):
        if not self.current_user: return
        fn = self.ui.lineEdit_7.text()
        ln = self.ui.lineEdit_8.text()
        ph = self.ui.lineEdit_9.text()
        em = self.ui.lineEdit_10.text()
        ad = self.ui.lineEdit_11.text()

        if not fn or not ln:
            QtWidgets.QMessageBox.warning(self, "Error", "Name required")
            return

        if self.db_ops.update_user_profile(self.current_user['user_id'], fn, ln, em, ph, ad):
            self.current_user.update({'name': f"{fn} {ln}", 'email': em, 'phone': ph, 'address': ad})
            QtWidgets.QMessageBox.information(self, "Success", "Profile Updated")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Failed to save")

    def add_patient_appointment_actions(self):
        if not hasattr(self.ui, 'MyAppointments_3'): return
        self.patient_appointment_action_frame = QtWidgets.QFrame(parent=self.ui.frame_3)
        self.patient_appointment_action_frame.setGeometry(QtCore.QRect(500, 10, 231, 31))
        self.patient_appointment_action_frame.setStyleSheet("background-color: transparent;")

        # --- UPDATE BUTTON (Blue -> Darker Blue -> Gray) ---
        self.update_appointment_btn = QtWidgets.QPushButton("Update", parent=self.patient_appointment_action_frame)
        self.update_appointment_btn.setGeometry(QtCore.QRect(0, 0, 70, 30))
        self.update_appointment_btn.setStyleSheet("""
            QPushButton { background-color: #3B82F6; color: white; border-radius: 6px; }
            QPushButton:hover { background-color: #2563EB; }
            QPushButton:disabled { background-color: #D1D5DB; color: #9CA3AF; }
        """)
        self.update_appointment_btn.clicked.connect(self.handle_update_appointment)

        # --- CANCEL BUTTON (Red -> Darker Red -> Gray) ---
        self.cancel_patient_appointment_btn = QtWidgets.QPushButton("Cancel",
                                                                    parent=self.patient_appointment_action_frame)
        self.cancel_patient_appointment_btn.setGeometry(QtCore.QRect(80, 0, 70, 30))
        self.cancel_patient_appointment_btn.setStyleSheet("""
            QPushButton { background-color: #EF4444; color: white; border-radius: 6px; }
            QPushButton:hover { background-color: #DC2626; }
            QPushButton:disabled { background-color: #D1D5DB; color: #9CA3AF; }
        """)
        self.cancel_patient_appointment_btn.clicked.connect(self.handle_cancel_patient_appointment)

        # --- DETAILS BUTTON (Gray -> Darker Gray -> Light Gray) ---
        self.view_details_btn = QtWidgets.QPushButton("Details", parent=self.patient_appointment_action_frame)
        self.view_details_btn.setGeometry(QtCore.QRect(160, 0, 70, 30))
        self.view_details_btn.setStyleSheet("""
            QPushButton { background-color: #6B7280; color: white; border-radius: 6px; }
            QPushButton:hover { background-color: #4B5563; }
            QPushButton:disabled { background-color: #D1D5DB; color: #9CA3AF; }
        """)
        self.view_details_btn.clicked.connect(self.handle_view_appointment_details)

        self.ui.MyAppointments_3.itemSelectionChanged.connect(self.update_patient_appointment_buttons)
        self.update_patient_appointment_buttons()

    def update_patient_appointment_buttons(self):
        """Enable buttons only if a row is selected and status is 'Pending'"""
        row = self.ui.MyAppointments_3.currentRow()

        # Default: Disable all
        self.update_appointment_btn.setEnabled(False)
        self.cancel_patient_appointment_btn.setEnabled(False)
        self.view_details_btn.setEnabled(False)

        if row != -1:
            # Details is always available if a row is selected
            self.view_details_btn.setEnabled(True)

            # Check Status for Update/Cancel
            status_item = self.ui.MyAppointments_3.item(row, 3)
            if status_item:
                status_text = status_item.text().lower()
                # Enable Update/Cancel only if status is pending
                if status_text == "pending":
                    self.update_appointment_btn.setEnabled(True)
                    self.cancel_patient_appointment_btn.setEnabled(True)

    def get_selected_appointment_id(self):
        row = self.ui.MyAppointments_3.currentRow()
        if row == -1: return None
        date = self.ui.MyAppointments_3.item(row, 0).text()
        time = self.ui.MyAppointments_3.item(row, 1).text()
        return self.db_ops.get_patient_appointment_id(self.current_user['patient_id'], date, time)

    def handle_cancel_patient_appointment(self):
        row = self.ui.MyAppointments_3.currentRow()
        if row == -1: return

        reply = QtWidgets.QMessageBox.question(self, "Cancel", "Cancel this appointment?",
                                               QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            aid = self.get_selected_appointment_id()
            if aid and self.db_ops.cancel_appointment(aid):
                QtWidgets.QMessageBox.information(self, "Success", "Cancelled")
                self.refresh_appointments_table()
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Failed to cancel")

    def handle_update_appointment(self):
        row = self.ui.MyAppointments_3.currentRow()
        if row == -1: return

        status_item = self.ui.MyAppointments_3.item(row, 3)
        if status_item and status_item.text().lower() != 'pending':
            QtWidgets.QMessageBox.warning(self, "Restricted", "Can only update Pending appointments.")
            return

        aid = self.get_selected_appointment_id()
        if not aid: return

        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("Reschedule")
        layout = QtWidgets.QVBoxLayout(dialog)

        de = QtWidgets.QDateEdit();
        de.setDate(QDate.currentDate());
        de.setCalendarPopup(True)
        te = QtWidgets.QTimeEdit();
        te.setTime(QTime(9, 0))

        bg = QtWidgets.QButtonGroup(dialog)
        r1 = QtWidgets.QRadioButton("Dr. Levi");
        r1.setChecked(True);
        bg.addButton(r1, 3)
        r2 = QtWidgets.QRadioButton("Dr. Chi");
        bg.addButton(r2, 4)

        layout.addWidget(QtWidgets.QLabel("New Date:"));
        layout.addWidget(de)
        layout.addWidget(QtWidgets.QLabel("New Time:"));
        layout.addWidget(te)
        layout.addWidget(QtWidgets.QLabel("Doctor:"));
        layout.addWidget(r1);
        layout.addWidget(r2)

        bb = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.StandardButton.Save | QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        bb.accepted.connect(dialog.accept);
        bb.rejected.connect(dialog.reject)
        layout.addWidget(bb)

        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            new_doc = bg.checkedId()
            new_d = de.date().toString("yyyy-MM-dd")
            new_t = te.time().toString("HH:mm:ss")
            if self.db_ops.reschedule_appointment(aid, new_d, new_t, new_doc):
                self.db_ops.create_notification(new_doc,
                                                f"Reschedule: {self.current_user['name']} to {new_d} at {new_t}.")
                QtWidgets.QMessageBox.information(self, "Success", "Rescheduled & Doctor Notified!")
                self.refresh_appointments_table()
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Failed to update")

    def handle_view_appointment_details(self):
        row = self.ui.MyAppointments_3.currentRow()
        if row == -1: return
        date = self.ui.MyAppointments_3.item(row, 0).text()
        time = self.ui.MyAppointments_3.item(row, 1).text()
        doc = self.ui.MyAppointments_3.item(row, 2).text()
        st = self.ui.MyAppointments_3.item(row, 3).text()
        QtWidgets.QMessageBox.information(self, "Details", f"Date: {date}\nTime: {time}\nDoctor: {doc}\nStatus: {st}")

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