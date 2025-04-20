import cv2
import mediapipe as mp

class PoseDetector:
    def __init__(self):
        self.pose = mp.solutions.pose.Pose()
        self.drawing = mp.solutions.drawing_utils

    def get_landmarks(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.pose.process(rgb)
        if result.pose_landmarks:
            self.drawing.draw_landmarks(frame, result.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)
            landmarks = result.pose_landmarks.landmark
            return landmarks, frame
        return None, frame