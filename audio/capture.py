import sounddevice as sd
import numpy as np

from config import SAMPLE_RATE, CHANNELS, BLOCK_SIZE


class AudioCapture:

    def __init__(self, raw_audio_queue):
        self.raw_audio_queue = raw_audio_queue

    def callback(self, indata, frames, time_info, status):

        if status:
            print(status)

        self.raw_audio_queue.put(indata.copy())

    def start(self):

        return sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype=np.int16,
            blocksize=BLOCK_SIZE,
            callback=self.callback,
        )