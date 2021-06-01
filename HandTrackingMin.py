import mediapipe as mp
import cv2
import time

camera_index = 0
cap = cv2.VideoCapture(camera_index)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cTime = 0
pTime = 0


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    if result.multi_hand_landmarks:
        for handLandmark in result.multi_hand_landmarks:
            for id, lm in enumerate(handLandmark.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                # print(id, cx, cy)
                if id == 0:
                    color = (255, 255, 255)
                    size = 20
                    cv2.circle(img, (cx, cy), size, color, cv2.FILLED)

            mpDraw.draw_landmarks(img, handLandmark, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    text_to_print = str(int(fps))
    value_range = (10, 70)
    font = cv2.FONT_HERSHEY_COMPLEX
    scale = 3
    color = (0, 0, 0)
    thickness = 3
    cv2.putText(img, text_to_print, value_range, font, scale, color, thickness)

    window_title = "Test Window"
    cv2.imshow(window_title, img)
    cv2.waitKey(1)
