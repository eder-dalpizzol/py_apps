import PySimpleGUI as sg

values = sg.Window('', [[sg.Input(key= '-INPUT-'), sg.Button('Ok'), sg.Button('Cancel')]]).read()

print(values.get('-INPUT-'))