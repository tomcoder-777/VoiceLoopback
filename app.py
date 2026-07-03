from audio.capture import AudioCapture
from stt.whisper_engine import WhisperEngine
from tts.supertonic_engine import SupertonicEngine


def main():

    capture = AudioCapture()
    stt = WhisperEngine()
    tts = SupertonicEngine()
    print("\nVoiceLoopback Started")
    while True:

        audio = capture.record()
        text = stt.transcribe(audio)
        if not text:
            continue
        print(f"\nYou: {text}")
        tts.speak(text)
        
if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        print("\nGoodbye!")