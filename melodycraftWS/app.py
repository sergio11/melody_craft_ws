from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room
from melody_generation import generate_melody
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(24)
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    """
    Event handler for when a client connects to the server.
    Creates a room for the client using their client_id.
    """
    client_id = request.args.get('client_id')
    join_room(client_id)

@socketio.on('generate_melody')
def handle_generate_melody(data):
    """
    Event handler for generating a melody based on client input.
    Takes the client's text input, generates a melody, and sends it back to the client.
    """
    text = data['text']
    client_id = data['client_id']

    try:
        # Call the generate_melody function
        generate_melody(text, client_id)
    except Exception as e:
        # Handle exceptions in case of an error
        emit('error', str(e), room=client_id)

if __name__ == '__main__':
    socketio.run(app, debug=True)