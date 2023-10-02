from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import config


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("HIDS App")
        layout = QVBoxLayout()

        directories = QLineEdit()
        self.directories_input = ""
        directories.textEdited.connect(self.directories_edited)

        function = QComboBox()
        function.addItems(["md5", "sha1", "sha256"]),
        self.function_input = "md5"
        function.currentTextChanged.connect(self.function_edited)

        email = QLineEdit()
        self.email_input = ""
        email.textEdited.connect(self.email_edited)

        scan = QSpinBox()
        scan.setMinimum(1)
        scan.setMaximum(3)
        self.scan_input = 1
        scan.valueChanged.connect(self.scan_edited)
        log = QSpinBox()
        log.setMinimum(1)
        log.setMaximum(3)
        self.log_input = 1
        log.valueChanged.connect(self.log_edited)

        run = QPushButton("RUN")
        run.clicked.connect(self.run)

        default = QPushButton("Continue with default config")
        default.clicked.connect(self.default)

        widgets = [
            QLabel("directories_to_scan"),
            directories,
            QLabel("hash_function"),
            function,
            QLabel("email_to_notify"),
            email,
            QLabel("scan_interval"),
            scan,
            QLabel("log_interval"),
            log,
            run,
            default,
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

    def function_edited(self, s):
        self.function_input = s
        print(s)

    def scan_edited(self, i):
        self.scan_input = i
        print(i)

    def log_edited(self, i):
        self.log_input = i
        print(i)

    def run(self):
        config.editConfig(
            self.directories_input,
            self.function_input,
            self.email_input,
            self.scan_input,
            self.log_input,
        )
        start()

    def default(self):
        config.writeDefaultConfig()
        start()


def start():
    print("starts app")

def startGUI():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec_()
