from supertonic import TTS
import sounddevice as sd

from config import (
    VOICE,
    LANGUAGE,
    SUPERTONIC_MODEL_PATH,
)

class SupertonicEngine:

    def __init__(self):

        print("Loading Supertonic...")
        self.tts = TTS(
        model="supertonic-3",
        model_dir=SUPERTONIC_MODEL_PATH,
        auto_download=False
        )
        self.voice = self.tts.get_voice_style(VOICE)
        print("Supertonic Ready!")
    def speak(self, text):

        if not text:
            return

        print(f"Assistant: {text}")

        wav, duration = self.tts.synthesize(
            text=text,
            voice_style=self.voice,
            lang=LANGUAGE
        )

        wav = wav.squeeze()
        sd.stop()
        sd.play(
            wav,
            self.tts.sample_rate
        )
        sd.wait()