import PySimpleGUI as sg

# Define the layout for the first child window
layout1 = [[sg.Text('Child Window 1')],
           [sg.Input(key='input1'), sg.Button('OK')]]

# Define the layout for the second child window
layout2 = [[sg.Text('Child Window 2')],
           [sg.Listbox(values=['Item 1', 'Item 2', 'Item 3'], key='listbox', size=(30, 3))],
           [sg.Button('Add Item'), sg.Button('Remove Item')]]

# Define the main window layout
layout = [[sg.Text('Main Window')],
          [sg.Frame('Child Window 1', layout1, title_color='red'),
           sg.Frame('Child Window 2', layout2, title_color='blue')],
          [sg.Button('Close')]]

# Create the main window
window = sg.Window('MDI Application', layout, element_justification='center', resizable=True)

# Run the application loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
      break
    if event == 'Close':
        break
    elif event == 'OK':
        # Do something with the input from the first child window
        print(values['input1'])
    elif event == 'Add Item':
        # Add an item to the listbox in the second child window
        window['listbox'].append('New Item')
    elif event == 'Remove Item':
        # Remove the selected item from the listbox in the second child window
        window['listbox'].remove(values['listbox'][0])

# Close the window
window.close()
