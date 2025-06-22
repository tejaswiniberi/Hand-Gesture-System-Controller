def detect_gesture(landmarks):
    if not landmarks or len(landmarks) < 21:
        return None

    def finger_up(tip, pip):
        return landmarks[tip][1] < landmarks[pip][1]

    fingers = [
        finger_up(8, 6),    # Index
        finger_up(12, 10),  # Middle
        finger_up(16, 14),  # Ring
        finger_up(20, 18)   # Pinky
    ]

    thumb_up = landmarks[4][1] < landmarks[3][1] and landmarks[4][0] > landmarks[3][0]
    index_up = fingers[0]
    middle_up = fingers[1]
    ring_up = fingers[2]
    pinky_up = fingers[3]

    # Pinch detection
    pinch_distance = ((landmarks[4][0] - landmarks[8][0]) ** 2 + (landmarks[4][1] - landmarks[8][1]) ** 2) ** 0.5
    is_pinching = pinch_distance < 0.03

    # Wave detection (large X movement)
    x_coords = [lm[0] for lm in landmarks]
    x_movement = max(x_coords) - min(x_coords)
    is_waving = x_movement > 0.2

    # === GESTURE RULES ===

    if is_waving:
        return "exit_app"

    if is_pinching:
        return "mouse_control"

    if thumb_up and not any([index_up, middle_up, ring_up, pinky_up]):
        return "screenshot"

    if thumb_up and pinky_up and not any([index_up, middle_up, ring_up]):
        return "open_browser"

    if all([thumb_up, index_up, middle_up, ring_up, pinky_up]):
        return "play_pause"

    if index_up and not any([middle_up, ring_up, pinky_up, thumb_up]):
        return "volume_up"

    if index_up and middle_up and not any([ring_up, pinky_up, thumb_up]):
        return "volume_down"

    return None
