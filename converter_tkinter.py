import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Converter")

# Create a label for the input field
input_label = tk.Label(root, text="Value:")
input_label.grid(row=0, column=0)

# Create an input field
input_field = tk.Entry(root)
input_field.grid(row=0, column=1)

# Create a label for the units drop-down
units_label = tk.Label(root, text="Units:")
units_label.grid(row=0, column=2)

# Create a drop-down list for the units
units_var = tk.StringVar(root)
units_var.set("")
units_dropdown = tk.OptionMenu(root, units_var, "km to mile", "kg to pound", "sec to min")
units_dropdown.grid(row=0, column=3)

# Create a button to perform the conversion
convert_button = tk.Button(root, text="Convert", command=lambda: convert_units())
convert_button.grid(row=0, column=4)

# Create a label for the output field
output_label = tk.Label(root, text="Output")
output_label.grid(row=1, column=0, columnspan=5)

# Create an output field
output_field = tk.Label(root, text="")
output_field.grid(row=2, column=0, columnspan=5)

def convert_units():
    # Get the input value
    input_value = input_field.get()
    output_str = ""
    # Check if the input value is numeric
    if input_value.isnumeric():
        if units_var.get() != "":
            # Perform the selected conversion
            if units_var.get() == "km to mile":
                output = round(float(input_value) * 0.6214, 2)
                output_str = f'{input_value} km are {output} miles'
            elif units_var.get() == "kg to pound":
                output = round(float(input_value) * 2.20462, 2)
                output_str = f'{input_value} kg are {output} pounds'
            elif units_var.get() == "sec to min":
                output = round(float(input_value) / 60, 2)
                output_str = f'{input_value} seconds are {output} minutes'
        else:
            output_str = "Select a type of convertion"
    else:
        output_str = "Insert a valid number"

    # Update the output field with the result
    output_field.config(text=output_str)

root.mainloop()
