from audio.capture import AudioCapture

capture = AudioCapture()

audio = capture.record()

if audio is None:
    print("No speech detected.")
else:
    print("Recording completed.")
    print("Shape :", audio.shape)
    print("Type  :", audio.dtype)
    print("Min   :", audio.min())
    print("Max   :", audio.max())