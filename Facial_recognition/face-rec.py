import cv2
import mediapipe as mp
import numpy as np

mp_face_detection = mp.solutions.face_detection
mp_hand_detection = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

known_face_encodings = []
known_face_names = []

def compute_face_encoding(face_image):
    return np.random.rand(128)

def load_and_encode_known_faces():
    image1 = cv2.imread("C:/Users/Diwakar/OneDrive - MSFT/Pictures/jeemain p1 - Copy.jpg")
    encoding1 = compute_face_encoding(image1)
    known_face_encodings.append(encoding1)
    known_face_names.append("Person 1")

    image2 = cv2.imread("C:/Users/Diwakar/OneDrive - MSFT/Pictures/IMG_7592.JPG")
    encoding2 = compute_face_encoding(image2)
    known_face_encodings.append(encoding2)
    known_face_names.append("Person 2")

load_and_encode_known_faces()

video_capture = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection, \
     mp_hand_detection.Hands(min_detection_confidence=0.5) as hand_detection:
    
    while True:
        ret, frame = video_capture.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        face_results = face_detection.process(rgb_frame)

        face_names = []
        if face_results.detections:
            for detection in face_results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                x, y, w, h = (int(bboxC.xmin * iw), int(bboxC.ymin * ih),
                              int(bboxC.width * iw), int(bboxC.height * ih))
                
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                face_image = rgb_frame[y:y+h, x:x+w]
                face_encoding = compute_face_encoding(face_image)

                matches = [np.linalg.norm(face_encoding - known_encoding) < 0.6 for known_encoding in known_face_encodings]
                name = "Face"
                if any(matches):
                    best_match_index = np.argmin([np.linalg.norm(face_encoding - known_encoding) for known_encoding in known_face_encodings])
                    name = known_face_names[best_match_index]

                face_names.append(name)
                cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

        hand_results = hand_detection.process(rgb_frame)
        if hand_results.multi_hand_landmarks:
            for hand_landmarks in hand_results.multi_hand_landmarks:
                x_min = int(min([landmark.x for landmark in hand_landmarks.landmark]) * iw)
                y_min = int(min([landmark.y for landmark in hand_landmarks.landmark]) * ih)
                x_max = int(max([landmark.x for landmark in hand_landmarks.landmark]) * iw)
                y_max = int(max([landmark.y for landmark in hand_landmarks.landmark]) * ih)

                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)
                cv2.putText(frame, "Hand", (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video_capture.release()
cv2.destroyAllWindows()
