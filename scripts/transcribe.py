import argparse
import whisper
import os

# Setup argument parser
parser = argparse.ArgumentParser(description="Transcribe an audio file using Whisper.")
parser.add_argument("--file", required=True, help="Path to the audio file to transcribe.")
args = parser.parse_args()

AUDIO_PATH = args.file

print("🔁 Loading model...")
model = whisper.load_model("base")

print("🎧 Transcribing audio...")
result = model.transcribe(AUDIO_PATH)

print("\n✅ Transcription complete!\n")
print("🔊 Transcribed Text:\n")
print(result["text"])

# Save output
os.makedirs("outputs", exist_ok=True)
with open("outputs/transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
print("\n💾 Transcription saved to outputs/transcript.txt")
