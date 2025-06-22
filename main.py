import cv2
from utils.hand_tracking import get_hand_landmarks
from utils.gesture_detection import detect_gesture
from gesture_controller import perform_action

cap = cv2.VideoCapture(0)

print("Starting Hand Gesture Controlled System... Press 'q' to quit.")

while True:
    success, frame = cap.read()
    if not success:
        print("Failed to grab frame")
        break

    # Flip for natural interaction
    frame = cv2.flip(frame, 1)

    # Get landmarks from Mediapipe
    landmarks, annotated_frame = get_hand_landmarks(frame)

    if landmarks:
        gesture = detect_gesture(landmarks)
        if gesture:
            print("Gesture Detected:", gesture)
            perform_action(gesture)

    cv2.imshow("Hand Gesture Controller", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
