import mysql.connector
from mysql.connector import Error
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'appointment',
    'port': 3306,
    'charset': 'utf8mb4',
    'use_unicode': True,
    'autocommit': True
}


class DatabaseConnection:
    """Base database connection class"""
    _instance = None
    _connection = None

    def connect(self):
        """Establish database connection"""
        try:
            if self._connection is None or not self._connection.is_connected():
                self._connection = mysql.connector.connect(**DB_CONFIG)
            return self._connection
        except Error as e:
            logger.error(f"❌ Error connecting to database: {e}")
            return None

    def execute_query(self, query, params=None, fetch_all=True):
        """Execute a query and return results"""
        connection = self.connect()
        if not connection:
            return None

        cursor = None
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, params or ())

            if query.strip().upper().startswith(('SELECT', 'SHOW', 'DESC')):
                if fetch_all:
                    result = cursor.fetchall()
                else:
                    result = cursor.fetchone()
                return result
            else:
                connection.commit()
                return cursor.rowcount
        except Error as e:
            logger.error(f"❌ Query execution error: {e}")
            logger.error(f"Query: {query}")
            return None
        finally:
            if cursor:
                cursor.close()


class DatabaseOperations(DatabaseConnection):
    """
    Database operations for the application.
    """

    def __init__(self):
        self.connect()
        self.initialize_notification_table()

    def initialize_notification_table(self):
        """Creates the Notification table if it doesn't exist"""
        query = """
                CREATE TABLE IF NOT EXISTS Notification \
                ( \
                    NotificationID \
                    INT \
                    AUTO_INCREMENT \
                    PRIMARY \
                    KEY, \
                    UserID \
                    INT \
                    NOT \
                    NULL, \
                    Message \
                    TEXT \
                    NOT \
                    NULL, \
                    IsRead \
                    BOOLEAN \
                    DEFAULT \
                    FALSE, \
                    CreatedAt \
                    TIMESTAMP \
                    DEFAULT \
                    CURRENT_TIMESTAMP, \
                    FOREIGN \
                    KEY \
                ( \
                    UserID \
                ) REFERENCES User \
                ( \
                    UserID \
                ) ON DELETE CASCADE
                    ) \
                """
        self.execute_query(query, fetch_all=False)

    # ================= AUTH & USER =================
    def authenticate_user(self, email, password):
        query = """
                SELECT u.UserID, \
                       u.FirstName, \
                       u.LastName, \
                       u.Email, \
                       u.UserType,
                       u.Phone, \
                       u.Address, \
                       d.Specialization, \
                       p.DateOfBirth, \
                       p.Gender
                FROM User u
                         LEFT JOIN Doctor d ON u.UserID = d.DoctorID AND u.UserType = 'D'
                         LEFT JOIN Patient p ON u.UserID = p.PatientID AND u.UserType = 'P'
                WHERE u.Email = %s \
                  AND u.Password = %s
                """
        return self.execute_query(query, (email, password), fetch_all=False)

    def register_patient(self, first_name, last_name, email, phone, address, password, dob=None, gender=None):
        try:
            user_query = "INSERT INTO User (FirstName, LastName, Email, Phone, Address, Password, UserType) VALUES (%s, %s, %s, %s, %s, %s, 'P')"
            if self.execute_query(user_query, (first_name, last_name, email, phone, address, password),
                                  fetch_all=False):
                user_id_res = self.execute_query("SELECT LAST_INSERT_ID() as UserID", fetch_all=False)
                if user_id_res:
                    pid = user_id_res['UserID']
                    pat_query = "INSERT INTO Patient (PatientID, DateOfBirth, Gender) VALUES (%s, %s, %s)"
                    if self.execute_query(pat_query, (pid, dob, gender), fetch_all=False):
                        return {"success": True, "message": "Registered successfully", "user_id": pid}
            return {"success": False, "message": "Failed to register"}
        except Exception as e:
            return {"success": False, "message": str(e)}

    def update_user_profile(self, user_id, first, last, email, phone, address):
        query = "UPDATE User SET FirstName=%s, LastName=%s, Email=%s, Phone=%s, Address=%s WHERE UserID=%s"
        return self.execute_query(query, (first, last, email, phone, address, user_id), fetch_all=False)

    def get_user_by_id(self, user_id):
        query = """
                SELECT u.*, d.Specialization, p.DateOfBirth, p.Gender
                FROM User u
                         LEFT JOIN Doctor d ON u.UserID = d.DoctorID
                         LEFT JOIN Patient p ON u.UserID = p.PatientID
                WHERE u.UserID = %s
                """
        return self.execute_query(query, (user_id,), fetch_all=False)

    # ================= APPOINTMENTS =================
    def create_appointment(self, patient_id, doctor_id, date, time):
        query = "INSERT INTO Appointment (PatientID, DoctorID, AppointmentDate, AppointmentTime, Status) VALUES (%s, %s, %s, %s, 'pending')"
        return self.execute_query(query, (patient_id, doctor_id, date, time), fetch_all=False)

    def get_patient_appointments(self, patient_id):
        query = """
                SELECT a.AppointmentID, \
                       a.AppointmentDate, \
                       TIME_FORMAT(a.AppointmentTime, '%h:%i %p') as AppointmentTime,
                       a.Status, \
                       CONCAT(u.FirstName, ' ', u.LastName)       as DoctorName
                FROM Appointment a
                         JOIN Doctor d ON a.DoctorID = d.DoctorID
                         JOIN User u ON d.DoctorID = u.UserID
                WHERE a.PatientID = %s
                ORDER BY a.AppointmentDate DESC, a.AppointmentTime DESC
                """
        return self.execute_query(query, (patient_id,))

    def get_todays_appointments_for_doctor(self, doctor_id):
        query = """
                SELECT a.AppointmentID, \
                       TIME_FORMAT(a.AppointmentTime, '%h:%i %p') as AppointmentTime,
                       CONCAT(u.FirstName, ' ', u.LastName)       as PatientName,
                       CONCAT(du.FirstName, ' ', du.LastName)     as DoctorName,
                       a.Status
                FROM Appointment a
                         JOIN Patient p ON a.PatientID = p.PatientID
                         JOIN User u ON p.PatientID = u.UserID
                         JOIN Doctor d ON a.DoctorID = d.DoctorID
                         JOIN User du ON d.DoctorID = du.UserID
                WHERE DATE (a.AppointmentDate) = CURDATE() AND a.DoctorID = %s
                ORDER BY a.AppointmentTime
                """
        return self.execute_query(query, (doctor_id,))

    def get_all_appointments_for_doctor(self, doctor_id):
        query = """
                SELECT a.AppointmentID, \
                       DATE_FORMAT(a.AppointmentDate, '%Y-%m-%d') as AppointmentDate,
                       TIME_FORMAT(a.AppointmentTime, '%h:%i %p') as AppointmentTime, \
                       a.Status,
                       CONCAT(u.FirstName, ' ', u.LastName)       as PatientName, \
                       u.Email                                    as PatientEmail, \
                       u.Phone                                    as PatientPhone
                FROM Appointment a
                         JOIN Patient p ON a.PatientID = p.PatientID
                         JOIN User u ON p.PatientID = u.UserID
                WHERE a.DoctorID = %s
                ORDER BY a.AppointmentDate DESC
                """
        return self.execute_query(query, (doctor_id,))

    def get_all_clients(self):
        query = """
                SELECT u.UserID, CONCAT(u.FirstName, ' ', u.LastName) as PatientName, u.Email, u.Phone
                FROM User u \
                         JOIN Patient p ON u.UserID = p.PatientID
                WHERE u.UserType = 'P'
                ORDER BY u.LastName
                """
        return self.execute_query(query)

    # ================= ACTIONS & HELPERS =================
    def update_appointment_status(self, appointment_id, status):
        query = "UPDATE Appointment SET Status = %s WHERE AppointmentID = %s"
        return self.execute_query(query, (status, appointment_id), fetch_all=False)

    def mark_appointment_as_noshow(self, appointment_id, doctor_id, reason=None):
        query = """
                UPDATE Appointment
                SET Status           = 'noshow', \
                    NoShowReason     = %s, \
                    MarkedAsNoShowBy = %s, \
                    MarkedAsNoShowAt = NOW()
                WHERE AppointmentID = %s
                """
        return self.execute_query(query, (reason, doctor_id, appointment_id), fetch_all=False)

    def reschedule_appointment(self, appointment_id, new_date, new_time, new_doctor_id):
        query = """
                UPDATE Appointment
                SET AppointmentDate = %s, \
                    AppointmentTime = %s, \
                    DoctorID        = %s, \
                    Status          = 'pending'
                WHERE AppointmentID = %s
                """
        return self.execute_query(query, (new_date, new_time, new_doctor_id, appointment_id), fetch_all=False)

    def cancel_appointment(self, appointment_id):
        query = "UPDATE Appointment SET Status = 'cancelled' WHERE AppointmentID = %s"
        return self.execute_query(query, (appointment_id,), fetch_all=False)

    def get_appointment_by_row_data(self, doctor_id, patient_name, appointment_time):
        """Find ID based on visual data (Doctor view)"""
        query = """
                SELECT a.AppointmentID
                FROM Appointment a
                         JOIN User u ON a.PatientID = u.UserID
                WHERE a.DoctorID = %s
                  AND CONCAT(u.FirstName, ' ', u.LastName) = %s
                  AND TIME_FORMAT(a.AppointmentTime, '%h:%i %p') = %s
                  AND DATE (a.AppointmentDate) = CURDATE()
                    LIMIT 1
                """
        result = self.execute_query(query, (doctor_id, patient_name, appointment_time), fetch_all=False)
        return result['AppointmentID'] if result else None

    def get_patient_appointment_id(self, patient_id, date_str, time_str):
        """Robust ID finding for Patient view"""
        try:
            query = """
                    SELECT AppointmentID, \
                           TIME_FORMAT(AppointmentTime, '%h:%i %p') as FormattedTime, \
                           AppointmentTime                          as RawTime
                    FROM Appointment
                    WHERE PatientID = %s \
                      AND AppointmentDate = %s
                    """
            results = self.execute_query(query, (patient_id, date_str))
            if not results: return None
            target = str(time_str).strip().lower()
            for row in results:
                formatted = str(row['FormattedTime']).strip().lower()
                raw = str(row['RawTime']).strip().lower()
                if target == formatted or target == raw:
                    return row['AppointmentID']
            if len(results) == 1: return results[0]['AppointmentID']
            return None
        except:
            return None

    # ================= REPORTS & KPI =================
    def calculate_noshow_rate(self, doctor_id, start_date, end_date):
        query = """
                SELECT COUNT(*)                                                                                      as total_appointments,
                       SUM(CASE WHEN Status = 'noshow' THEN 1 ELSE 0 END)                                            as noshow_count,
                       SUM(CASE WHEN Status = 'completed' THEN 1 ELSE 0 END)                                         as completed_count,
                       SUM(CASE WHEN Status = 'cancelled' THEN 1 ELSE 0 END)                                         as cancelled_count,
                       ROUND(SUM(CASE WHEN Status = 'noshow' THEN 1 ELSE 0 END) * 100.0 / NULLIF(COUNT(*), 0), \
                             1)                                                                                      as noshow_rate,
                       ROUND(SUM(CASE WHEN Status = 'completed' THEN 1 ELSE 0 END) * 100.0 / NULLIF(COUNT(*), 0), \
                             1)                                                                                      as completion_rate,
                       ROUND(SUM(CASE WHEN Status = 'cancelled' THEN 1 ELSE 0 END) * 100.0 / NULLIF(COUNT(*), 0), \
                             1)                                                                                      as cancellation_rate
                FROM Appointment
                WHERE DoctorID = %s \
                  AND AppointmentDate BETWEEN %s AND %s
                """
        result = self.execute_query(query, (doctor_id, start_date, end_date), fetch_all=False)
        if not result or result['total_appointments'] is None:
            return {'total_appointments': 0, 'noshow_count': 0, 'completed_count': 0, 'cancelled_count': 0,
                    'noshow_rate': 0.0, 'completion_rate': 0.0, 'cancellation_rate': 0.0}
        return result

    def get_noshow_appointments(self, doctor_id, start_date, end_date):
        query = """
                SELECT a.AppointmentDate, \
                       TIME_FORMAT(a.AppointmentTime, '%h:%i %p')           as AppointmentTime,
                       CONCAT(u.FirstName, ' ', u.LastName)                 as PatientName, \
                       u.Phone, \
                       u.Email,
                       a.NoShowReason, \
                       DATE_FORMAT(a.MarkedAsNoShowAt, '%Y-%m-%d %h:%i %p') as MarkedAsNoShowAt
                FROM Appointment a
                         JOIN User u ON a.PatientID = u.UserID
                WHERE a.DoctorID = %s \
                  AND a.Status = 'noshow' \
                  AND a.AppointmentDate BETWEEN %s AND %s
                ORDER BY a.AppointmentDate DESC
                """
        return self.execute_query(query, (doctor_id, start_date, end_date))

    # ================= NOTIFICATION SYSTEM =================

    def create_notification(self, user_id, message):
        query = "INSERT INTO Notification (UserID, Message) VALUES (%s, %s)"
        return self.execute_query(query, (user_id, message), fetch_all=False)

    def get_user_notifications(self, user_id):
        query = """
                SELECT NotificationID, Message, IsRead, DATE_FORMAT(CreatedAt, '%M %d, %h:%i %p') as Date
                FROM Notification \
                WHERE UserID = %s \
                ORDER BY CreatedAt DESC \
                """
        return self.execute_query(query, (user_id,))

    def mark_notification_read(self, notification_id):
        query = "UPDATE Notification SET IsRead = 1 WHERE NotificationID = %s"
        return self.execute_query(query, (notification_id,), fetch_all=False)

    def get_unread_notification_count(self, user_id):
        """Count unread notifications for the badge"""
        query = "SELECT COUNT(*) as count FROM Notification WHERE UserID = %s AND IsRead = 0"
        res = self.execute_query(query, (user_id,), fetch_all=False)
        return res['count'] if res else 0

    def get_patient_id_from_appointment(self, appointment_id):
        query = "SELECT PatientID FROM Appointment WHERE AppointmentID = %s"
        res = self.execute_query(query, (appointment_id,), fetch_all=False)
        return res['PatientID'] if res else None