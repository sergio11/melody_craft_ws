from flask import Flask, Response, request
from flask_sse import sse
from .melodie_generation import generate_melody
from .sse_server import sse_stream

app = Flask(__name__)
app.register_blueprint(sse, url_prefix='/stream')

@app.route('/')
def index():
    """
    Returns a message indicating that the SSE server is running.
    """
    return 'SSE Server is running'

@app.route('/generate_melody', methods=['POST'])
def generate_melody_route():
    """
    Endpoint to start the melody generation process.

    Returns:
        str: A message indicating whether the process has started or an error message.
    """
    if request.method == 'POST':
        text = request.json.get('text', '')
        if text:
            generate_melody(text)
            return 'Processing started'
        else:
            return 'Text not provided', 400
    else:
        return 'Method not allowed', 405

@app.route('/stream')
def stream():
    """
    Endpoint for streaming SSE events to the client.

    Returns:
        Response: An SSE response stream.
    """
    return Response(sse_stream(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run()