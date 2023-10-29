# MelodyCraftWS 🎵

[![PyPI version](https://badge.fury.io/py/MelodyCraftWS.svg)](https://badge.fury.io/py/MelodyCraftWS)

MelodyCraftWS is a Python package that combines the power of text-based melody generation with real-time notifications using WebSockets. This project demonstrates the magic of turning lyrics or text into beautiful melodies and keeping you informed about the progress.

<p align="center">
  <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white" />
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
</p>

🚀 **Features:**
- Generate melodies from text input.
- Estimated duration based on the number of words and average WPM.
- Real-time progress updates via WebSockets.
- Send success or error notifications to the client.

## Implementation Details 🛠️

This project is built using the following tools and libraries:

- [Flask](https://flask.palletsprojects.com/): A micro web framework for building web applications.
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/): A Flask extension for WebSockets.
- [Audiocraft](https://github.com/yourusername/audiocraft): A Python library for music and audio generation.

## Usage 📦

1. Install the package via `pip`:
   
```bash
pip install MelodyCraftWS
```

2. Create a Flask application and integrate the package to generate melodies and send WebSocket events.

```python
# Import the necessary components and set up the MelodyCraftServer
from MelodyCraftWS import MelodyCraftServer

server = MelodyCraftServer()
```

3. Start your application, and it's ready to generate melodies from text and send notifications in real-time.

```python
if __name__ == '__main__':
    server.run(debug=True)
```

### How to Generate Melodies 🎶

Send a POST request to the */generate_melody* endpoint with the text parameter containing the lyrics or text you want to transform into a melody.

The estimated duration is calculated based on the text's word count and an average words per minute (WPM) rate.

The melody is generated using the Audiocraft library, and real-time updates are sent to the client via WebSockets.

Success or error notifications are sent depending on the outcome.

#### Client Component

The client component, MelodyCraftClient, connects to the MelodyCraft server, sends text input for melody generation, and receives the generated melodies. It also allows custom event listeners for additional functionality.

##### Step 1: Preparation of the Client

Ensure you have the MelodyCraftClient class defined in a file, such as melodycraft_client.py.

```python
# melodycraft_client.py

from MelodyCraftWS import MelodyCraftClient

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
    client.generate_melody('Text input for melody generation')

    # Wait for user input to exit
    input('Press Enter to disconnect...')
    client.disconnect()
```

##### Step 2: Running the Client

Open a separate terminal and navigate to the location of the melodycraft_client.py file.
Run the client by executing the following command:

```bash
python melodycraft_client.py
```

This will start the client and connect to the server. You can use the client to generate melodies, receive custom events, and interact with the MelodyCraft server.

Make sure the values of 'server_url' and 'client_id' in the client file (melodycraft_client.py) are configured with the actual values corresponding to your server. You can also add or remove custom events and adjust the handling logic according to your needs.

### License 📜
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to contribute, report issues, and make this project even better!

### 🌟 Enjoy creating melodies with MelodyCraftWS! 🌟


