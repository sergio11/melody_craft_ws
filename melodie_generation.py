from audiocraft.models import MusicGen

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
    Generate a melody from the given text and return the generated tokens.

    Args:
        text (str): The text used to generate the melody.

    Returns:
        list: The generated tokens.
    """
    try:
        print(f"Defining the text for the melody: {text}")
        print("Loading the pre-trained model...")
        model = MusicGen.get_pretrained('facebook/musicgen-small')

        estimated_duration = calculate_duration(text)
        print(f"Estimated duration of the melody: {estimated_duration} seconds")

        generation_params = {
            'use_sampling': True,
            'top_k': 250,
            'duration': estimated_duration
        }
        print(f"Setting generation parameters: {generation_params}")
        model.set_generation_params(**generation_params)
        print("Generating the melody from the text...")
        output = model.generate(
            descriptions=[text],
            progress=True,
            return_tokens=True
        )
        print(f"Generated tokens: {output[0]}")

        return output[0]

    except Exception as e:
        # You can handle the error here or raise it as needed
        raise Exception(f"Error: {str(e)}")
