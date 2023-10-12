from audiocraft.models import MusicGen
from flask_socketio import emit, join_room

# Average Words Per Minute (WPM) estimation
AVERAGE_WPM = 150

def calculate_duration(text):
    """
    Calculate the estimated duration in seconds based on the number of words and the average WPM.
    
    Args:
        text (str): The text for which to estimate the duration.
        
    Returns:
        float: The estimated duration in seconds.
    """
    words = text.split()
    estimated_duration = len(words) / AVERAGE_WPM * 60
    return estimated_duration

def generate_melody(text, room):
    """
    Generate a melody from the given text and send progress updates to the specified client.

    Args:
        text (str): The text used to generate the melody.
        client_id (str): The ID of the client to send updates to.
    """
    try:
        emit("info", "Defining the text for the melody", room=room)
        emit("info", "Loading the pre-trained model...", room=room)
        model = MusicGen.get_pretrained('facebook/musicgen-small')
        estimated_duration = calculate_duration(text)
        emit("info", f"Estimated duration of the melody: {estimated_duration} seconds", room=room)
        generation_params = {
            'use_sampling': True,
            'top_k': 250,
            'duration': estimated_duration
        }
        emit("info", f"Setting generation parameters: {generation_params}", room=room)
        model.set_generation_params(**generation_params)
        emit("info", "Generating the melody from the text...", room=room)
        output = model.generate(
            descriptions=[text],
            progress=True,
            return_midi=True  # Request to return a MIDI file instead of tokens
        )
        # The MIDI file is in output['midi']
        midi_file = output['midi']

        # Send the MIDI file via Socket.IO to the specific client
        emit("success", "Melody generated", {'midi_file': midi_file}, room=room)
    except Exception as e:
        emit("error", f"Error: {str(e)}", room=room)