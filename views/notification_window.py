from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import Qt
from models.database import DatabaseOperations


class NotificationButton(QtWidgets.QPushButton):
    """
    Custom Button that draws a Red Badge if there are unread notifications.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.unread_count = 0
        self.setFixedSize(40, 40)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        # Style as a clean icon button
        self.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid #E5E7EB;
                border-radius: 20px; /* Circle */
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #F3F4F6;
                border-color: #D1D5DB;
            }
        """)
        self.setText("🔔")  # Bell Icon

    def set_count(self, count):
        """Update count and redraw"""
        self.unread_count = count
        self.update()  # Triggers paintEvent

    def paintEvent(self, event):
        """Draw the button, then draw the red badge on top"""
        super().paintEvent(event)  # Draw normal button first

        if self.unread_count > 0:
            painter = QtGui.QPainter(self)
            painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)

            # 1. Red Circle
            painter.setBrush(QtGui.QColor("#EF4444"))  # Red
            painter.setPen(Qt.PenStyle.NoPen)

            # Position: Top Right of button
            badge_size = 18
            rect = QtCore.QRect(22, 0, badge_size, badge_size)
            painter.drawEllipse(rect)

            # 2. Number
            painter.setPen(QtGui.QColor("white"))
            font = painter.font()
            font.setBold(True)
            font.setPointSize(8)
            painter.setFont(font)

            # Center text in red circle
            # Cap at "9+" if too many
            text = str(self.unread_count) if self.unread_count < 10 else "9+"
            painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, text)


class NotificationWindow(QtWidgets.QDialog):
    """Popup window to show notifications"""

    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        self.user_id = user_id
        self.db_ops = DatabaseOperations()

        self.setWindowTitle("Notifications")
        self.setMinimumSize(400, 500)
        self.setStyleSheet("background-color: white;")

        self.setup_ui()
        self.load_notifications()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)

        # Header
        header = QtWidgets.QLabel("🔔 Your Notifications")
        header.setStyleSheet(
            "font-size: 18px; font-weight: bold; color: #111; padding-bottom: 10px; border-bottom: 1px solid #EEE;")
        layout.addWidget(header)

        # List Widget
        self.list_widget = QtWidgets.QListWidget()
        self.list_widget.setStyleSheet("""
            QListWidget { border: none; }
            QListWidget::item { border-bottom: 1px solid #F3F4F6; }
            QListWidget::item:hover { background-color: #F9FAFB; }
        """)
        self.list_widget.setSpacing(5)
        layout.addWidget(self.list_widget)

        # Close Button
        close_btn = QtWidgets.QPushButton("Close")
        close_btn.clicked.connect(self.accept)
        close_btn.setStyleSheet(
            "background-color: #4F46E5; color: white; padding: 8px; border-radius: 6px; font-weight: bold;")
        layout.addWidget(close_btn)

    def load_notifications(self):
        self.list_widget.clear()
        notifs = self.db_ops.get_user_notifications(self.user_id)

        if not notifs:
            item = QtWidgets.QListWidgetItem("No notifications yet.")
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.list_widget.addItem(item)
            return

        for n in notifs:
            item = QtWidgets.QListWidgetItem()

            # Custom Widget for the item
            widget = QtWidgets.QWidget()
            w_layout = QtWidgets.QVBoxLayout(widget)
            w_layout.setContentsMargins(10, 10, 10, 10)

            # Logic: If read, gray text. If unread, black text + blue dot.
            color = "#111" if not n['IsRead'] else "#6B7280"
            weight = "bold" if not n['IsRead'] else "normal"

            msg_lbl = QtWidgets.QLabel(n['Message'])
            msg_lbl.setWordWrap(True)
            msg_lbl.setStyleSheet(f"font-size: 13px; font-weight: {weight}; color: {color};")

            date_lbl = QtWidgets.QLabel(n['Date'])
            date_lbl.setStyleSheet("font-size: 11px; color: #9CA3AF; margin-top: 4px;")

            w_layout.addWidget(msg_lbl)
            w_layout.addWidget(date_lbl)

            item.setSizeHint(widget.sizeHint())
            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, widget)

            # Mark as read
            if not n['IsRead']:
                self.db_ops.mark_notification_read(n['NotificationID'])