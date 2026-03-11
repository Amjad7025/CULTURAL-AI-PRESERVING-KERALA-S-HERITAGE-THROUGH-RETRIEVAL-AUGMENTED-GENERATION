# audio_processing.py
from faster_whisper import WhisperModel

# Choose model: tiny, base, small, medium, large
model = WhisperModel("base", device="cpu", compute_type="float32")

def transcribe_audio(audio_path):
    segments, info = model.transcribe(audio_path)
    text = " ".join([segment.text for segment in segments])
    return text
