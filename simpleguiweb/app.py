# -*- coding: utf-8 -*-

from flask import Flask, render_template_string
import PySimpleGUIWeb as sg

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = sg.FlexForm('Formulario de Exemplo', default_element_size=(20, 1), layout=[      
                    [sg.Text('Digite um texto:'), sg.InputText()],      
                    [sg.Submit(), sg.Cancel()]      
                    ])
    while True:
        button, values = form.Read()
        if button == 'Cancel' or None:
            break
        if button == 'Submit':
            return f'O texto digitado foi: {values[0]}'
    return render_template_string(form.GetPage())

if __name__ == '__main__':
    app.run(debug=True)
 