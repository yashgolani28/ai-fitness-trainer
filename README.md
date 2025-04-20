# AI Fitness Trainer

An AI-powered fitness trainer using pose detection and feedback for workout guidance.


##  Features

- Real-time webcam-based pose detection
- Automatic exercise type classification
- Accurate rep counting using angle tracking
- Posture/form feedback for better results
- Personalized training suggestions after each session

##  Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy

##  How It Works

1. **Pose Detection:** Uses MediaPipe to detect body landmarks from webcam.
2. **Exercise Recognition:** Classifies exercises like squats using landmark positions.
3. **Repetition Logic:** Measures angles between joints to count reps.
4. **Feedback Module:** Compares joint positions to ideal posture.
5. **Training Plan:** Suggests workout structure based on user performance.

##  Installation

```bash
pip install opencv-python mediapipe numpy

