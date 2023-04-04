# still needs adjustments
import PySimpleGUI as sg

def create_layout2():
    # Define the layout for the second child window
    layout2 = [[sg.Listbox(values=['Item 1', 'Item 2', 'Item 3'], key='listbox', size=(30, 3))],
               [sg.Button('Add Item'), sg.Button('Remove Item')]]
    # Return the layout
    return layout2

# Define the layout for the first child window
layout1 = [[sg.Text('Child Window 1')],
           [sg.Input(key='input1'), sg.Button('OK')]]

# Define the main window layout
layout = [[sg.Text('Main Window')],
          [sg.Frame('Child Window 1', layout1, title_color='red')],
          [sg.Frame('Child Window 2', [[sg.Text('Child Window 2')]], title_color='blue', key='frame2', visible=True)],
          [sg.Button('Create Child Window 2'), sg.Button('Close')]]

# Create the main window
window = sg.Window('MDI Application', layout, element_justification='center', resizable=True, finalize=True)

# Maximize the main window
window.maximize()

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
    elif event == 'Create Child Window 2':
        # Get the layout for the second child window
        layout2 = create_layout2()
        # Update the main window with the layout for the second child window
        window['frame2'].update(layout2, visible=True)
        # Disable the 'Create Child Window 2' button
        window['Create Child Window 2'].update(disabled=True)
    elif event == 'Add Item':
        # Add an item to the listbox in the second child window
        window['listbox'].append('New Item')
    elif event == 'Remove Item':
        # Remove the selected item from the listbox in the second child window
        window['listbox'].remove(values['listbox'][0])

# Close the window
window.close()
