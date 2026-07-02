# VoiceLoopback

A lightweight local speech loopback prototype that listens to your microphone, transcribes speech with Whisper, and speaks the recognized text back using Supertonic.

## What it does

- Captures microphone audio
- Uses VAD to detect speech regions
- Transcribes speech with faster-whisper
- Sends recognized text to a TTS worker for playback

## Requirements

- Python 3.10+
- A working microphone
- Speakers or headphones

## Local setup

1. Clone the repository
   ```bash
   git clone https://github.com/tomcoder-777/VoiceLoopback
   cd VoiceLoopback
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app
   ```bash
   python app.py
   ```

5. Speak into the microphone and listen for the synthesized reply.

> Use headphones to avoid microphone feedback while testing.

## Notes

- The current configuration uses Whisper tiny on CPU for a lighter local experience.
- The first run may download model weights and take a little longer.
- On some systems, audio backend setup may require additional OS-level audio drivers.

## Troubleshooting

- If audio playback fails, verify your speakers/headphones are connected.
- If microphone input is silent, check your default input device in your OS settings.
- If the app cannot import dependencies, make sure the virtual environment is active.
