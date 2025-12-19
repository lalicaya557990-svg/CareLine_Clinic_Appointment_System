import os
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtGui import QPixmap
from views.ui_files.appointment_login_ui import Ui_Login


class LoginView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setWindowTitle("CareLine - Appointment System")
        self.load_images()

    def load_images(self):
        # Image loading logic from original LoginWindow
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        images_dir = os.path.join(current_dir, "images")

        if os.path.exists(images_dir):
            logo_path = os.path.join(images_dir, "logo.png")
            if os.path.exists(logo_path):
                self.ui.label_5.setPixmap(QPixmap(logo_path).scaled(121, 111))

            login_img = os.path.join(images_dir, "loginxregister.png")
            if os.path.exists(login_img):
                pixmap = QPixmap(login_img).scaled(611, 341)
                self.ui.label_4.setPixmap(pixmap)
                self.ui.label_21.setPixmap(pixmap)

            self.ui.label_2.setPixmap(QPixmap(os.path.join(images_dir, "contactus.png")).scaled(750, 350))
            self.ui.label.setPixmap(QPixmap(os.path.join(images_dir, "contact us.png")).scaled(661, 381))