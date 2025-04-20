import numpy as np

class RepCounter:
    def __init__(self, exercise):
        self.exercise = exercise
        self.stage = None
        self.count = 0

    def calculate_angle(self, a, b, c):
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)

        radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
        angle = np.abs(radians * 180.0 / np.pi)
        if angle > 180:
            angle = 360 - angle
        return angle

    def update(self, landmarks):
        if self.exercise == "Squat":
            hip = [landmarks[24].x, landmarks[24].y]
            knee = [landmarks[26].x, landmarks[26].y]
            ankle = [landmarks[28].x, landmarks[28].y]
            angle = self.calculate_angle(hip, knee, ankle)

            if angle > 160:
                self.stage = "up"
            if angle < 90 and self.stage == "up":
                self.stage = "down"
                self.count += 1

        elif self.exercise == "Push-up":
            shoulder = [landmarks[12].x, landmarks[12].y]
            elbow = [landmarks[14].x, landmarks[14].y]
            wrist = [landmarks[16].x, landmarks[16].y]
            angle = self.calculate_angle(shoulder, elbow, wrist)

            if angle > 160:
                self.stage = "up"
            if angle < 90 and self.stage == "up":
                self.stage = "down"
                self.count += 1

        elif self.exercise == "Bicep Curl":
            shoulder = [landmarks[12].x, landmarks[12].y]
            elbow = [landmarks[14].x, landmarks[14].y]
            wrist = [landmarks[16].x, landmarks[16].y]
            angle = self.calculate_angle(shoulder, elbow, wrist)

            if angle > 150:
                self.stage = "down"
            if angle < 60 and self.stage == "down":
                self.stage = "up"
                self.count += 1

        elif self.exercise == "Lunge":
            hip = [landmarks[24].x, landmarks[24].y]
            knee = [landmarks[26].x, landmarks[26].y]
            ankle = [landmarks[28].x, landmarks[28].y]
            angle = self.calculate_angle(hip, knee, ankle)

            if angle > 160:
                self.stage = "up"
            if angle < 90 and self.stage == "up":
                self.stage = "down"
                self.count += 1

        return self.count
