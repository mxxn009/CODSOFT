# Real-Time Face and Hand Detection with Recognition

This project performs real-time face and hand detection using a webcam and recognizes specific faces based on pre-encoded data. It uses OpenCV for video capture and display, MediaPipe for detecting faces and hands, and NumPy for encoding and comparison. Detected faces are matched against known faces, and bounding boxes are drawn around recognized faces and detected hands.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Structure](#project-structure)
4. [Libraries Used](#libraries-used)
5. [Explanation of Key Components](#explanation-of-key-components)
6. [Future Improvements](#future-improvements)

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Install the required libraries:
    ```bash
    pip install opencv-python mediapipe numpy
    ```

## Usage

1. Ensure your webcam is connected and functional.
2. Run the script:
    ```bash
    python <script_name>.py
    ```
3. A video window will open displaying the real-time video feed with detected faces and hands. Press 'q' to exit the program.

## Project Structure

- `<script_name>.py`: Main script containing the code for face and hand detection and recognition.

## Libraries Used

- **OpenCV (cv2)**: Handles video capture, drawing on frames, and displaying the video feed.
- **MediaPipe (mp)**: Detects faces and hands in real time. Provides pre-trained models for reliable face and hand detection.
- **NumPy (np)**: Used to store and compare face encodings using mathematical operations.

## Explanation of Key Components

1. **Face Detection**: 
    - The script captures frames from the webcam and uses MediaPipe’s `FaceDetection` model to detect faces.
    - Each detected face is cropped, encoded, and compared with known encodings to recognize familiar faces.
  
2. **Hand Detection**: 
    - The script also uses MediaPipe’s `Hands` model to detect hands in the video feed. Bounding boxes are drawn around detected hands.

3. **Face Recognition**:
    - Pre-loaded images of known faces are encoded and stored. When a new face is detected, its encoding is compared to the stored encodings using Euclidean distance. If the distance is below a set threshold, the face is recognized.

4. **Display**:
    - The OpenCV `imshow` function displays the real-time video feed with bounding boxes and labels.

## Future Improvements

1. **Replace Random Encodings**: Use a dedicated face encoding model, such as FaceNet, to generate real encodings instead of random vectors.
2. **Add Face and Hand Landmark Detection**: Utilize MediaPipe’s drawing utilities to draw landmarks on detected faces and hands.
3. **Optimize Face Matching**: Implement a more efficient face matching algorithm to improve recognition speed and accuracy.
