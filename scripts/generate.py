import sys
import numpy as np
import soundfile as sf
from kokoro import KPipeline

# Parse arguments cleanly
script_path = sys.argv[1] if len(sys.argv) > 1 else "script.txt"
voice_choice = sys.argv[2] if len(sys.argv) > 2 else "af_bella"

# Read user script text
with open(script_path, "r", encoding="utf-8") as f:
    text = f.read().strip()

print(f"Generating TTS audio with voice '{voice_choice}'...")

# Initialize American English pipeline
pipeline = KPipeline(lang_code='a')

# Generate audio chunks (speed=1.1 for quick YouTube Shorts pacing)
generator = pipeline(text, voice=voice_choice, speed=1.1)

audio_chunks = [chunk for _, _, chunk in generator]
audio = np.concatenate(audio_chunks)

# Save WAV output at native 24kHz sample rate
output_file = "voiceover.wav"
sf.write(output_file, audio, 24000)

print(f"Done! Saved audio output to {output_file}")
