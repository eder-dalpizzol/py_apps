from flask import Flask, render_template
from flask_socketio import SocketIO
import PySimpleGUIWeb as sg

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

sg.ChangeLookAndFeel('GreenMono')

layout = [
    [sg.Text('Enter your name:')],
    [sg.Input()],
    [sg.Button('OK')]
]

window = sg.Window('My Web App', layout, web_port=8000)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

if __name__ == '__main__':
    socketio.run(app, debug=True)
