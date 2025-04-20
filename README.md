# AI Fitness Trainer

An AI-powered fitness trainer using pose detection and feedback for workout guidance.

## Features
- Real-time pose detection
- Personalized workout suggestions
- Repetition counting and form correction

## Tech Stack
- OpenCV, MediaPipe
- Python

## Folder Structure
├── pose_detection.py           # Real-time webcam feed + pose landmarks
├── exercise_classifier.py      # Recognize the type of exercise
├── rep_counter.py              # Count reps based on joint angles
├── feedback.py                 # Form feedback and accuracy
├── training_plan.py            # Dynamic plan based on performance
└── main.py                     # Integrate all modules
- `documentation/` – Documents for the project
