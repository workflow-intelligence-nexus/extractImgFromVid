
# Video Frame Extractor

This repository contains a Python script that extracts still images from a given video file. The extracted images are placed in a subdirectory named "TrainingImages." The script is designed to generate an image every half second of the video, making it suitable for training a YOLOv8 object recognition model.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- **Python 3:** The script is written in Python 3 and requires it to be installed on your system.
- **ffmpeg:** The script uses the `ffmpeg` command-line tool to process the video file. It must be installed on your system.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/videoframe-extractor.git
   ```

2. **Navigate to the directory:**
   ```bash
   cd videoframe-extractor
   ```

3. **Install ffmpeg (if not already installed):** On macOS, you can install ffmpeg using Homebrew:
   ```bash
   brew install ffmpeg
   ```

## Usage

1. **Make the script executable (optional):**
   ```bash
   chmod +x extract_images.py
   ```

2. **Run the script with the path to the video file:**
   ```bash
   python extract_images.py path_to_video_file
   ```
   Replace `path_to_video_file` with the actual path to the video file you want to process.

3. **Find the extracted images:** The extracted images will be saved in the "TrainingImages" subdirectory within the current directory.

## Contributing

Feel free to fork the repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

