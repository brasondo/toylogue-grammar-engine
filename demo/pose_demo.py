import cv2
from pose.detector import detect_pose_frame
from pose.mapper import map_pose_to_symbolic_event
import mediapipe as mp
print(dir(mp.solutions))


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    landmarks = detect_pose_frame(frame)
    if landmarks:
        event = map_pose_to_symbolic_event(landmarks)
        print(f"[POSE EVENT]: {event}")

    cv2.imshow("Pose Demo", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
