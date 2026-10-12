import sys
import numpy as np
import soundfile as sf
from kokoro import KPipeline

# Get the script path from arguments (default to script.txt if omitted)
script_path = sys.argv[1] if len(sys.argv) > 1 else "script.txt"
voice_choice = sys.argv[2] if len(sys.argv) > 2 else "af_bella"

with open(script_path, "r", encoding="utf-8") as f:
    text = f.read().strip()

print(f"Generating audio using voice: {voice_choice}")

# Initialize Kokoro Pipeline ('a' = American English, 'b' = British English)
pipeline = KPipeline(lang_code='a')

# Generate TTS audio stream (speed=1.1 for high retention pacing)
generator = pipeline(text, voice=voice_choice, speed=1.1)

audio_chunks = [chunk for _, _, chunk in generator]
audio = np.concatenate(audio_chunks)

# Save to output file
output_file = "voiceover.wav"
sf.write(output_file, audio, 24000)
print(f"Success! Audio exported to {output_file}")
