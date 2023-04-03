__version__ = '0.1.0'

import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow,
    QVBoxLayout, 
    QPushButton,
    QCheckBox,
    QLineEdit,
    QLabel,
    QWidget
)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Generator")
        self.setFixedSize(QSize(400, 600))
        
        uppercase_checkbox = QCheckBox("Uppercase Letters")
        lowercase_checkbox = QCheckBox("Lowercase Letters")
        numbers_checkbox = QCheckBox("Include Numbers")
        symbols_checkbox = QCheckBox("Include Symbols")
        symbols_lineedit = QLineEdit("@%+\\/'!#$^?:,(){}[]~`-_.")
        
        password_options_layout = QVBoxLayout()
        password_options_layout.addWidget(uppercase_checkbox)
        password_options_layout.addWidget(lowercase_checkbox)
        password_options_layout.addWidget(numbers_checkbox)
        password_options_layout.addWidget(symbols_checkbox)
        password_options_layout.addWidget(symbols_lineedit)
        
        main_layout = QVBoxLayout()
        main_layout.addLayout(password_options_layout)
        
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()