import whisper
import tempfile
import os

# Load model once
model = whisper.load_model("base")

# Set ffmpeg path manually
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg-8.0.1-essentials_build\bin"

def transcribe_audio(audio_file):

    # Save uploaded audio temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_file.read())
        temp_audio_path = temp_audio.name

    # Transcribe
    result = model.transcribe(temp_audio_path)

    return result["text"]