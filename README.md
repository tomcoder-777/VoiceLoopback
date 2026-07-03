### 1. Clone the repository
```bashgit clone https://github.com/tomcoder-777/VoiceLoopback.git

cd VoiceLoopback
```
### 2. Create virtual environment
python -m venv venv

### 3. Activate it

#### Windows
```bash
venv\Scripts\activate
```

#### Linux/Mac
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Download AI models
```bash
python scripts/download_models.py
```

### 6. Verify installation
```bash
python scripts/verify_setup.py
```

### 7. Run the application
```bash
python app.py
```

```
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
```