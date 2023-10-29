# Import the MelodyCraftClient class
from melodycraftWS.client.melody_craft_client import MelodyCraftClient


if __name__ == '__main__':
    # Replace 'server_url' and 'client_id' with the actual values
    server_url = 'http://your-server-url.com'
    client_id = 'your_client_id'

    # Create an instance of the MelodyCraftClient
    client = MelodyCraftClient(server_url, client_id)

    # Define a custom event listener for 'custom_event'
    def custom_event_handler(data):
        print('Custom Event Received:', data)

    # Add the custom event listener
    client.add_event_listener('custom_event', custom_event_handler)

    # Example usage: Generate a melody
    text_input = 'This is an example text for melody generation.'
    client.generate_melody(text_input)

    # Wait for user input to disconnect
    input('Press Enter to disconnect...')
    client.disconnect()
