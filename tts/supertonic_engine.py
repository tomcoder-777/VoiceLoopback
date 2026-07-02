import numpy as np
import sounddevice as sd

try:
    from supertonic import TTS
except ImportError:  # pragma: no cover - optional dependency
    TTS = None


class SupertonicEngine:

    def __init__(self):

        print("Loading Supertonic...")

        self.tts = None
        self.voice = None
        self.sample_rate = 22050

        if TTS is None:
            print("Supertonic is not installed. Install the requirements to enable speech playback.")
            return

        self.tts = TTS()
        self.voice = self.tts.get_voice_style("F1")
        self.sample_rate = getattr(self.tts, "sample_rate", self.sample_rate)

        print("Supertonic Ready!")

    def speak(self, text):

        if not text or not text.strip():
            return

        if self.tts is None:
            print(f"TTS unavailable: {text}")
            return

        print(f"TTS: {text}")

        wav, _ = self.tts.synthesize(
            text=text,
            voice_style=self.voice,
            lang="en"
        )

        wav = np.asarray(wav, dtype=np.float32).squeeze()

        if wav.ndim > 1:
            wav = wav.mean(axis=1)

        sd.stop()
        sd.play(wav, self.sample_rate)

    def stop(self):

        sd.stop()