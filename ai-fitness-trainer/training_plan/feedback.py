def give_feedback(landmarks, exercise):
    if exercise == "Squat":
        hip = landmarks[24].y
        knee = landmarks[26].y
        return "Good Form" if hip > knee else "Go lower for full range"

    elif exercise == "Push-up":
        shoulder_y = landmarks[12].y
        elbow_y = landmarks[14].y
        return "Lower your chest" if shoulder_y < elbow_y else "Good Push"

    elif exercise == "Bicep Curl":
        wrist = landmarks[16].y
        elbow = landmarks[14].y
        return "Good Curl" if wrist < elbow else "Lift higher"

    elif exercise == "Lunge":
        left_knee = landmarks[25].y
        right_knee = landmarks[26].y
        return "Keep balance" if abs(left_knee - right_knee) < 0.2 else "Step deeper"

    return "Hold your form"
