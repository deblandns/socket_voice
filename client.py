import socketio
import pyaudio
import base64

socket_io = socketio.Client()

@socket_io.event
def connect():
    print("we are connected to server")

@socket_io.event
def disconnect():
    print("we are disconnected from server")

@socket_io.event
def voice(data):
    audio_data = base64.b64decode(data)
    stream.write(audio_data)

socket_io.connect('http://127.0.0.1:7332')

# audio stream setup
p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True, input=True, frames_per_buffer=1024)

def send_audio():
    while True:
        data = stream.read(1024)
        encoded_data = base64.b64encode(data).decode('utf-8')
        socket_io.emit('voice', encoded_data)

if __name__ == "__main__":
    send_audio()