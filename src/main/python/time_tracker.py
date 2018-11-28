import os
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QMainWindow, QStackedLayout)
from PyQt5.QtGui import QPixmap, QScreen


class WidgetTimeTracker(QDialog):

    def __init__(self, parent=None):
        super(WidgetTimeTracker, self).__init__(parent)
        self.image_path = os.path.join(os.getcwd(), 'src',
                                       'main', 'images',
                                       'screenshots')
        self.setFixedSize(350, 600)
        self.create_layout()
        self.setWindowTitle("Behaviour Tracking")
        self.setLayout(self.main_layout)
        self.capture_btn.clicked.connect(self.capture_screen)

    def create_layout(self):
        self.main_layout = QGridLayout()
        self.capture_btn = QPushButton('Capture Screen')
        self.tracking_btn = QPushButton('Start Tracking')
        self.main_layout.addWidget(self.capture_btn, 1, 0)
        self.main_layout.addWidget(self.tracking_btn, 1, 1)

    def capture_screen(self):
        self.img_preview = QLabel()
        self.current_screen = QApplication.primaryScreen().grabWindow(0)
        self.current_screen.save("{}".format(os.path.join(self.image_path,
                                                          "snap1.jpg")), 'jpg')
        self.img_preview.setPixmap(self.current_screen.scaled(250, 350,
                                                              Qt.KeepAspectRatio,
                                                              Qt.SmoothTransformation))
        self.set_layout_with_screeshot()

    def set_layout_with_screeshot(self):
        self.main_layout.addWidget(self.img_preview, 0, 0, 0, 0, alignment=Qt.AlignCenter)
        self.update()


