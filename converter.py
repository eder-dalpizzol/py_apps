import PySimpleGUI as sg

sg.theme('Purple')
layout = [
  [
    sg.Text('Value:'), sg.Input(key= '-INPUT-'), 
    sg.Text('Units:'), sg.Combo(['km to mile', 'kg to pound', 'sec to min'], key='-UNITS-'),
    sg.Button('Convert', key= '-CONVERT-')
  ],
  [sg.Text('Output', key= '-OUTPUT-')]
]

window = sg.Window('Converter', layout)

while True:
  event, values = window.read()

  if event == sg.WIN_CLOSED:
    break

  if event == '-CONVERT-':
    input_value = values['-INPUT-']
    if input_value.isnumeric():
      if values['-UNITS-'] != '':
        match values['-UNITS-']:
          case 'km to mile':
            output = round(float(input_value) * 0.6214, 2)
            output_str = f'{input_value} km are {output} miles'
          case 'kg to pound':
            output = round(float(input_value) * 2.20462, 2)
            output_str = f'{input_value} kg are {output} pounds'
          case 'sec to min':
            output = round(float(input_value) / 60, 2)
            output_str = f'{input_value} seconds are {output} minutes'
      else:
        output_str = 'Select a type of convertion'
    else:
      output_str = 'Insert a valid number'    

    window['-OUTPUT-'].update(output_str)

window.close()