import streamlit as st
import subprocess
from pathlib import Path
import os

if not Path("MeiGen-MultiTalk").exists():
    os.system("git lfs install")
    os.system("git clone https://huggingface.co/MeiGen-AI/MeiGen-MultiTalk")

st.title("🎥 MeiGen AI - Talking Avatar Generator")

# Upload files
audio = st.file_uploader("Upload your audio file", type=["wav", "mp3"])
image = st.file_uploader("Upload a face image", type=["jpg", "png"])

if audio and image:
    audio_path = Path("audio_input.wav")
    image_path = Path("image_input.png")

    with open(audio_path, "wb") as f:
        f.write(audio.read())
    with open(image_path, "wb") as f:
        f.write(image.read())

    st.info("Running MeiGen inference... please wait ⏳")

    # Run MeiGen inference script (adjust depending on repo you fork)
    command = [
        "python", "inference.py",
        "--audio", str(audio_path),
        "--image", str(image_path),
        "--output", "output.mp4"
    ]
    subprocess.run(command)

    if Path("output.mp4").exists():
        st.video("output.mp4")
        st.success("✅ Video generated successfully!")
