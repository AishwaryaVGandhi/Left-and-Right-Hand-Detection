# Left and Right Hand Detection 

A real-time hand detection application that uses computer vision to detect and track hands in a video stream.

## Features

- Real-time hand detection (1 or 2 hands)
- Visual display of 21 hand landmarks per hand
- Mirror mode for intuitive interaction

## Technology Stack
- **OpenCV**: Computer vision operations
- **cvzone**: Simplified hand tracking interface

## Installation

### Prerequisites
- Python 3.7+
- Webcam

### Setup
```bash
pip install opencv-python cvzone
```

## Usage
1. Run the script:
```bash
python Hand Detection.py
```

2. The application will:
    - Open a 720p video window
    - Show detected hands with landmarks
    - Display in mirror mode (flipped horizontally)

3. To exit the program press 'q'.
