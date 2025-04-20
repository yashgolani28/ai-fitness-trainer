def classify_exercise(landmarks):
    if not landmarks:
        return "Unknown"

    left_knee = landmarks[25]
    right_knee = landmarks[26]
    left_elbow = landmarks[13]
    right_elbow = landmarks[14]
    left_shoulder = landmarks[11]
    right_shoulder = landmarks[12]

    # Squat
    hip = landmarks[23]
    knee_height = (left_knee.y + right_knee.y) / 2
    hip_height = hip.y
    if abs(hip_height - knee_height) < 0.1:
        return "Squat"

    # Push-up: elbows close to shoulders and body horizontal
    if abs(left_elbow.y - left_shoulder.y) < 0.05 and abs(right_elbow.y - right_shoulder.y) < 0.05:
        return "Push-up"

    # Bicep curl: elbow below shoulder, wrist moves up/down
    if abs(left_elbow.y - right_elbow.y) < 0.1 and abs(left_elbow.x - right_elbow.x) > 0.2:
        return "Bicep Curl"

    # Lunge: one knee lower than the other
    if abs(left_knee.y - right_knee.y) > 0.2:
        return "Lunge"

    return "Unknown"
