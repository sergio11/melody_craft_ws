from flask_sse import sse
import time

event_queue = []

def send_sse_event(event_type, message, data=None):
    """
    Send an SSE event to clients.

    Args:
        event_type (str): The type of the SSE event.
        message (str): The message to send.
        data (dict, optional): Additional data to include in the event.
    """
    event = {"message": message, "type": event_type}
    if data is not None:
        event["data"] = data

    event_queue.append(event)

def sse_stream():
    """
    Server-Sent Events stream generator.

    Yields:
        str: An SSE event formatted as a string.
    """
    while True:
        if event_queue:
            event = event_queue.pop(0)
            sse.publish(event, type=event['type'])
        time.sleep(1)