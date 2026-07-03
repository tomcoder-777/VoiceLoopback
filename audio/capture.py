import sounddevice as sd
import numpy as np
import threading

from config import (
    SAMPLE_RATE,
    CHANNELS,
    SILENCE_THRESHOLD,
    SILENCE_DURATION,
)


class AudioCapture:

    def __init__(self):

        self.audio = []
        self.recording = False
        self.finished = threading.Event()
        self.block_size = 1600        # 100 ms

    def callback(self, indata, frames, time_info, status):

        if status:
            print(status)

        volume = np.max(np.abs(indata))

        if volume > SILENCE_THRESHOLD:

            self.recording = True
            self.silence_count = 0
            self.audio.append(indata.copy())

        elif self.recording:

            self.audio.append(indata.copy())
            self.silence_count += 1

            if self.silence_count >= int(SILENCE_DURATION * 10):
                self.finished.set()

    def record(self):

        self.audio = []
        self.recording = False
        self.silence_count = 0
        self.finished.clear()
        print("\nListening...")
        with sd.InputStream(

            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype=np.int16,
            blocksize=self.block_size,
            callback=self.callback
        ):

            self.finished.wait()
        audio = np.concatenate(self.audio)
        audio = audio.flatten()
        audio = audio.astype(np.float32)
        audio /= 32768.0
        return audio