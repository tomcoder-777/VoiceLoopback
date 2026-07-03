from faster_whisper import WhisperModel

from config import (
    WHISPER_MODEL_PATH,
    DEVICE,
    COMPUTE_TYPE,
)


class WhisperEngine:

    def __init__(self):

        print("Loading Whisper...")

        # self.model = WhisperModel(
        #     WHISPER_MODEL,
        #     device=DEVICE,
        #     compute_type=COMPUTE_TYPE,
        # )
        print("Using model path:", WHISPER_MODEL_PATH)
        self.model = WhisperModel(
        WHISPER_MODEL_PATH,
        device=DEVICE,
        compute_type=COMPUTE_TYPE,
    )

        print("Whisper Ready!")

    def transcribe(self, audio):

        segments, info = self.model.transcribe(
            audio,
            beam_size=1,
            language="en"
        )

        text = ""

        for segment in segments:
            text += segment.text.strip() + " "
        return text.strip()