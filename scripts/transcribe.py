import whisper
import os

AUDIO_PATH = "audio_samples/sample.mp3"
OUTPUT_PATH = "outputs/transcript.txt"

print("🔁 Loading model...")
model = whisper.load_model("base")

print("🎧 Transcribing audio...")
result = model.transcribe(AUDIO_PATH)

print("\n✅ Transcription complete!\n")
print("🔊 Transcribed Text:\n")
print(result["text"])

# Save to file
os.makedirs("outputs", exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"\n💾 Transcription saved to {OUTPUT_PATH}")

