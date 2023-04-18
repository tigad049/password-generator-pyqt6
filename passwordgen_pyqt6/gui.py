import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
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
        self.setFixedSize(QSize(400, 300))
        
        def add_widgets_to_layout(widgets, layout):
            for widget_num in widgets:
                layout.addWidget(widgets[widget_num])
        
        widgets = {}
        layouts = {}
        
        # TEXT LABEL WIDGETS
        # Create title and password placeholder
        widgets[0] = title_label = QLabel("Password Generator")
        widgets[1] = generated_password_label = QLabel("Generate a password!")
        
        # Move title to top left of the layout
        title_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        
        # Move password label to the bottom left of the layout
        generated_password_label.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)
        
        # Set title font size
        title_font = title_label.font()
        title_font.setPointSize(12)
        title_label.setFont(title_font)
        
        # Set password font size and make it bold
        password_font = generated_password_label.font()
        password_font.setPointSize(20)
        password_font.setBold(True)
        generated_password_label.setFont(password_font)
        
        # Add text to vertical layout
        layouts[0] = labels_layout = QVBoxLayout()
        add_widgets_to_layout(widgets, labels_layout)
        widgets.clear()
        
        # BUTTON WIDGETS
        # Create buttons
        widgets[0] = generate_button = QPushButton("Generate")
        widgets[1] = copy_button = QPushButton("Copy to Clipboard")
        
        # Add buttons to horizontal layout
        layouts[1] = buttons_layout = QHBoxLayout()
        add_widgets_to_layout(widgets, buttons_layout)
        widgets.clear()
        
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
        
        def disable_lineedit(value):
            symbols_lineedit.setEnabled(value)
        
        symbols_checkbox.stateChanged.connect(disable_lineedit)
        
        # Create label for password length controls
        widgets[5] = length_label = QLabel("Password Length")
        
        # Add password options widgets to vertical layout
        layouts[2] = password_options_layout = QVBoxLayout()
        add_widgets_to_layout(widgets, password_options_layout)
        widgets.clear()
        
        # PASSWORD LENGTH CONTROLS
        # Create password length controls
        widgets[0] = length_slider = QSlider(Qt.Orientation.Horizontal)
        widgets[1] = length_spinbox = QSpinBox()
        
        # Set ranges
        length_slider.setRange(3, 100)
        length_spinbox.setRange(3, 100)
        
        # Set defaults
        length_slider.setValue(12)
        length_spinbox.setValue(12)
        
        # Connect values of slider and spinbox to display correctly
        def change_length_slider_value(value):
            length_slider.setValue(value)
        
        def change_length_spinbox_value(value):
            length_spinbox.setValue(value)
        
        length_slider.valueChanged.connect(change_length_spinbox_value)
        length_spinbox.valueChanged.connect(change_length_slider_value)
        
        # Add password length controls to horizontal layout
        layouts[3] = password_length_layout = QHBoxLayout()
        add_widgets_to_layout(widgets, password_length_layout)
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