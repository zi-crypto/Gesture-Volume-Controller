# Hand Landmark Detector with Gesture-Controlled Media

## Project Overview

This project is a **Hand Landmark Detector** that allows gesture-based control of various media functions such as adjusting the volume, pausing or playing videos, and seeking forward or backward using hand gestures. The system tracks and places numbered landmarks on the detected hand in real-time. By calculating the **Euclidean distance** between specific landmarks, the user can control the volume. Additionally, snapping fingers can pause or play videos, and other hand gestures can be used to seek through media without touching the keyboard or mouse.

## Key Features

- **Real-Time Hand Tracking**: Detects the hand and tracks its movements with numbered landmarks.
- **Gesture-Based Volume Control**: Adjust the volume of your PC by moving your hand and using finger landmarks.
- **Snap Detection**: Pause or play videos by snapping your fingers.
- **Gesture-Controlled Video Seeking**: Seek forward or backward in a video with specific hand gestures.
- **Completely Hands-Free**: No need for physical contact with the PC—everything is controlled via hand gestures.

## Technologies Used

The following technologies were used in the project:

- **MediaPipe**: For real-time hand landmark detection and tracking.
- **OpenCV**: For capturing video feed from the webcam and rendering the hand landmarks.
- **NumPy**: For calculating the **Euclidean distance** between hand landmarks.
- **Pynput**: For simulating key presses and controlling media actions like volume adjustment, play/pause, and video seeking.
- **Python**: The core language that integrates all components and controls the application flow.

## How It Works

### Hand Landmark Detection
- Using **MediaPipe**, the software detects 21 unique landmarks on the hand in real-time. Each landmark has an index number corresponding to its position on the hand (e.g., tips of fingers, knuckles, etc.).

### Volume Control
- The **Euclidean distance** between two landmarks (such as the thumb and index finger) is calculated.
- By changing this distance (e.g., by bringing the thumb and index finger closer or farther apart), the system adjusts the PC volume.

### Snap Detection for Play/Pause
- The system detects the distinct movement and sound signature of a **finger snap** using audio and visual cues.
- When a snap is detected, the software triggers the play/pause function of the current media.

### Video Seeking with Gestures
- Specific hand gestures are detected by tracking the position of landmarks.

## Installation

To run this project on your local machine, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-repository/hand-gesture-media-control.git
    ```

2. **Install the required dependencies**

3. **Run the application**:
    ```bash
    python GestureVolumeControl.py
    ```

## Usage

1. **Start the webcam feed**: The software will begin tracking your hand in real-time.
2. **Control volume**: Use the distance between your thumb and index finger to adjust the volume.
3. **Snap to pause/play**: Snap your fingers to pause or resume the video.

## Example Gestures

- **Volume Control**: Move your thumb and index finger closer together to lower the volume, and farther apart to increase it.
- **Snap Detection**: A single finger snap will pause or resume the video.
- **Seek Gestures**: touching thumb with pinky skips backward, and touching thumb with ring finger skips forward.

## Future Improvements

- **Multi-Hand Support**: Add the ability to control the system with both hands for more advanced gestures.
- **Customizable Gestures**: Allow users to define their own gestures for different media controls.
- **Integration with More Applications**: Extend the functionality to control more media applications and other PC tasks.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributors

- **Ziad Amer** - Lead Developer and Gesture Control Engineer

## Acknowledgments

We thank the developers of **MediaPipe** and **OpenCV** for providing the tools that made this project possible.
