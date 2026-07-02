from supertonic import TTS
import sounddevice as sd


class SupertonicEngine:

    def __init__(self):

        print("Loading Supertonic...")

        self.tts = TTS()

        self.voice = self.tts.get_voice_style("F1")

        print("Supertonic Ready!")

    def speak(self, text):

        if not text.strip():
            return

        print(f"TTS: {text}")

        wav, duration = self.tts.synthesize(
            text=text,
            voice_style=self.voice,
            lang="en"
        )

        wav = wav.squeeze()

        sd.play(
            wav,
            self.tts.sample_rate
        )

        sd.wait()