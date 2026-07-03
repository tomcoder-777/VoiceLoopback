# from faster_whisper import WhisperModel

# print("Loading model...")

# model = WhisperModel(
#     "small",
#     device="cpu",
#     compute_type="int8"
# )

# print("Model loaded!")

from faster_whisper import WhisperModel
import time

print("Loading FastWhisper...")

start = time.time()

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

end = time.time()

print(f"Loaded in {end-start:.2f} seconds")
print("Model is ready!")