import PySimpleGUI as sg

def create_window(theme):
  sg.theme(theme)
  sg.set_options(font= 'Franklin 20')
  button_size = (6,3)
  layout = [
    [sg.Text('', font= 'Franklin 30', justification= 'right', expand_x= True, pad= (10,25), right_click_menu= theme_menu, key= '-OUTPUT-')],
    [sg.Button('Clear', expand_x= True, size=button_size), sg.Button('Enter',expand_x= True, size=button_size)],
    [sg.Button('7', size=button_size),sg.Button('8', size=button_size),sg.Button('9', size=button_size),sg.Button('%', size=button_size)],
    [sg.Button('4', size=button_size),sg.Button('5', size=button_size),sg.Button('6', size=button_size),sg.Button('*', size=button_size)],
    [sg.Button('1', size=button_size),sg.Button('2', size=button_size),sg.Button('3', size=button_size),sg.Button('-', size=button_size)],
    [sg.Button('0', expand_x= True, size=button_size),sg.Button('.', size=button_size),sg.Button('+', size=button_size)]
  ]

  return sg.Window('Calculator', layout)

theme_menu = ['menu', ['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 
                       'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 
                       'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 
                       'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 
                       'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 
                       'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 
                       'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 
                       'DarkGrey14', 'DarkGrey15', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 
                       'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 
                       'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 
                       'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 
                       'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 
                       'Default', 'Default1', 'DefaultNoMoreNagging', 'GrayGrayGray', 'Green', 'GreenMono', 'GreenTan', 
                       'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 
                       'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 
                       'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 
                       'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 
                       'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 
                       'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 
                       'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 
                       'PythonPlus', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 
                       'Tan', 'TanBlue', 'TealMono', 'Topanga']]
window = create_window('BrownBlue')

current_nmb = []
full_operation = []

while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED:
    break

  if event in theme_menu[1]:
    window.close()
    window = create_window(event)

  if event in ['0','1','2','3','4','5','6','7','8','9','.']:
    current_nmb.append(event)
    num_string = ''.join(current_nmb)
    window['-OUTPUT-'].Update(num_string)

  if event in ['*','%','+','-']:  
    full_operation.append(''.join(current_nmb))
    current_nmb = []
    full_operation.append(event)
    window['-OUTPUT-'].Update('')

  if event == 'Enter':
    full_operation.append(''.join(current_nmb))
    result = (eval(' '.join(full_operation)))
    window['-OUTPUT-'].Update(result)
    full_operation = []

  if event == 'Clear':
    full_operation = []
    current_nmb = []
    window['-OUTPUT-'].Update('')

window.close()