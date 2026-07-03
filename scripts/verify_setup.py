from pathlib import Path
import importlib
import sounddevice as sd
import sys

ROOT = Path(__file__).resolve().parent.parent

print("=" * 50)
print("VoiceLoopback Setup Verification")
print("=" * 50)

# --------------------------------------------------
# Python Version
# --------------------------------------------------

print("\n[1] Python")

print(f"Version : {sys.version.split()[0]}")

if sys.version_info < (3, 11):
    print("FAIL : Python 3.11 or newer required")
else:
    print("PASS")

# --------------------------------------------------
# Required Packages
# --------------------------------------------------

print("\n[2] Python Packages")

packages = [
    "faster_whisper",
    "supertonic",
    "sounddevice",
    "numpy",
]

for pkg in packages:

    try:
        importlib.import_module(pkg)
        print(f"PASS : {pkg}")

    except ImportError:
        print(f"FAIL : {pkg}")

# --------------------------------------------------
# Whisper Model
# --------------------------------------------------

print("\n[3] Whisper Model")

whisper = ROOT / "models" / "whisper"

required = [
    "config.json",
    "model.bin",
    "tokenizer.json",
]

missing = False

for f in required:

    if not (whisper / f).exists():
        print(f"Missing : {f}")
        missing = True

if not missing:
    print("PASS")

# --------------------------------------------------
# Supertonic Model
# --------------------------------------------------

print("\n[4] Supertonic Model")

supertonic = ROOT / "models" / "supertonic3"

required = [
    "config.json",
    "onnx",
    "voice_styles",
]

missing = False

for f in required:

    if not (supertonic / f).exists():
        print(f"Missing : {f}")
        missing = True

if not missing:
    print("PASS")

# --------------------------------------------------
# Audio Devices
# --------------------------------------------------

print("\n[5] Audio Devices")

devices = sd.query_devices()

input_found = False
output_found = False

for d in devices:

    if d["max_input_channels"] > 0:
        input_found = True

    if d["max_output_channels"] > 0:
        output_found = True

print(f"Input Device  : {'PASS' if input_found else 'FAIL'}")
print(f"Output Device : {'PASS' if output_found else 'FAIL'}")

# --------------------------------------------------
# Summary
# --------------------------------------------------

print("\n" + "=" * 50)
print("Verification Complete")
print("=" * 50)