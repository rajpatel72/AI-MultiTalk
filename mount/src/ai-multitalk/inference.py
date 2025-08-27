import argparse
import os
from generate_multitalk import generate_video  # <- this comes from MultiTalk repo

def run_inference(audio_files, ref_image, prompt, output_path="output.mp4"):
    """
    Run a simple MultiTalk inference and save video.
    """
    print(">>> Starting inference...")
    video_path = generate_video(
        audio_files=audio_files,
        ref_image=ref_image,
        prompt=prompt,
        output_path=output_path
    )
    print(f">>> Inference complete. Video saved to {video_path}")
    return video_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run MultiTalk inference")
    parser.add_argument("--audio", nargs="+", required=True, help="Path(s) to audio file(s)")
    parser.add_argument("--image", required=True, help="Path to reference image")
    parser.add_argument("--prompt", required=True, help="Prompt text for conversation")
    parser.add_argument("--out", default="output.mp4", help="Output video path")

    args = parser.parse_args()

    if not os.path.exists(args.image):
        raise FileNotFoundError(f"Reference image not found: {args.image}")

    for a in args.audio:
        if not os.path.exists(a):
            raise FileNotFoundError(f"Audio file not found: {a}")

    run_inference(args.audio, args.image, args.prompt, args.out)
