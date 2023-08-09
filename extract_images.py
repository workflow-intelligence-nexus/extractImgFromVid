#!/usr/bin/env python3
import os
import sys
import subprocess

def extract_images(video_path):
    # Check if ffmpeg is installed
    try:
        subprocess.run(["ffmpeg", "-version"], check=True)
    except FileNotFoundError:
        print("ffmpeg is not installed. Please install it and try again.")
        sys.exit(1)

    # Check if the video file exists
    if not os.path.exists(video_path):
        print(f"Video file '{video_path}' does not exist.")
        sys.exit(1)

    # Create the TrainingImages directory if it does not exist
    output_dir = "TrainingImages"
    os.makedirs(output_dir, exist_ok=True)

    # Extract images using ffmpeg (2 images per second)
    output_path = os.path.join(output_dir, "image_%04d.jpg")
    command = [
        "ffmpeg",
        "-i", video_path,
        "-vf", "fps=2",  # 2 frames per second
        "-q:v", "2",  # High quality JPEG
        output_path
    ]

    # Run the command
    subprocess.run(command)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_video>")
        sys.exit(1)

    video_path = sys.argv[1]
    extract_images(video_path)
    print("Images extracted successfully!")
