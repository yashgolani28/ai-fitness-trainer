    def update(self, landmarks):
        if self.exercise == "Squat":
            # same as before
            ...

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
