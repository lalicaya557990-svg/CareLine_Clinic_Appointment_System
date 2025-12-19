# login_ui.py
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(787, 460)
        Login.setStyleSheet("QMainWindow {\n"
"    background-color: #8E9498;\n"
"}\n"
"#centralwidget {\n"
"    background-color: #8E9498;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=Login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(-10, 0, 121, 111))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/images/logo.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(80, 40, 131, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_8.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 40, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: transparent; /* Makes the background clear */\n"
"/* Optional: Makes it look like a link */\n"
"    color: White; /* Optional: Changes text color to blue like a link */\n"
"}\n"
"\n"
"/* Optional: Style for when the mouse is hovering over the button */\n"
"QPushButton:hover {\n"
"    background-color: #BF94E4;\n"
" /* Darker green on hover */\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 40, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: transparent; /* Makes the background clear */\n"
"/* Optional: Makes it look like a link */\n"
"    color: White; /* Optional: Changes text color to blue like a link */\n"
"}\n"
"\n"
"/* Optional: Style for when the mouse is hovering over the button */\n"
"QPushButton:hover {\n"
"    background-color: #BF94E4; /* Darker green on hover */\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(640, 40, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: transparent; /* Makes the background clear */\n"
"/* Optional: Makes it look like a link */\n"
"    color: White; /* Optional: Changes text color to blue like a link */\n"
"}\n"
"\n"
"/* Optional: Style for when the mouse is hovering over the button */\n"
"QPushButton:hover {\n"
"    background-color: #BF94E4; /* Darker green on hover */\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-20, 0, 801, 461))
        self.stackedWidget.setStyleSheet("QStackedWidget > QWidget {\n"
"    background-color: #8E9498;\n"
"}\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.homepage = QtWidgets.QWidget()
        self.homepage.setObjectName("homepage")
        self.label_4 = QtWidgets.QLabel(parent=self.homepage)
        self.label_4.setGeometry(QtCore.QRect(210, 80, 611, 341))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/images/loginxregister.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=self.homepage)
        self.label_6.setGeometry(QtCore.QRect(460, 120, 291, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.homepage)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 240, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFFFF; /* White background */\n"
"    border: 1px solid #CCCCCC; /* Light grey border */\n"
"    border-radius: 10px; /* Rounded corners (adjust as needed) */\n"
"    padding: 8px; /* Space inside the box so text isn\'t touching edges */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Dropdown shadow */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #0078D7; /* Highlight border when clicked/focused */\n"
"}\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.homepage)
        self.pushButton.setGeometry(QtCore.QRect(380, 290, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setUnderline(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    color: #6358DC;\n"
"    padding: 5px 10px;\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #0056b3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #004085;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.homepage)
        self.lineEdit.setGeometry(QtCore.QRect(380, 180, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFFFF; /* White background */\n"
"    border: 1px solid #CCCCCC; /* Light grey border */\n"
"    border-radius: 10px; /* Rounded corners (adjust as needed) */\n"
"    padding: 8px; /* Space inside the box so text isn\'t touching edges */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Dropdown shadow */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #0078D7; /* Highlight border when clicked/focused */\n"
"}\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.homepage)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 320, 351, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        self.pushButton_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #6358DC;\n"
"    border: none; /* Optional: Removes the default system border so the color shows fully */\n"
"}\n"
"QPushButton {\n"
"    padding: 15px 32px; /* Add padding for a better size */\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 10px;\n"
"    margin: 4px 2px;\n"
"    border-radius: 8px; /* Rounded corners */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #BF94E4; /* Darker green on hover */\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.homepage)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 360, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setUnderline(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    color: #6358DC;\n"
"    padding: 5px 10px;\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #0056b3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #004085;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7 = QtWidgets.QLabel(parent=self.homepage)
        self.label_7.setGeometry(QtCore.QRect(470, 360, 131, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_7.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.checkBox = QtWidgets.QCheckBox(parent=self.homepage)
        self.checkBox.setGeometry(QtCore.QRect(630, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.stackedWidget.addWidget(self.homepage)
        self.Register = QtWidgets.QWidget()
        self.Register.setObjectName("Register")
        self.label_23 = QtWidgets.QLabel(parent=self.Register)
        self.label_23.setGeometry(QtCore.QRect(460, 120, 291, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_23.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(15)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_22 = QtWidgets.QLabel(parent=self.Register)
        self.label_22.setGeometry(QtCore.QRect(470, 360, 131, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_22.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.Register)
        self.pushButton_8.setGeometry(QtCore.QRect(580, 360, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setUnderline(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    color: #6358DC;\n"
"    padding: 5px 10px;\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #0056b3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #004085;\n"
"}\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_21 = QtWidgets.QLabel(parent=self.Register)
        self.label_21.setGeometry(QtCore.QRect(210, 80, 611, 341))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        self.label_21.setFont(font)
        self.label_21.setAutoFillBackground(False)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap(":/images/loginxregister.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.Register)
        self.pushButton_10.setGeometry(QtCore.QRect(360, 320, 351, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        self.pushButton_10.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    background-color: #6358DC;\n"
"    border: none; /* Optional: Removes the default system border so the color shows fully */\n"
"}\n"
"QPushButton {\n"
"    padding: 15px 32px; /* Add padding for a better size */\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 10px;\n"
"    margin: 4px 2px;\n"
"    border-radius: 8px; /* Rounded corners */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #BF94E4; /* Darker green on hover */\n"
"}\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.Register)
        self.lineEdit_7.setGeometry(QtCore.QRect(350, 170, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFFFF; /* White background */\n"
"    border: 1px solid #CCCCCC; /* Light grey border */\n"
"    border-radius: 10px; /* Rounded corners (adjust as needed) */\n"
"    padding: 8px; /* Space inside the box so text isn\'t touching edges */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Dropdown shadow */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #0078D7; /* Highlight border when clicked/focused */\n"
"}\n"
"")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.Register)
        self.lineEdit_8.setGeometry(QtCore.QRect(550, 170, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFFFF; /* White background */\n"
"    border: 1px solid #CCCCCC; /* Light grey border */\n"
"    border-radius: 10px; /* Rounded corners (adjust as needed) */\n"
"    padding: 8px; /* Space inside the box so text isn\'t touching edges */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Dropdown shadow */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #0078D7; /* Highlight border when clicked/focused */\n"
"}\n"
"")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.Register)
        self.lineEdit_9.setGeometry(QtCore.QRect(350, 220, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFFFF; /* White background */\n"
"    border: 1px solid #CCCCCC; /* Light grey border */\n"
"    border-radius: 10px; /* Rounded corners (adjust as needed) */\n"
"    padding: 8px; /* Space inside the box so text isn\'t touching edges */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Dropdown shadow */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #0078D7; /* Highlight border when clicked/focused */\n"
"}\n"
"")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(parent=self.Register)
        self.lineEdit_10.setGeometry(QtCore.QRect(550, 220, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFFFF; /* White background */\n"
"    border: 1px solid #CCCCCC; /* Light grey border */\n"
"    border-radius: 10px; /* Rounded corners (adjust as needed) */\n"
"    padding: 8px; /* Space inside the box so text isn\'t touching edges */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Dropdown shadow */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #0078D7; /* Highlight border when clicked/focused */\n"
"}\n"
"")
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(parent=self.Register)
        self.lineEdit_11.setGeometry(QtCore.QRect(350, 270, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFFFF; /* White background */\n"
"    border: 1px solid #CCCCCC; /* Light grey border */\n"
"    border-radius: 10px; /* Rounded corners (adjust as needed) */\n"
"    padding: 8px; /* Space inside the box so text isn\'t touching edges */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Dropdown shadow */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #0078D7; /* Highlight border when clicked/focused */\n"
"}\n"
"")
        self.lineEdit_11.setText("")
        self.lineEdit_11.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_11.setCursorPosition(0)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(parent=self.Register)
        self.lineEdit_12.setGeometry(QtCore.QRect(550, 270, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFFFF; /* White background */\n"
"    border: 1px solid #CCCCCC; /* Light grey border */\n"
"    border-radius: 10px; /* Rounded corners (adjust as needed) */\n"
"    padding: 8px; /* Space inside the box so text isn\'t touching edges */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Dropdown shadow */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #0078D7; /* Highlight border when clicked/focused */\n"
"}\n"
"")
        self.lineEdit_12.setText("")
        self.lineEdit_12.setFrame(False)
        self.lineEdit_12.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.Register)
        self.pushButton_9.setGeometry(QtCore.QRect(550, 360, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setUnderline(True)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    color: #6358DC;\n"
"    padding: 5px 10px;\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #0056b3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #004085;\n"
"}\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_24 = QtWidgets.QLabel(parent=self.Register)
        self.label_24.setGeometry(QtCore.QRect(440, 360, 141, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_24.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(9)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_22.raise_()
        self.pushButton_8.raise_()
        self.label_21.raise_()
        self.pushButton_10.raise_()
        self.lineEdit_7.raise_()
        self.label_23.raise_()
        self.lineEdit_8.raise_()
        self.lineEdit_9.raise_()
        self.lineEdit_10.raise_()
        self.lineEdit_11.raise_()
        self.lineEdit_12.raise_()
        self.pushButton_9.raise_()
        self.label_24.raise_()
        self.stackedWidget.addWidget(self.Register)
        self.aboutus = QtWidgets.QWidget()
        self.aboutus.setObjectName("aboutus")
        self.label_2 = QtWidgets.QLabel(parent=self.aboutus)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 761, 301))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_2.setPalette(palette)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/contactus.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.aboutus)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 121, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_3.setPalette(palette)
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(parent=self.aboutus)
        self.label_10.setGeometry(QtCore.QRect(40, 170, 141, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        self.label_10.setPalette(palette)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.aboutus)
        self.label_11.setGeometry(QtCore.QRect(240, 170, 141, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        self.label_11.setPalette(palette)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.aboutus)
        self.label_12.setGeometry(QtCore.QRect(260, 170, 121, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_12.setPalette(palette)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.aboutus)
        self.label_13.setGeometry(QtCore.QRect(460, 170, 141, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        self.label_13.setPalette(palette)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.aboutus)
        self.label_14.setGeometry(QtCore.QRect(470, 170, 121, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_14.setPalette(palette)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.aboutus)
        self.label_15.setGeometry(QtCore.QRect(650, 170, 141, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        self.label_15.setPalette(palette)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.aboutus)
        self.label_16.setGeometry(QtCore.QRect(680, 170, 121, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_16.setPalette(palette)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=self.aboutus)
        self.label_17.setGeometry(QtCore.QRect(210, 320, 141, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        self.label_17.setPalette(palette)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.aboutus)
        self.label_18.setGeometry(QtCore.QRect(210, 320, 121, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_18.setPalette(palette)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(parent=self.aboutus)
        self.label_19.setGeometry(QtCore.QRect(500, 320, 121, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_19.setPalette(palette)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(parent=self.aboutus)
        self.label_20.setGeometry(QtCore.QRect(500, 320, 141, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        self.label_20.setPalette(palette)
        self.label_20.setObjectName("label_20")
        self.stackedWidget.addWidget(self.aboutus)
        self.contactus = QtWidgets.QWidget()
        self.contactus.setObjectName("contactus")
        self.label = QtWidgets.QLabel(parent=self.contactus)
        self.label.setGeometry(QtCore.QRect(100, 60, 661, 381))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/contact us.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(parent=self.contactus)
        self.label_9.setGeometry(QtCore.QRect(350, 130, 291, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_9.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.contactus)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 180, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFFFF; /* White background */\n"
"    border: 1px solid #CCCCCC; /* Light grey border */\n"
"    border-radius: 10px; /* Rounded corners (adjust as needed) */\n"
"    padding: 8px; /* Space inside the box so text isn\'t touching edges */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Dropdown shadow */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #0078D7; /* Highlight border when clicked/focused */\n"
"}\n"
"")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.contactus)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 230, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFFFF; /* White background */\n"
"    border: 1px solid #CCCCCC; /* Light grey border */\n"
"    border-radius: 10px; /* Rounded corners (adjust as needed) */\n"
"    padding: 8px; /* Space inside the box so text isn\'t touching edges */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Dropdown shadow */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #0078D7; /* Highlight border when clicked/focused */\n"
"}\n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.contactus)
        self.lineEdit_5.setGeometry(QtCore.QRect(240, 280, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFFFF; /* White background */\n"
"    border: 1px solid #CCCCCC; /* Light grey border */\n"
"    border-radius: 10px; /* Rounded corners (adjust as needed) */\n"
"    padding: 8px; /* Space inside the box so text isn\'t touching edges */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Dropdown shadow */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #0078D7; /* Highlight border when clicked/focused */\n"
"}\n"
"")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.contactus)
        self.pushButton_7.setGeometry(QtCore.QRect(250, 330, 341, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(99, 88, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        self.pushButton_7.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    background-color: #6358DC;\n"
"    border: none; /* Optional: Removes the default system border so the color shows fully */\n"
"}\n"
"QPushButton {\n"
"    padding: 15px 32px; /* Add padding for a better size */\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 10px;\n"
"    margin: 4px 2px;\n"
"    border-radius: 8px; /* Rounded corners */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #BF94E4; /* Darker green on hover */\n"
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.textEdit = QtWidgets.QTextEdit(parent=self.contactus)
        self.textEdit.setGeometry(QtCore.QRect(430, 180, 161, 141))
        self.textEdit.setStyleSheet("QTextEdit {\n"
"    background-color: #FFFFFF; /* White background */\n"
"    border: 1px solid #CCCCCC; /* Light grey border */\n"
"    border-radius: 10px; /* Rounded corners (adjust as needed) */\n"
"    padding: 8px; /* Space inside the box so text isn\'t touching edges */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Dropdown shadow */\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 1px solid #0078D7; /* Highlight border when clicked/focused */\n"
"}\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.stackedWidget.addWidget(self.contactus)
        self.stackedWidget.raise_()
        self.label_5.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.label_8.raise_()
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.label_8.setText(_translate("Login", "CARELINE"))
        self.pushButton_4.setText(_translate("Login", "Home"))
        self.pushButton_5.setText(_translate("Login", "About Us"))
        self.pushButton_6.setText(_translate("Login", "Contact Us"))
        self.label_6.setText(_translate("Login", "Welcome to CareLine"))
        self.lineEdit_2.setPlaceholderText(_translate("Login", " Password"))
        self.pushButton.setText(_translate("Login", "Forgot Password?"))
        self.lineEdit.setPlaceholderText(_translate("Login", " Username"))
        self.pushButton_2.setText(_translate("Login", "Login"))
        self.pushButton_3.setText(_translate("Login", "Register"))
        self.label_7.setText(_translate("Login", "Dont have an account?"))
        self.checkBox.setText(_translate("Login", "Remember me"))
        self.label_23.setText(_translate("Login", "Patient Register"))
        self.label_22.setText(_translate("Login", "Dont have an account?"))
        self.pushButton_8.setText(_translate("Login", "Register"))
        self.pushButton_10.setText(_translate("Login", "Register"))
        self.lineEdit_7.setPlaceholderText(_translate("Login", " First Name"))
        self.lineEdit_8.setPlaceholderText(_translate("Login", " Last Name"))
        self.lineEdit_9.setPlaceholderText(_translate("Login", " Email"))
        self.lineEdit_10.setPlaceholderText(_translate("Login", " Phone Number"))
        self.lineEdit_11.setPlaceholderText(_translate("Login", " Password"))
        self.lineEdit_12.setPlaceholderText(_translate("Login", " Confirm Password"))
        self.pushButton_9.setText(_translate("Login", "Login"))
        self.label_24.setText(_translate("Login", "Already have an account?"))
        self.label_3.setText(_translate("Login", "Make An Appointment"))
        self.label_10.setText(_translate("Login", "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. \n"
"Maecenas porttitor congue \n"
"massa."))
        self.label_11.setText(_translate("Login", "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. \n"
"Maecenas porttitor congue \n"
"massa."))
        self.label_12.setText(_translate("Login", "Help by Specialist"))
        self.label_13.setText(_translate("Login", "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. \n"
"Maecenas porttitor congue \n"
"massa."))
        self.label_14.setText(_translate("Login", "Get Diagnostic report"))
        self.label_15.setText(_translate("Login", "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. \n"
"Maecenas porttitor congue \n"
"massa."))
        self.label_16.setText(_translate("Login", "Medical Checkup"))
        self.label_17.setText(_translate("Login", "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. \n"
"Maecenas porttitor congue \n"
"massa."))
        self.label_18.setText(_translate("Login", "Example"))
        self.label_19.setText(_translate("Login", "Example"))
        self.label_20.setText(_translate("Login", "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. \n"
"Maecenas porttitor congue \n"
"massa."))
        self.label_9.setText(_translate("Login", "Drop Us A Message"))
        self.lineEdit_3.setPlaceholderText(_translate("Login", " Name"))
        self.lineEdit_4.setPlaceholderText(_translate("Login", " Email"))
        self.lineEdit_5.setPlaceholderText(_translate("Login", " Phone Number"))
        self.pushButton_7.setText(_translate("Login", "Send"))
        self.textEdit.setPlaceholderText(_translate("Login", "Note"))