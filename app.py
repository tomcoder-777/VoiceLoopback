import time
import threading
from queue import Queue
import time
from audio.capture import AudioCapture
from audio.vad import VADWorker
from stt.whisper_engine import WhisperEngine
from tts.supertonic_engine import SupertonicEngine
from tts.tts_worker import TTSWorker
# ============================
# Queues
# ============================

raw_audio_queue = Queue()
speech_queue = Queue()
text_queue = Queue()


# ============================
# Load Whisper
# ============================

engine = WhisperEngine()
# tts = SupertonicEngine()
tts_worker = TTSWorker(text_queue)
# ============================
# Whisper Worker
# ============================

def whisper_worker():

    while True:

        audio = speech_queue.get()

        stt_start = time.perf_counter()

        text = engine.transcribe(audio)

        stt_time = (time.perf_counter() - stt_start) * 1000

        print(f"\nSTT Time : {stt_time:.1f} ms")

        for line in text:

            if line.strip():

                print(f">> {line}")

                tts_start = time.perf_counter()

                text_queue.put(line)

                tts_queue_time = (time.perf_counter() - tts_start) * 1000

                print(f"TTS Queue : {tts_queue_time:.1f} ms")
# ============================
# Start VAD Worker
# ============================

vad = VADWorker(
    raw_audio_queue,
    speech_queue
)

vad_thread = threading.Thread(
    target=vad.run,
    daemon=True
)

vad_thread.start()


# ============================
# Start Whisper Worker
# ============================

stt_thread = threading.Thread(
    target=whisper_worker,
    daemon=True
)
tts_thread = threading.Thread(
    target=tts_worker.run,
    daemon=True
)
stt_thread.start()
tts_thread.start()


# ============================
# Start Microphone
# ============================

capture = AudioCapture(raw_audio_queue)

print("Listening...")

with capture.start():

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        print("\nStopped.")