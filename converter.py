import PySimpleGUI as sg

# Define o tema da janela como "Purple"
sg.theme('Purple')

# Define a estrutura da janela com um rótulo, campo de entrada, rótulo, lista suspensa e botão
layout = [
  [
    sg.Text('Value:'), sg.Input(key= '-INPUT-'), 
    sg.Text('Units:'), sg.Combo(['km to mile', 'kg to pound', 'sec to min'], key='-UNITS-'),
    sg.Button('Convert', key= '-CONVERT-')
  ],
  [sg.Text('Output', key= '-OUTPUT-')]
]

# Cria a janela com o título "Converter" e a estrutura definida anteriormente
window = sg.Window('Converter', layout)

# Loop principal da janela
while True:
  # Lê o evento e os valores dos campos de entrada
  event, values = window.read()

  # Se o evento for o fechamento da janela, sai do loop
  if event == sg.WIN_CLOSED:
    break

  # Se o evento for o botão "Convert", realiza a conversão
  if event == '-CONVERT-':
    input_value = values['-INPUT-']
    # Verifica se o valor inserido é numérico
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
        # Se não foi selecionada uma unidade de conversão, exibe uma mensagem de erro
        output_str = 'Select a type of convertion'
    else:
      # Se o valor inserido não é numérico, exibe uma mensagem de erro
      output_str = 'Insert a valid number'    

    # Atualiza o campo de saída com o resultado da conversão
    window['-OUTPUT-'].update(output_str)

# Fecha a janela
window.close()
