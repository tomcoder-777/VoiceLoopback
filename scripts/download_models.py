from pathlib import Path
from faster_whisper import download_model
from supertonic import TTS


ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = ROOT / "models"

WHISPER_DIR = MODELS_DIR / "whisper"
SUPERTONIC_DIR = MODELS_DIR / "supertonic3"


def download_whisper():
    print("Downloading Whisper Tiny...")

    download_model(
        "tiny",
        output_dir=str(WHISPER_DIR)
    )

    print("Whisper downloaded.")


def download_supertonic():
    print("Downloading Supertonic 3...")

    TTS(
        model="supertonic-3",
        model_dir=str(SUPERTONIC_DIR),
        auto_download=True
    )

    print("Supertonic downloaded.")


if __name__ == "__main__":

    MODELS_DIR.mkdir(exist_ok=True)

    download_whisper()

    download_supertonic()

    print("\nAll models downloaded successfully!")