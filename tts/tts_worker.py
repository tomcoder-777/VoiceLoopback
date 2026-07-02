from queue import Queue
from tts.supertonic_engine import SupertonicEngine


class TTSWorker:

    def __init__(self, text_queue):

        self.text_queue = text_queue

        self.engine = SupertonicEngine()

    def run(self):

        while True:

            text = self.text_queue.get()

            if text.strip():

                self.engine.speak(text)