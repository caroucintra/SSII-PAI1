from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("HIDS App")
        layout = QVBoxLayout()

        directories = QLineEdit()
        directories.textEdited.connect(self.directories_edited)

        hash = QComboBox()
        hash.addItems(['md5', 'sha1', 'sha256']),
        hash.currentTextChanged.connect(self.hash_edited)

        email = QLineEdit()
        email.textEdited.connect(self.email_edited)

        scan = QSpinBox()
        scan.setMinimum(1)
        scan.setMaximum(3)
        scan.valueChanged.connect(self.scan_edited)
        log = QSpinBox()
        log.setMinimum(1)
        log.setMaximum(3)
        log.valueChanged.connect(self.log_edited)

        
        widgets = [
            QLabel("directories_to_scan"),
            directories,
            QLabel('hash_function'),
            hash,
            QLabel('email_to_notify'),
            email,
            QLabel('scan_interval'),
            scan,
            QLabel('log_interval'),
            log,
            QPushButton('RUN'),
        ]

        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)
    
    def directories_edited(self, s):
        self.directories_input = s
        print(s)

    def email_edited(self, s):
        self.email_input = s
        print(s)
    
    def hash_edited(self, s):
        self.hash_input = s
        print(s)
    
    def scan_edited(self, i):
        self.scan_input = i
        print(i)

    def log_edited(self, i):
        self.log_input = i
        print(i)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()