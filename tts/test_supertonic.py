from supertonic import TTS
import soundfile as sf

print("Loading Supertonic...")

tts = TTS()

print("Loaded!")
print("Model:", tts.model_name)
print("Sample Rate:", tts.sample_rate)
print("Available Voices:", tts.voice_style_names)

# Load the voice style object
voice = tts.get_voice_style("F1")

print("Synthesizing...")

wav, duration = tts.synthesize(
    text="Hello. This is a Supertonic test.",
    voice_style=voice,
    lang="en"
)

print("Duration:", duration)
print("Original Shape:", wav.shape)
print("Original Dtype:", wav.dtype)

# Convert (1, samples) -> (samples,)
wav = wav.squeeze()

print("New Shape:", wav.shape)

# Save audio
sf.write(
    file="output.wav",
    data=wav,
    samplerate=tts.sample_rate,
    format="WAV"
)

print("Saved output.wav successfully!")