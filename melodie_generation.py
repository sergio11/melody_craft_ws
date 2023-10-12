from audiocraft.models import MusicGen
from .sse_server import send_sse_event

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

def generate_melody(text):
    """
    Generate a melody from the given text and send SSE notifications.

    Args:
        text (str): The text used to generate the melody.
    """
    try:
        send_sse_event("info", "Defining the text for the melody")
        send_sse_event("info", "Loading the pre-trained model...")
        model = MusicGen.get_pretrained('facebook/musicgen-small')

        estimated_duration = calculate_duration(text)
        send_sse_event("info", f"Estimated duration of the melody: {estimated_duration} seconds")

        generation_params = {
            'use_sampling': True,
            'top_k': 250,
            'duration': estimated_duration
        }
        send_sse_event("info", f"Setting generation parameters: {generation_params}")
        model.set_generation_params(**generation_params)
        send_sse_event("info", "Generating the melody from the text...")
        output = model.generate(
            descriptions=[text],
            progress=True,
            return_midi=True  # Request to return a MIDI file instead of tokens
        )

        # The MIDI file is in output['midi']
        midi_file = output['midi']

        # Send the MIDI file via SSE
        send_sse_event("success", "Melody generated", midi_file)

    except Exception as e:
        send_sse_event("error", f"Error: {str(e)}")