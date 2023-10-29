from socketIO_client import SocketIO

class MelodyCraftClient:
    
    def __init__(self, server_url, client_id):
        self.server_url = server_url
        self.client_id = client_id
        self.socket = SocketIO(server_url)
        self.event_listeners = {}  # Dictionary to store event listeners

        # Connect to the server and join the room
        self.socket.on('connect', self.on_connect)
        self.socket.on('error', self.on_error)

    def on_connect(self):
        print(f'Connected to server with client ID: {self.client_id}')

    def on_error(self, error_message):
        print('Error:', error_message)

    def generate_melody(self, text):
        data = {'text': text, 'client_id': self.client_id}
        self.socket.emit('generate_melody', data)

    def add_event_listener(self, event, callback):
        """
        Add a custom event listener for the given event.
        """
        self.socket.on(event, self.on_custom_event)
        self.event_listeners[event] = callback

    def on_custom_event(self, data):
        """
        Handle incoming custom events by notifying the registered listener.
        """
        event = data['event']
        if event in self.event_listeners:
            self.event_listeners[event](data['data'])

    def remove_event_listener(self, event):
        """
        Remove a custom event listener for the given event.
        """
        if event in self.event_listeners:
            self.socket.off(event)
            del self.event_listeners[event]

    def disconnect(self):
        self.socket.disconnect()