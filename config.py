# Audio
SAMPLE_RATE = 16000
CHANNELS = 1
DTYPE = "int16"

# Record until silence
CHUNK_DURATION = 0.1          # 100 ms
SILENCE_THRESHOLD = 200
SILENCE_DURATION = 0.8        # seconds

# Whisper
WHISPER_MODEL_PATH = "models/whisper"
# WHISPER_MODEL = "tiny"
DEVICE = "cpu"
COMPUTE_TYPE = "int8"

# Supertonic

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
WHISPER_MODEL_PATH = str(BASE_DIR / "models" / "whisper")
SUPERTONIC_MODEL_PATH = str(BASE_DIR / "models" / "supertonic3")

VOICE = "F1"
LANGUAGE = "en"
