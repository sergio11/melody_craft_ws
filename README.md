# SongCraftSEE 🎵

SongCraftSEE is a Python package that combines the power of text-based melody generation with real-time notifications using Server-Sent Events (SSE). This project demonstrates the magic of turning lyrics or text into beautiful melodies and keeping you informed about the progress.

<p align="center">
  <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white" />
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
</p>

🚀 **Features:**
- Generate melodies from text input.
- Estimated duration based on the number of words and average WPM.
- Real-time progress updates via SSE.
- Send success or error notifications to the client.

## Implementation Details 🛠️

This project is built using the following tools and libraries:

- [Flask](https://flask.palletsprojects.com/): A micro web framework for building web applications.
- [Flask-SSE](https://flask-sse.readthedocs.io/): A Flask extension for Server-Sent Events.
- [Audiocraft](https://github.com/yourusername/audiocraft): A Python library for music and audio generation.

## Usage 📦

1. Install the package via `pip`:

```bash
pip install songcraftsee
```

2. Create a Flask application and integrate the package to generate melodies and send SSE events.

3. Start your application, and it's ready to generate melodies from text and send notifications in real-time.

## How to Generate Melodies 🎶

Send a POST request to the /generate_melody endpoint with the text parameter containing the lyrics or text you want to transform into a melody.

The estimated duration is calculated based on the text's word count and an average words per minute (WPM) rate.

The melody is generated using the Audiocraft library, and real-time updates are sent to the client via SSE.

Success or error notifications are sent depending on the outcome.

## License 📜
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to contribute, report issues, and make this project even better!

🌟 Enjoy creating melodies with SongCraftSEE! 🌟
