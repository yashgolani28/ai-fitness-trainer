import cv2
from pose_detection import PoseDetector
from exercise_classifier import classify_exercise
from rep_counter import RepCounter
from feedback import give_feedback
from training_plan import generate_plan

cap = cv2.VideoCapture(0)
detector = PoseDetector()
rep_counter = None
exercise_name = "Unknown"

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    landmarks, frame = detector.get_landmarks(frame)
    if landmarks:
        exercise_name = classify_exercise(landmarks)

        if rep_counter is None and exercise_name != "Unknown":
            rep_counter = RepCounter(exercise_name)

        if rep_counter:
            reps = rep_counter.update(landmarks)
            feedback = give_feedback(landmarks, exercise_name)

            cv2.putText(frame, f'Exercise: {exercise_name}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, f'Reps: {reps}', (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            cv2.putText(frame, f'Feedback: {feedback}', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 100, 255), 2)

    cv2.imshow("AI Fitness Trainer", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

if rep_counter:
    print(generate_plan(rep_counter.count, exercise_name))