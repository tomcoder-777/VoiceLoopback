from faster_whisper import WhisperModel
from config import MODEL_NAME, DEVICE, COMPUTE_TYPE, BEAM_SIZE


class WhisperEngine:
    def __init__(self):
        print("Loading Whisper Tiny...")

        self.model = WhisperModel(
            MODEL_NAME,
            device=DEVICE,
            compute_type=COMPUTE_TYPE
        )

        print("Whisper Ready!")

    def transcribe(self, audio):

        segments, info = self.model.transcribe(
            audio,
            beam_size=BEAM_SIZE
        )

        return [segment.text.strip() for segment in segments]