import numpy as np
from queue import Empty
from silero_vad import load_silero_vad, get_speech_timestamps


class VADWorker:

    def __init__(self, raw_audio_queue, speech_queue):

        self.raw_audio_queue = raw_audio_queue
        self.speech_queue = speech_queue

        print("Loading Silero VAD...")

        self.model = load_silero_vad()

        print("Silero Ready!")

        self.buffer = []

        # 1 second of audio
        self.max_chunks = 32

    def run(self):

        while True:

            try:
                chunk = self.raw_audio_queue.get(timeout=0.1)
            except Empty:
                continue

            chunk = chunk.flatten().astype(np.float32) / 32768.0

            self.buffer.append(chunk)

            if len(self.buffer) < self.max_chunks:
                continue

            audio = np.concatenate(self.buffer)

            speech = get_speech_timestamps(
                audio,
                self.model,
                sampling_rate=16000
            )

            if speech:

                merged_audio = []

                for segment in speech:
                    merged_audio.append(
                        audio[segment["start"]:segment["end"]]
                    )

                if merged_audio:
                    speech_audio = np.concatenate(merged_audio)
                    self.speech_queue.put(speech_audio)

            self.buffer.clear()