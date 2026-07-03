# 1. Clone the repository
git clone https://github.com/tomcoder-777/VoiceLoopback.git

cd VoiceLoopback

# 2. Create virtual environment
python -m venv venv

# 3. Activate it

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Download AI models
python scripts/download_models.py

# 6. Verify installation
python scripts/verify_setup.py

# 7. Run the application
python app.py

VoiceLoopback/
│
├── audio/
├── stt/
├── tts/
├── scripts/
│   ├── download_models.py
│   └── verify_setup.py
│
├── models/
│   ├── whisper/
│   └── supertonic3/
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
