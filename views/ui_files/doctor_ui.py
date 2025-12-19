# doctor_ui.py - UPDATED WITH KPI BUTTON
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(891, 529)
        Login.setStyleSheet("QMainWindow {\n"
                            "    background-color: #8E9498;\n"
                            "}\n"
                            "#centralwidget {\n"
                            "    background-color: #8E9498;\n"
                            "}\n"
                            "")
        self.centralwidget = QtWidgets.QWidget(parent=Login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 300, 111))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/images/logoremover.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        # Add this line after creating the label or in your initialization method
        self.label_5.hide()
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 40, 131, 31))
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
        self.pushButton_4.setGeometry(QtCore.QRect(570, 40, 75, 24))
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
        self.pushButton_5.setGeometry(QtCore.QRect(670, 40, 75, 24))
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
        self.pushButton_6.setGeometry(QtCore.QRect(770, 40, 75, 24))
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
        self.stackedWidget.setGeometry(QtCore.QRect(-20, 0, 921, 541))
        self.stackedWidget.setStyleSheet("QStackedWidget > QWidget {\n"
                                         "    background-color: #8E9498;\n"
                                         "}\n"
                                         "")
        self.stackedWidget.setObjectName("stackedWidget")
        self.NewAppointment = QtWidgets.QWidget()
        self.NewAppointment.setObjectName("NewAppointment")
        self.frame = QtWidgets.QFrame(parent=self.NewAppointment)
        self.frame.setGeometry(QtCore.QRect(20, 90, 151, 441))
        self.frame.setStyleSheet("\n"
                                 "background-color: rgb(217, 219, 221);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setGeometry(QtCore.QRect(5, -10, 151, 111))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/images/logoremover.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 90, 151, 41))
        self.pushButton_3.setStyleSheet("/* Base style for the button */\n"
                                        "QPushButton {\n"
                                        "    /* Make the button transparent by default */\n"
                                        "  background-color: #D3D3D3; /* The light grey color from the picture */\n"
                                        "    color: black;              /* Keeps the text black */\n"
                                        "    /* Adjust border-radius to match the full rounding in the image */\n"
                                        "    border-radius: 15px;       \n"
                                        "}\n"
                                        "/* The style to use when the button is the active page (the \"checked\" state) */\n"
                                        "")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(0, 410, 151, 23))
        self.pushButton_12.setStyleSheet("QPushButton {\n"
                                         "    background-color: transparent;\n"
                                         "    border: none;\n"
                                         "    color: red;\n"
                                         "}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(0, 150, 151, 41))
        self.pushButton_11.setStyleSheet("/* Base style for the button */\n"
                                         "QPushButton {\n"
                                         "    /* Make the button transparent by default */\n"
                                         "  background-color: transparent; /* The light grey color from the picture */\n"
                                         "    color: black;              /* Keeps the text black */\n"
                                         "    /* Adjust border-radius to match the full rounding in the image */\n"
                                         "    border-radius: 15px;       \n"
                                         "}\n"
                                         "/* The style to use when the button is the active page (the \"checked\" state) */\n"
                                         "")
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setChecked(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(0, 270, 151, 41))
        self.pushButton_13.setStyleSheet("/* Base style for the button */\n"
                                         "QPushButton {\n"
                                         "    /* Make the button transparent by default */\n"
                                         "  background-color: #transparent; /* The light grey color from the picture */\n"
                                         "    color: black;              /* Keeps the text black */\n"
                                         "    /* Adjust border-radius to match the full rounding in the image */\n"
                                         "    border-radius: 15px;       \n"
                                         "}\n"
                                         "/* The style to use when the button is the active page (the \"checked\" state) */\n"
                                         "")
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setChecked(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_21 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_21.setGeometry(QtCore.QRect(0, 210, 151, 41))
        self.pushButton_21.setStyleSheet("/* Base style for the button */\n"
                                         "QPushButton {\n"
                                         "    /* Make the button transparent by default */\n"
                                         "  background-color: transparent; /* The light grey color from the picture */\n"
                                         "    color: black;              /* Keeps the text black */\n"
                                         "    /* Adjust border-radius to match the full rounding in the image */\n"
                                         "    border-radius: 15px;       \n"
                                         "}\n"
                                         "/* The style to use when the button is the active page (the \"checked\" state) */\n"
                                         "")
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.setChecked(False)
        self.pushButton_21.setObjectName("pushButton_21")

        # ADD KPI BUTTON TO DASHBOARD PAGE
        self.pushButton_kpi_dashboard = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_kpi_dashboard.setGeometry(QtCore.QRect(0, 330, 151, 41))
        self.pushButton_kpi_dashboard.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: black;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #D3D3D3;
            }
        """)
        self.pushButton_kpi_dashboard.setText("📊 KPI Reports")
        self.pushButton_kpi_dashboard.setCheckable(True)
        self.pushButton_kpi_dashboard.setChecked(False)
        self.pushButton_kpi_dashboard.setObjectName("pushButton_kpi_dashboard")

        self.frame_2 = QtWidgets.QFrame(parent=self.NewAppointment)
        self.frame_2.setGeometry(QtCore.QRect(170, 90, 751, 441))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.todaysAppointment = QtWidgets.QFrame(parent=self.frame_2)
        self.todaysAppointment.setGeometry(QtCore.QRect(10, 30, 231, 121))
        self.todaysAppointment.setStyleSheet("/* Doctor frames */\n"
                                             "QFrame#todaysAppointment, QFrame#CompletedAppointment{\n"
                                             "    background-color: white;\n"
                                             "    border: 1px solid #D1D5DB;\n"
                                             "    border-radius: 8px;\n"
                                             "    padding: 12px;\n"
                                             "    margin-bottom: 8px;\n"
                                             "}\n"
                                             "\n"
                                             "")
        self.todaysAppointment.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.todaysAppointment.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.todaysAppointment.setObjectName("todaysAppointment")
        self.textDrLevi_2 = QtWidgets.QLabel(parent=self.todaysAppointment)
        self.textDrLevi_2.setGeometry(QtCore.QRect(160, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textDrLevi_2.setFont(font)
        self.textDrLevi_2.setObjectName("textDrLevi_2")
        self.textDrLevi = QtWidgets.QLabel(parent=self.todaysAppointment)
        self.textDrLevi.setGeometry(QtCore.QRect(120, 20, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textDrLevi.setFont(font)
        self.textDrLevi.setWordWrap(True)
        self.textDrLevi.setObjectName("textDrLevi")
        self.picDrLevi = QtWidgets.QLabel(parent=self.todaysAppointment)
        self.picDrLevi.setGeometry(QtCore.QRect(30, 20, 71, 71))
        self.picDrLevi.setAutoFillBackground(False)
        self.picDrLevi.setText("")
        self.picDrLevi.setPixmap(QtGui.QPixmap(":/images/calendar.png"))
        self.picDrLevi.setScaledContents(True)
        self.picDrLevi.setObjectName("picDrLevi")
        self.CompletedAppointment = QtWidgets.QFrame(parent=self.frame_2)
        self.CompletedAppointment.setGeometry(QtCore.QRect(260, 30, 231, 121))
        self.CompletedAppointment.setStyleSheet("\n"
                                                "QFrame#todaysAppointment, QFrame#CompletedAppointment, QFrame#TotalClients{\n"
                                                "    background-color: white;\n"
                                                "    border: 1px solid #D1D5DB;\n"
                                                "    border-radius: 8px;\n"
                                                "    padding: 12px;\n"
                                                "    margin-bottom: 8px;\n"
                                                "}\n"
                                                "\n"
                                                "")
        self.CompletedAppointment.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.CompletedAppointment.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.CompletedAppointment.setObjectName("CompletedAppointment")
        self.textDrLevi_5 = QtWidgets.QLabel(parent=self.CompletedAppointment)
        self.textDrLevi_5.setGeometry(QtCore.QRect(160, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textDrLevi_5.setFont(font)
        self.textDrLevi_5.setObjectName("textDrLevi_5")
        self.textDrLevi_6 = QtWidgets.QLabel(parent=self.CompletedAppointment)
        self.textDrLevi_6.setGeometry(QtCore.QRect(120, 20, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textDrLevi_6.setFont(font)
        self.textDrLevi_6.setWordWrap(True)
        self.textDrLevi_6.setObjectName("textDrLevi_6")
        self.picDrLevi_3 = QtWidgets.QLabel(parent=self.CompletedAppointment)
        self.picDrLevi_3.setGeometry(QtCore.QRect(30, 20, 71, 71))
        self.picDrLevi_3.setAutoFillBackground(False)
        self.picDrLevi_3.setText("")
        self.picDrLevi_3.setPixmap(QtGui.QPixmap(":/images/completed.png"))
        self.picDrLevi_3.setScaledContents(True)
        self.picDrLevi_3.setObjectName("picDrLevi_3")
        self.TotalClients = QtWidgets.QFrame(parent=self.frame_2)
        self.TotalClients.setGeometry(QtCore.QRect(500, 30, 231, 121))
        self.TotalClients.setStyleSheet("\n"
                                        "QFrame#todaysAppointment, QFrame#CompletedAppointment, QFrame#TotalClients{\n"
                                        "    background-color: white;\n"
                                        "    border: 1px solid #D1D5DB;\n"
                                        "    border-radius: 8px;\n"
                                        "    padding: 12px;\n"
                                        "    margin-bottom: 8px;\n"
                                        "}\n"
                                        "\n"
                                        "")
        self.TotalClients.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.TotalClients.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.TotalClients.setObjectName("TotalClients")
        self.textDrLevi_15 = QtWidgets.QLabel(parent=self.TotalClients)
        self.textDrLevi_15.setGeometry(QtCore.QRect(160, 60, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textDrLevi_15.setFont(font)
        self.textDrLevi_15.setObjectName("textDrLevi_15")
        self.textDrLevi_16 = QtWidgets.QLabel(parent=self.TotalClients)
        self.textDrLevi_16.setGeometry(QtCore.QRect(120, 20, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textDrLevi_16.setFont(font)
        self.textDrLevi_16.setWordWrap(True)
        self.textDrLevi_16.setObjectName("textDrLevi_16")
        self.picDrLevi_8 = QtWidgets.QLabel(parent=self.TotalClients)
        self.picDrLevi_8.setGeometry(QtCore.QRect(30, 20, 71, 71))
        self.picDrLevi_8.setAutoFillBackground(False)
        self.picDrLevi_8.setText("")
        self.picDrLevi_8.setPixmap(QtGui.QPixmap(":/images/audience.png"))
        self.picDrLevi_8.setScaledContents(True)
        self.picDrLevi_8.setObjectName("picDrLevi_8")
        self.textDrLevi_16.raise_()
        self.picDrLevi_8.raise_()
        self.textDrLevi_15.raise_()
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 150, 700, 281))
        self.frame_3.setStyleSheet("background-color: transparent; border: none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(parent=self.frame_3)
        self.label.setGeometry(QtCore.QRect(30, 10, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        # MODERN TABLE FOR TODAY'S APPOINTMENTS
        self.tableTodayAppointments = QtWidgets.QTableWidget(parent=self.frame_3)
        self.tableTodayAppointments.setGeometry(QtCore.QRect(20, 50, 711, 221))
        self.tableTodayAppointments.setObjectName("tableTodayAppointments")
        self.tableTodayAppointments.setColumnCount(4)
        self.tableTodayAppointments.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableTodayAppointments.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTodayAppointments.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTodayAppointments.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTodayAppointments.setHorizontalHeaderItem(3, item)
        self.tableTodayAppointments.horizontalHeader().setDefaultSectionSize(175)
        self.tableTodayAppointments.horizontalHeader().setStretchLastSection(True)
        self.tableTodayAppointments.verticalHeader().setVisible(False)

        # Modern table styling for Today's Appointments
        self.tableTodayAppointments.setStyleSheet("""
                    /* Modern Table Styling */
                    QTableWidget {
                        background-color: white;
                        border: 1px solid #E5E7EB;
                        border-radius: 8px;
                        gridline-color: #F3F4F6;
                        selection-background-color: #3B82F6;
                        selection-color: white;
                        outline: none;
                        font-size: 14px;
                    }

                    /* Header Styling */
                    QHeaderView::section {
                        background-color: #F9FAFB;
                        padding: 16px;
                        border: none;
                        border-right: 1px solid #E5E7EB;
                        border-bottom: 2px solid #E5E7EB;
                        font-weight: 600;
                        font-size: 13px;
                        color: #374151;
                        text-transform: uppercase;
                        letter-spacing: 0.5px;
                    }

                    QHeaderView::section:last {
                        border-right: none;
                    }

                    /* Row Styling */
                    QTableWidget::item {
                        padding: 16px;
                        border: none;
                        border-bottom: 1px solid #F3F4F6;
                        color: #374151;
                    }

                    QTableWidget::item:selected {
                        background-color: #3B82F6;
                        color: white;
                    }

                    /* Alternate Row Colors */
                    QTableWidget::item:alternate {
                        background-color: #F9FAFB;
                    }

                    /* Scrollbar Styling */
                    QScrollBar:vertical {
                        border: none;
                        background-color: #F3F4F6;
                        width: 12px;
                        border-radius: 6px;
                        margin: 0px;
                    }

                    QScrollBar::handle:vertical {
                        background-color: #D1D5DB;
                        border-radius: 6px;
                        min-height: 30px;
                    }

                    QScrollBar::handle:vertical:hover {
                        background-color: #9CA3AF;
                    }

                    QScrollBar::add-line:vertical, 
                    QScrollBar::sub-line:vertical {
                        border: none;
                        background: none;
                        height: 0px;
                    }

                    QScrollBar:horizontal {
                        border: none;
                        background-color: #F3F4F6;
                        height: 12px;
                        border-radius: 6px;
                        margin: 0px;
                    }

                    QScrollBar::handle:horizontal {
                        background-color: #D1D5DB;
                        border-radius: 6px;
                        min-width: 30px;
                    }

                    /* Status Badges */
                    QTableWidget::item[status="confirmed"] {
                        background-color: #D1FAE5;
                        color: #059669;
                        border-radius: 20px;
                        padding: 6px 16px;
                        font-weight: 600;
                        font-size: 12px;
                        text-align: center;
                    }

                    QTableWidget::item[status="pending"] {
                        background-color: #FEF3C7;
                        color: #D97706;
                        border-radius: 20px;
                        padding: 6px 16px;
                        font-weight: 600;
                        font-size: 12px;
                        text-align: center;
                    }

                    QTableWidget::item[status="cancelled"] {
                        background-color: #FEE2E2;
                        color: #DC2626;
                        border-radius: 20px;
                        padding: 6px 16px;
                        font-weight: 600;
                        font-size: 12px;
                        text-align: center;
                    }
                """)

        self.stackedWidget.addWidget(self.NewAppointment)

        self.AppointmentList = QtWidgets.QWidget()
        self.AppointmentList.setObjectName("AppointmentList")
        self.frame_6 = QtWidgets.QFrame(parent=self.AppointmentList)
        self.frame_6.setGeometry(QtCore.QRect(20, 90, 151, 441))
        self.frame_6.setStyleSheet("\n"
                                   "background-color: rgb(217, 219, 221);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_7.setGeometry(QtCore.QRect(5, -10, 151, 111))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/images/logoremover.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.frame_6)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 90, 151, 41))
        self.pushButton_7.setStyleSheet("/* Base style for the button */\n"
                                        "QPushButton {\n"
                                        "    /* Make the button transparent by default */\n"
                                        "  background-color: transparent; /* The light grey color from the picture */\n"
                                        "    color: black;              /* Keeps the text black */\n"
                                        "    /* Adjust border-radius to match the full rounding in the image */\n"
                                        "    border-radius: 15px;       \n"
                                        "}\n"
                                        "/* The style to use when the button is the active page (the \"checked\" state) */\n"
                                        "")
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setChecked(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.frame_6)
        self.pushButton_14.setGeometry(QtCore.QRect(0, 410, 151, 23))
        self.pushButton_14.setStyleSheet("QPushButton {\n"
                                         "    background-color: transparent;\n"
                                         "    border: none;\n"
                                         "    color: red;\n"
                                         "}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.frame_6)
        self.pushButton_15.setGeometry(QtCore.QRect(0, 150, 151, 41))
        self.pushButton_15.setStyleSheet("/* Base style for the button */\n"
                                         "QPushButton {\n"
                                         "    /* Make the button transparent by default */\n"
                                         "  background-color: #D3D3D3; /* The light grey color from the picture */\n"
                                         "    color: black;              /* Keeps the text black */\n"
                                         "    /* Adjust border-radius to match the full rounding in the image */\n"
                                         "    border-radius: 15px;       \n"
                                         "}\n"
                                         "/* The style to use when the button is the active page (the \"checked\" state) */\n"
                                         "")
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.setChecked(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(parent=self.frame_6)
        self.pushButton_16.setGeometry(QtCore.QRect(0, 270, 151, 41))
        self.pushButton_16.setStyleSheet("/* Base style for the button */\n"
                                         "QPushButton {\n"
                                         "    /* Make the button transparent by default */\n"
                                         "  background-color: #transparent; /* The light grey color from the picture */\n"
                                         "    color: black;              /* Keeps the text black */\n"
                                         "    /* Adjust border-radius to match the full rounding in the image */\n"
                                         "    border-radius: 15px;       \n"
                                         "}\n"
                                         "/* The style to use when the button is the active page (the \"checked\" state) */\n"
                                         "")
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setChecked(False)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_22 = QtWidgets.QPushButton(parent=self.frame_6)
        self.pushButton_22.setGeometry(QtCore.QRect(0, 210, 151, 41))
        self.pushButton_22.setStyleSheet("/* Base style for the button */\n"
                                         "QPushButton {\n"
                                         "    /* Make the button transparent by default */\n"
                                         "  background-color: transparent; /* The light grey color from the picture */\n"
                                         "    color: black;              /* Keeps the text black */\n"
                                         "    /* Adjust border-radius to match the full rounding in the image */\n"
                                         "    border-radius: 15px;       \n"
                                         "}\n"
                                         "/* The style to use when the button is the active page (the \"checked\" state) */\n"
                                         "")
        self.pushButton_22.setCheckable(True)
        self.pushButton_22.setChecked(False)
        self.pushButton_22.setObjectName("pushButton_22")

        # ADD KPI BUTTON TO APPOINTMENT LIST PAGE
        self.pushButton_kpi_appointments = QtWidgets.QPushButton(parent=self.frame_6)
        self.pushButton_kpi_appointments.setGeometry(QtCore.QRect(0, 330, 151, 41))
        self.pushButton_kpi_appointments.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: black;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #D3D3D3;
            }
        """)
        self.pushButton_kpi_appointments.setText("📊 KPI Reports")
        self.pushButton_kpi_appointments.setCheckable(True)
        self.pushButton_kpi_appointments.setChecked(False)
        self.pushButton_kpi_appointments.setObjectName("pushButton_kpi_appointments")

        self.frame_4 = QtWidgets.QFrame(parent=self.AppointmentList)
        self.frame_4.setGeometry(QtCore.QRect(170, 90, 751, 441))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 751, 441))
        self.frame_5.setStyleSheet("background-color: white; border-radius: 8px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        # MODERN TABLE FOR APPOINTMENT LIST
        self.tableTodayAppointments_2 = QtWidgets.QTableWidget(parent=self.frame_5)
        self.tableTodayAppointments_2.setGeometry(QtCore.QRect(20, 60, 711, 361))
        self.tableTodayAppointments_2.setObjectName("tableTodayAppointments_2")
        self.tableTodayAppointments_2.setColumnCount(6)
        self.tableTodayAppointments_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableTodayAppointments_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTodayAppointments_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTodayAppointments_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTodayAppointments_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTodayAppointments_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTodayAppointments_2.setHorizontalHeaderItem(5, item)
        self.tableTodayAppointments_2.horizontalHeader().setDefaultSectionSize(115)
        self.tableTodayAppointments_2.horizontalHeader().setStretchLastSection(True)
        self.tableTodayAppointments_2.verticalHeader().setVisible(False)

        # Modern table styling for Appointment List
        self.tableTodayAppointments_2.setStyleSheet("""
                    /* Modern Table Styling */
                    QTableWidget {
                        background-color: white;
                        border: 1px solid #E5E7EB;
                        border-radius: 8px;
                        gridline-color: #F3F4F6;
                        selection-background-color: #10B981;
                        selection-color: white;
                        outline: none;
                        font-size: 14px;
                    }

                    /* Header Styling */
                    QHeaderView::section {
                        background-color: #10B981;
                        padding: 16px;
                        border: none;
                        border-right: 1px solid #0D9C6F;
                        border-bottom: 2px solid #0D9C6F;
                        font-weight: 600;
                        font-size: 13px;
                        color: white;
                        text-transform: uppercase;
                        letter-spacing: 0.5px;
                    }

                    QHeaderView::section:last {
                        border-right: none;
                    }

                    /* Row Styling */
                    QTableWidget::item {
                        padding: 16px;
                        border: none;
                        border-bottom: 1px solid #F3F4F6;
                        color: #374151;
                    }

                    QTableWidget::item:selected {
                        background-color: #10B981;
                        color: white;
                    }

                    /* Alternate Row Colors */
                    QTableWidget::item:alternate {
                        background-color: #F9FAFB;
                    }

                    /* Scrollbar Styling */
                    QScrollBar:vertical {
                        border: none;
                        background-color: #F3F4F6;
                        width: 12px;
                        border-radius: 6px;
                        margin: 0px;
                    }

                    QScrollBar::handle:vertical {
                        background-color: #D1D5DB;
                        border-radius: 6px;
                        min-height: 30px;
                    }

                    QScrollBar::handle:vertical:hover {
                        background-color: #9CA3AF;
                    }

                    QScrollBar::add-line:vertical, 
                    QScrollBar::sub-line:vertical {
                        border: none;
                        background: none;
                        height: 0px;
                    }

                    QScrollBar:horizontal {
                        border: none;
                        background-color: #F3F4F6;
                        height: 12px;
                        border-radius: 6px;
                        margin: 0px;
                    }

                    QScrollBar::handle:horizontal {
                        background-color: #D1D5DB;
                        border-radius: 6px;
                        min-width: 30px;
                    }
                """)

        self.stackedWidget.addWidget(self.AppointmentList)

        self.AllClient = QtWidgets.QWidget()
        self.AllClient.setObjectName("AllClient")
        self.frame_8 = QtWidgets.QFrame(parent=self.AllClient)
        self.frame_8.setGeometry(QtCore.QRect(170, 90, 751, 441))
        self.frame_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_9 = QtWidgets.QFrame(parent=self.frame_8)
        self.frame_9.setGeometry(QtCore.QRect(0, 0, 751, 441))
        self.frame_9.setStyleSheet("background-color: white; border-radius: 8px;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        # MODERN TABLE FOR TOTAL CLIENTS
        self.tableTodayAppointments_3 = QtWidgets.QTableWidget(parent=self.frame_9)
        self.tableTodayAppointments_3.setGeometry(QtCore.QRect(20, 60, 711, 361))
        self.tableTodayAppointments_3.setObjectName("tableTodayAppointments_3")
        self.tableTodayAppointments_3.setColumnCount(4)
        self.tableTodayAppointments_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableTodayAppointments_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTodayAppointments_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTodayAppointments_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTodayAppointments_3.setHorizontalHeaderItem(3, item)
        self.tableTodayAppointments_3.horizontalHeader().setDefaultSectionSize(175)
        self.tableTodayAppointments_3.horizontalHeader().setStretchLastSection(True)
        self.tableTodayAppointments_3.verticalHeader().setVisible(False)

        # Modern table styling for Total Clients
        self.tableTodayAppointments_3.setStyleSheet("""
                    /* Modern Table Styling */
                    QTableWidget {
                        background-color: white;
                        border: 1px solid #E5E7EB;
                        border-radius: 8px;
                        gridline-color: #F3F4F6;
                        selection-background-color: #8B5CF6;
                        selection-color: white;
                        outline: none;
                        font-size: 14px;
                    }

                    /* Header Styling */
                    QHeaderView::section {
                        background-color: #8B5CF6;
                        padding: 16px;
                        border: none;
                        border-right: 1px solid #7C3AED;
                        border-bottom: 2px solid #7C3AED;
                        font-weight: 600;
                        font-size: 13px;
                        color: white;
                        text-transform: uppercase;
                        letter-spacing: 0.5px;
                    }

                    QHeaderView::section:last {
                        border-right: none;
                    }

                    /* Row Styling */
                    QTableWidget::item {
                        padding: 16px;
                        border: none;
                        border-bottom: 1px solid #F3F4F6;
                        color: #374151;
                    }

                    QTableWidget::item:selected {
                        background-color: #8B5CF6;
                        color: white;
                    }

                    /* Alternate Row Colors */
                    QTableWidget::item:alternate {
                        background-color: #F9FAFB;
                    }

                    /* Scrollbar Styling */
                    QScrollBar:vertical {
                        border: none;
                        background-color: #F3F4F6;
                        width: 12px;
                        border-radius: 6px;
                        margin: 0px;
                    }

                    QScrollBar::handle:vertical {
                        background-color: #D1D5DB;
                        border-radius: 6px;
                        min-height: 30px;
                    }

                    QScrollBar::handle:vertical:hover {
                        background-color: #9CA3AF;
                    }

                    QScrollBar::add-line:vertical, 
                    QScrollBar::sub-line:vertical {
                        border: none;
                        background: none;
                        height: 0px;
                    }

                    QScrollBar:horizontal {
                        border: none;
                        background-color: #F3F4F6;
                        height: 12px;
                        border-radius: 6px;
                        margin: 0px;
                    }

                    QScrollBar::handle:horizontal {
                        background-color: #D1D5DB;
                        border-radius: 6px;
                        min-width: 30px;
                    }
                """)

        self.frame_7 = QtWidgets.QFrame(parent=self.AllClient)
        self.frame_7.setGeometry(QtCore.QRect(20, 90, 151, 441))
        self.frame_7.setStyleSheet("\n"
                                   "background-color: rgb(217, 219, 221);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_9 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_9.setGeometry(QtCore.QRect(5, -10, 151, 111))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/images/logoremover.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.frame_7)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 90, 151, 41))
        self.pushButton_8.setStyleSheet("/* Base style for the button */\n"
                                        "QPushButton {\n"
                                        "    /* Make the button transparent by default */\n"
                                        "  background-color: transparent; /* The light grey color from the picture */\n"
                                        "    color: black;              /* Keeps the text black */\n"
                                        "    /* Adjust border-radius to match the full rounding in the image */\n"
                                        "    border-radius: 15px;       \n"
                                        "}\n"
                                        "/* The style to use when the button is the active page (the \"checked\" state) */\n"
                                        "")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setChecked(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_17 = QtWidgets.QPushButton(parent=self.frame_7)
        self.pushButton_17.setGeometry(QtCore.QRect(0, 410, 151, 23))
        self.pushButton_17.setStyleSheet("QPushButton {\n"
                                         "    background-color: transparent;\n"
                                         "    border: none;\n"
                                         "    color: red;\n"
                                         "}")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(parent=self.frame_7)
        self.pushButton_18.setGeometry(QtCore.QRect(0, 150, 151, 41))
        self.pushButton_18.setStyleSheet("/* Base style for the button */\n"
                                         "QPushButton {\n"
                                         "    /* Make the button transparent by default */\n"
                                         "  background-color: transparent; /* The light grey color from the picture */\n"
                                         "    color: black;              /* Keeps the text black */\n"
                                         "    /* Adjust border-radius to match the full rounding in the image */\n"
                                         "    border-radius: 15px;       \n"
                                         "}\n"
                                         "/* The style to use when the button is the active page (the \"checked\" state) */\n"
                                         "")
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setChecked(False)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(parent=self.frame_7)
        self.pushButton_19.setGeometry(QtCore.QRect(0, 270, 151, 41))
        self.pushButton_19.setStyleSheet("/* Base style for the button */\n"
                                         "QPushButton {\n"
                                         "    /* Make the button transparent by default */\n"
                                         "  background-color: #transparent; /* The light grey color from the picture */\n"
                                         "    color: black;              /* Keeps the text black */\n"
                                         "    /* Adjust border-radius to match the full rounding in the image */\n"
                                         "    border-radius: 15px;       \n"
                                         "}\n"
                                         "/* The style to use when the button is the active page (the \"checked\" state) */\n"
                                         "")
        self.pushButton_19.setCheckable(True)
        self.pushButton_19.setChecked(False)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_23 = QtWidgets.QPushButton(parent=self.frame_7)
        self.pushButton_23.setGeometry(QtCore.QRect(0, 210, 151, 41))
        self.pushButton_23.setStyleSheet("/* Base style for the button */\n"
                                         "QPushButton {\n"
                                         "    /* Make the button transparent by default */\n"
                                         "  background-color: #D3D3D3; /* The light grey color from the picture */\n"
                                         "    color: black;              /* Keeps the text black */\n"
                                         "    /* Adjust border-radius to match the full rounding in the image */\n"
                                         "    border-radius: 15px;       \n"
                                         "}\n"
                                         "/* The style to use when the button is the active page (the \"checked\" state) */\n"
                                         "")
        self.pushButton_23.setCheckable(True)
        self.pushButton_23.setChecked(False)
        self.pushButton_23.setObjectName("pushButton_23")

        # ADD KPI BUTTON TO TOTAL CLIENTS PAGE
        self.pushButton_kpi_clients = QtWidgets.QPushButton(parent=self.frame_7)
        self.pushButton_kpi_clients.setGeometry(QtCore.QRect(0, 330, 151, 41))
        self.pushButton_kpi_clients.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: black;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #D3D3D3;
            }
        """)
        self.pushButton_kpi_clients.setText("📊 KPI Reports")
        self.pushButton_kpi_clients.setCheckable(True)
        self.pushButton_kpi_clients.setChecked(False)
        self.pushButton_kpi_clients.setObjectName("pushButton_kpi_clients")

        self.frame_7.raise_()
        self.frame_8.raise_()
        self.stackedWidget.addWidget(self.AllClient)

        # Profile section
        self.Profile = QtWidgets.QWidget()
        self.Profile.setObjectName("Profile")
        self.frame_11 = QtWidgets.QFrame(parent=self.Profile)
        self.frame_11.setGeometry(QtCore.QRect(170, 90, 751, 441))
        self.frame_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.frame_13 = QtWidgets.QFrame(parent=self.frame_11)
        self.frame_13.setGeometry(QtCore.QRect(0, 0, 751, 441))
        self.frame_13.setStyleSheet("background-color: white; border-radius: 8px;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.frame_13)
        self.pushButton_10.setGeometry(QtCore.QRect(200, 250, 351, 51))
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
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.frame_13)
        self.lineEdit_7.setGeometry(QtCore.QRect(180, 90, 181, 41))
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
        self.label_10 = QtWidgets.QLabel(parent=self.frame_13)
        self.label_10.setGeometry(QtCore.QRect(340, 40, 131, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        self.label_10.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.frame_13)
        self.lineEdit_9.setGeometry(QtCore.QRect(180, 150, 181, 41))
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
        self.lineEdit_10 = QtWidgets.QLineEdit(parent=self.frame_13)
        self.lineEdit_10.setGeometry(QtCore.QRect(390, 150, 181, 41))
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
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.frame_13)
        self.lineEdit_8.setGeometry(QtCore.QRect(390, 90, 181, 41))
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
        self.lineEdit_11 = QtWidgets.QLineEdit(parent=self.frame_13)
        self.lineEdit_11.setGeometry(QtCore.QRect(180, 200, 391, 41))
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
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.frame_10 = QtWidgets.QFrame(parent=self.Profile)
        self.frame_10.setGeometry(QtCore.QRect(20, 90, 151, 441))
        self.frame_10.setStyleSheet("\n"
                                    "background-color: rgb(217, 219, 221);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_12 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_12.setGeometry(QtCore.QRect(5, -10, 151, 111))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/images/logoremover.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.pushButton_27 = QtWidgets.QPushButton(parent=self.frame_10)
        self.pushButton_27.setGeometry(QtCore.QRect(0, 90, 151, 41))
        self.pushButton_27.setStyleSheet("/* Base style for the button */\n"
                                         "QPushButton {\n"
                                         "    /* Make the button transparent by default */\n"
                                         "  background-color: transparent; /* The light grey color from the picture */\n"
                                         "    color: black;              /* Keeps the text black */\n"
                                         "    /* Adjust border-radius to match the full rounding in the image */\n"
                                         "    border-radius: 15px;       \n"
                                         "}\n"
                                         "/* The style to use when the button is the active page (the \"checked\" state) */\n"
                                         "")
        self.pushButton_27.setCheckable(True)
        self.pushButton_27.setChecked(False)
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(parent=self.frame_10)
        self.pushButton_28.setGeometry(QtCore.QRect(0, 410, 151, 23))
        self.pushButton_28.setStyleSheet("QPushButton {\n"
                                         "    background-color: transparent;\n"
                                         "    border: none;\n"
                                         "    color: red;\n"
                                         "}")
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(parent=self.frame_10)
        self.pushButton_29.setGeometry(QtCore.QRect(0, 150, 151, 41))
        self.pushButton_29.setStyleSheet("/* Base style for the button */\n"
                                         "QPushButton {\n"
                                         "    /* Make the button transparent by default */\n"
                                         "  background-color: transparent; /* The light grey color from the picture */\n"
                                         "    color: black;              /* Keeps the text black */\n"
                                         "    /* Adjust border-radius to match the full rounding in the image */\n"
                                         "    border-radius: 15px;       \n"
                                         "}\n"
                                         "/* The style to use when the button is the active page (the \"checked\" state) */\n"
                                         "")
        self.pushButton_29.setCheckable(True)
        self.pushButton_29.setChecked(False)
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(parent=self.frame_10)
        self.pushButton_30.setGeometry(QtCore.QRect(0, 270, 151, 41))
        self.pushButton_30.setStyleSheet("/* Base style for the button */\n"
                                         "QPushButton {\n"
                                         "    /* Make the button transparent by default */\n"
                                         "  background-color: #transparent; /* The light grey color from the picture */\n"
                                         "    color: black;              /* Keeps the text black */\n"
                                         "    /* Adjust border-radius to match the full rounding in the image */\n"
                                         "    border-radius: 15px;       \n"
                                         "}\n"
                                         "/* The style to use when the button is the active page (the \"checked\" state) */\n"
                                         "")
        self.pushButton_30.setCheckable(True)
        self.pushButton_30.setChecked(False)
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(parent=self.frame_10)
        self.pushButton_31.setGeometry(QtCore.QRect(0, 210, 151, 41))
        self.pushButton_31.setStyleSheet("/* Base style for the button */\n"
                                         "QPushButton {\n"
                                         "    /* Make the button transparent by default */\n"
                                         "  background-color: #D3D3D3; /* The light grey color from the picture */\n"
                                         "    color: black;              /* Keeps the text black */\n"
                                         "    /* Adjust border-radius to match the full rounding in the image */\n"
                                         "    border-radius: 15px;       \n"
                                         "}\n"
                                         "/* The style to use when the button is the active page (the \"checked\" state) */\n"
                                         "")
        self.pushButton_31.setCheckable(True)
        self.pushButton_31.setChecked(False)
        self.pushButton_31.setObjectName("pushButton_31")

        # ADD KPI BUTTON TO PROFILE PAGE
        self.pushButton_kpi_profile = QtWidgets.QPushButton(parent=self.frame_10)
        self.pushButton_kpi_profile.setGeometry(QtCore.QRect(0, 330, 151, 41))
        self.pushButton_kpi_profile.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: black;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #D3D3D3;
            }
        """)
        self.pushButton_kpi_profile.setText("📊 KPI Reports")
        self.pushButton_kpi_profile.setCheckable(True)
        self.pushButton_kpi_profile.setChecked(False)
        self.pushButton_kpi_profile.setObjectName("pushButton_kpi_profile")

        self.frame_10.raise_()
        self.frame_11.raise_()
        self.stackedWidget.addWidget(self.Profile)
        self.stackedWidget.raise_()
        self.pushButton_6.raise_()
        self.label_5.raise_()
        self.pushButton_5.raise_()
        self.label_8.raise_()
        self.pushButton_4.raise_()
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        self.stackedWidget.setCurrentIndex(0)  # Start on first page (Dashboard)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.label_8.setText(_translate("Login", "CARELINE"))
        self.pushButton_4.setText(_translate("Login", "Home"))
        self.pushButton_5.setText(_translate("Login", "About Us"))
        self.pushButton_6.setText(_translate("Login", "Contact Us"))
        self.pushButton_3.setText(_translate("Login", "Dashboard"))
        self.pushButton_12.setText(_translate("Login", "Log Out"))
        self.pushButton_11.setText(_translate("Login", "Appointments"))
        self.pushButton_13.setText(_translate("Login", "My Profile"))
        self.pushButton_21.setText(_translate("Login", "Total Clients"))
        self.textDrLevi_2.setText(_translate("Login", "0"))
        self.textDrLevi.setText(_translate("Login", "     Today's "
                                                    "Appointment"))
        self.textDrLevi_5.setText(_translate("Login", "0"))
        self.textDrLevi_6.setText(_translate("Login", "  Completed Appointment"))
        self.textDrLevi_15.setText(_translate("Login", "0"))
        self.textDrLevi_16.setText(_translate("Login", "Total Clients"))
        self.label.setText(_translate("Login", "Today's Appointment"))
        item = self.tableTodayAppointments.horizontalHeaderItem(0)
        item.setText(_translate("Login", "Time"))
        item = self.tableTodayAppointments.horizontalHeaderItem(1)
        item.setText(_translate("Login", "Patient"))
        item = self.tableTodayAppointments.horizontalHeaderItem(2)
        item.setText(_translate("Login", "Doctor"))
        item = self.tableTodayAppointments.horizontalHeaderItem(3)
        item.setText(_translate("Login", "Status"))
        self.pushButton_7.setText(_translate("Login", "Dashboard"))
        self.pushButton_14.setText(_translate("Login", "Log Out"))
        self.pushButton_15.setText(_translate("Login", "Appointments"))
        self.pushButton_16.setText(_translate("Login", "My Profile"))
        self.pushButton_22.setText(_translate("Login", "Total Clients"))
        self.label_2.setText(_translate("Login", "Appointment List"))
        item = self.tableTodayAppointments_2.horizontalHeaderItem(0)
        item.setText(_translate("Login", "First Name"))
        item = self.tableTodayAppointments_2.horizontalHeaderItem(1)
        item.setText(_translate("Login", "Last Name"))
        item = self.tableTodayAppointments_2.horizontalHeaderItem(2)
        item.setText(_translate("Login", "Email"))
        item = self.tableTodayAppointments_2.horizontalHeaderItem(3)
        item.setText(_translate("Login", "Phone Number"))
        item = self.tableTodayAppointments_2.horizontalHeaderItem(4)
        item.setText(_translate("Login", "Date"))
        item = self.tableTodayAppointments_2.horizontalHeaderItem(5)
        item.setText(_translate("Login", "Time"))
        self.label_3.setText(_translate("Login", "Total Clients"))
        item = self.tableTodayAppointments_3.horizontalHeaderItem(0)
        item.setText(_translate("Login", "First Name"))
        item = self.tableTodayAppointments_3.horizontalHeaderItem(1)
        item.setText(_translate("Login", "Last Name"))
        item = self.tableTodayAppointments_3.horizontalHeaderItem(2)
        item.setText(_translate("Login", "Email"))
        item = self.tableTodayAppointments_3.horizontalHeaderItem(3)
        item.setText(_translate("Login", "Phone Number"))
        self.pushButton_8.setText(_translate("Login", "Dashboard"))
        self.pushButton_17.setText(_translate("Login", "Log Out"))
        self.pushButton_18.setText(_translate("Login", "Appointments"))
        self.pushButton_19.setText(_translate("Login", "My Profile"))
        self.pushButton_23.setText(_translate("Login", "Total Clients"))
        self.pushButton_10.setText(_translate("Login", "Save Changes"))
        self.lineEdit_7.setPlaceholderText(_translate("Login", "Account First Name"))
        self.label_10.setText(_translate("Login", "My Profile"))
        self.lineEdit_9.setPlaceholderText(_translate("Login", "Account Phone Number"))
        self.lineEdit_10.setPlaceholderText(_translate("Login", "Account Email"))
        self.lineEdit_8.setPlaceholderText(_translate("Login", "Account Last Name"))
        self.lineEdit_11.setPlaceholderText(_translate("Login", "Address"))
        self.pushButton_27.setText(_translate("Login", "Dashboard"))
        self.pushButton_28.setText(_translate("Login", "Log Out"))
        self.pushButton_29.setText(_translate("Login", "Appointments"))
        self.pushButton_30.setText(_translate("Login", "My Profile"))
        self.pushButton_31.setText(_translate("Login", "Total Clients"))