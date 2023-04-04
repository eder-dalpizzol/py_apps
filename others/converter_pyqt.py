import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout

class Converter(QWidget):
    def __init__(self):
        super().__init__()

        self.input_label = QLabel("Value:", self)
        self.input_field = QLineEdit(self)
        self.units_label = QLabel("Units:", self)
        self.units_dropdown = QComboBox(self)
        self.units_dropdown.addItems(["km to mile", "kg to pound", "sec to min"])
        self.convert_button = QPushButton("Convert", self)
        self.convert_button.clicked.connect(self.convert_units)
        self.output_label = QLabel("Output:", self)
        self.output_field = QLabel("", self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.units_label)
        layout.addWidget(self.units_dropdown)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_field)

        self.setWindowTitle("Converter")
        self.setLayout(layout)

    def convert_units(self):
        input_value = self.input_field.text()
        output_str = ""
        if input_value.isnumeric():
            if self.units_dropdown.currentText() != "":
                if self.units_dropdown.currentText() == "km to mile":
                    output = round(float(input_value) * 0.6214, 2)
                    output_str = f'{input_value} km are {output} miles'
                elif self.units_dropdown.currentText() == "kg to pound":
                    output = round(float(input_value) * 2.20462, 2)
                    output_str = f'{input_value} kg are {output} pounds'
                elif self.units_dropdown.currentText() == "sec to min":
                    output = round(float(input_value) / 60, 2)
                    output_str = f'{input_value} seconds are {output} minutes'
            else:
                output_str = "Select a type of convertion"
        else:
            output_str = "Insert a valid number"

        self.output_field.setText(output_str)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = Converter()
    converter.show()
    sys.exit(app.exec_())
