import sys, controller, pyclip
from PyQt6.QtCore import QSize, Qt, QTimer
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
        widgets[1] = self.generated_password_label = QLabel("Generate a password!")

        # Move title to top left of the layout
        title_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # Move password label to the bottom left of the layout
        self.generated_password_label.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)

        # Set title font size
        title_font = title_label.font()
        title_font.setPointSize(12)
        title_label.setFont(title_font)

        # Set password font and size
        password_font = self.generated_password_label.font()
        password_font.setPointSize(20)
        password_font.setFamily("Consolas")
        self.generated_password_label.setFont(password_font)

        # Add text to vertical layout
        layouts[0] = labels_layout = QVBoxLayout()
        add_widgets_to_layout(widgets, labels_layout)
        widgets.clear()

        # BUTTON WIDGETS
        # Create buttons
        widgets[0] = self.generate_button = QPushButton("Generate")
        widgets[1] = self.copy_button = QPushButton("Copy to Clipboard")

        self.generate_button.clicked.connect(self.generate_password)

        self.clipboard_button_timer = QTimer()

        def change_copy_button_text():
            self.copy_button.setText("Copy to Clipboard")
            self.clipboard_button_timer.stop()

        def copy_to_clipboard():
            pyclip.copy(self.generated_password_label.text())
            self.copy_button.setText("Copied!")
            self.clipboard_button_timer.timeout.connect(change_copy_button_text)
            self.clipboard_button_timer.start(2000)

        self.copy_button.clicked.connect(copy_to_clipboard)

        # Add buttons to horizontal layout
        layouts[1] = buttons_layout = QHBoxLayout()
        add_widgets_to_layout(widgets, buttons_layout)
        widgets.clear()

        # "PASSWORD OPTIONS" WIDGETS
        # Create checkboxes
        widgets[0] = self.uppercase_checkbox = QCheckBox("Uppercase Letters")
        widgets[1] = self.lowercase_checkbox = QCheckBox("Lowercase Letters")
        widgets[2] = self.numbers_checkbox = QCheckBox("Include Numbers")
        widgets[3] = self.symbols_checkbox = QCheckBox("Include Symbols")

        # Check all checkboxes
        for i in widgets:
            widgets[i].setCheckState(Qt.CheckState.Checked)

        # Create symbol edit box
        widgets[4] = self.symbols_lineedit = QLineEdit("@%+\/'!#$^?:,(){}[]~`-_.")

        def disable_lineedit(value):
            self.symbols_lineedit.setEnabled(value)

        self.symbols_checkbox.stateChanged.connect(disable_lineedit)

        # Create label for password length controls
        widgets[5] = length_label = QLabel("Password Length")

        # Add password options widgets to vertical layout
        layouts[2] = password_options_layout = QVBoxLayout()
        add_widgets_to_layout(widgets, password_options_layout)
        widgets.clear()

        # PASSWORD LENGTH CONTROLS
        # Create password length controls
        widgets[0] = self.length_slider = QSlider(Qt.Orientation.Horizontal)
        widgets[1] = self.length_spinbox = QSpinBox()

        # Set ranges
        self.length_slider.setRange(3, 100)
        self.length_spinbox.setRange(3, 100)

        # Set defaults
        self.length_slider.setValue(12)
        self.length_spinbox.setValue(12)

        # Connect values of slider and spinbox to display correctly
        def change_length_slider_value(value):
            self.length_slider.setValue(value)

        def change_length_spinbox_value(value):
            self.length_spinbox.setValue(value)

        self.length_slider.valueChanged.connect(change_length_spinbox_value)
        self.length_spinbox.valueChanged.connect(change_length_slider_value)

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

    def generate_password(self):
        use_lowercase = self.lowercase_checkbox.isChecked()
        use_uppercase = self.uppercase_checkbox.isChecked()
        use_numbers = self.numbers_checkbox.isChecked()
        use_symbols = self.symbols_checkbox.isChecked()
        symbols_string = self.symbols_lineedit.text()
        password_length = int(self.length_spinbox.value())
        
        # Remove alphanumeric characters from symbol string
        for i in symbols_string:
            if i.isalpha() or i.isnumeric():
                symbols_string = symbols_string.replace(i, "", 1)
        
        # Remove duplicates from symbol string
        self.symbols_lineedit.setText("".join(dict.fromkeys(symbols_string)))

        if symbols_string == "":
            self.symbols_lineedit.setText("@%+\/'!#$^?:,(){}[]~`-_.")
        
        password_string = controller.get_password(use_lowercase, use_uppercase, use_numbers, use_symbols, symbols_string, password_length)

        self.generated_password_label.setText(password_string)
        self.clipboard_button_timer.stop()
        self.copy_button.setText("Copy to Clipboard")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()