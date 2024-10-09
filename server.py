from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DEBLAND_secret_key'
socketio = SocketIO(app)

@socketio.on("connect")
def handle_connect():
    print("client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('voice')
def handle_voice(data):
    emit('voice', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=7332)