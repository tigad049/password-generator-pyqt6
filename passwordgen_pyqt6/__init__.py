__version__ = '0.1.0'

import sys
from PyQt6.QtCore import QSize, Qt, QObject
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow,
    QVBoxLayout, 
    QPushButton,
    QCheckBox,
    QLineEdit,
    QLabel,
    QWidget,
    QSlider,
    QSpinBox
)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Generator")
        self.setFixedSize(QSize(400, 600))
        
        widgets = {}
        layouts = {}
        
        # "PASSWORD OPTIONS" WIDGETS
        # Create checkboxes
        widgets[0] = uppercase_checkbox = QCheckBox("Uppercase Letters")
        widgets[1] = lowercase_checkbox = QCheckBox("Lowercase Letters")
        widgets[2] = numbers_checkbox = QCheckBox("Include Numbers")
        widgets[3] = symbols_checkbox = QCheckBox("Include Symbols")
        
        # Check all checkboxes
        for i in widgets:
            widgets[i].setCheckState(Qt.CheckState.Checked)
        
        # Create symbol edit box
        widgets[4] = symbols_lineedit = QLineEdit("@%+\\/'!#$^?:,(){}[]~`-_.")
        
        # Create password length controls
        widgets[5] = length_slider = QSlider(Qt.Orientation.Horizontal)
        widgets[6] = length_spinbox = QSpinBox()
        length_slider.setRange(3, 100)
        length_spinbox.setRange(3, 100)
        
        # Add password options widgets to layout
        layouts[0] = password_options_layout = QVBoxLayout()
        for widget in widgets:
            password_options_layout.addWidget(widgets[widget])
        widgets.clear()
        
        # Create main GUI layout
        main_layout = QVBoxLayout()
        
        # Add all currently defined layouts
        for i in layouts:
            main_layout.addLayout(layouts[i])
        
        # Display main GUI layout
        main_screen = QWidget()
        main_screen.setLayout(main_layout)
        self.setCentralWidget(main_screen)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()