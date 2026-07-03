from faster_whisper import WhisperModel
print("Loading local Whisper model...")
model = WhisperModel(
    "models/whisper",
    device="cpu",
    compute_type="int8"
)
print("Success!")