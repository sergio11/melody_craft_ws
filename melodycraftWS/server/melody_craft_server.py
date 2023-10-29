from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room
import secrets
from melodycraftWS.server.melody_generation import generate_melody

class MelodyCraftServer:
    
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = secrets.token_hex(24)
        self.socketio = SocketIO(self.app)
        self.socketio.on_event('connect', self.handle_connect)
        self.socketio.on_event('generate_melody', self.handle_generate_melody_request)
        self.socketio.on_event('disconnect', self.handle_disconnect)

    def run(self, debug=False):
        self.socketio.run(self.app, debug=debug)

    def handle_generate_melody(self, text, client_id):
        try:
            # Validate the input data
            if not text:
                raise ValueError("Empty input text")
            # Melody generation logic
            melody = generate_melody(text, client_id)
            # Send the generated melody to the client
            emit('melody_generated', melody, room=client_id)
        except ValueError as e:
            emit('error', str(e), room=client_id)
        except Exception as e:
            emit('error', "Unexpected error", room=client_id)

    def handle_connect(self):
        client_id = request.args.get('client_id')
        join_room(client_id)

    def handle_generate_melody_request(self, data):
        text = data['text']
        client_id = data['client_id']
        self.handle_generate_melody(text, client_id)

    def handle_disconnect(self):
        # Perform disconnection actions if needed
        pass