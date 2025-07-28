import mediapipe as mp

POSE_LANDMARKS = mp.solutions.pose.PoseLandmark

def map_pose_to_symbolic_event(landmarks) -> str:
    # Get landmark coordinates
    left_wrist = landmarks.landmark[POSE_LANDMARKS.LEFT_WRIST]
    right_wrist = landmarks.landmark[POSE_LANDMARKS.RIGHT_WRIST]
    left_shoulder = landmarks.landmark[POSE_LANDMARKS.LEFT_SHOULDER]
    right_shoulder = landmarks.landmark[POSE_LANDMARKS.RIGHT_SHOULDER]

    # Heuristic 1: both arms raised above shoulders
    if (
        left_wrist.y < left_shoulder.y and
        right_wrist.y < right_shoulder.y
    ):
        return "CAST_SPELL"

    # Heuristic 2: arms crossed (wrists near opposite shoulders)
    dist_left = abs(left_wrist.x - right_shoulder.x)
    dist_right = abs(right_wrist.x - left_shoulder.x)

    if dist_left < 0.1 and dist_right < 0.1:
        return "DEFENSIVE_STANCE"

    return "NEUTRAL"
