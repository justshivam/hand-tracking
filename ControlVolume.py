from HandTrackingModule import handDetector as hd
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import cv2
import math


cap = cv2.VideoCapture(0)
detector = hd()
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
while True:
    success, img = cap.read()
    img = detector.findHands(img,)
    landmarks = detector.findPosition(img, draw=False)
    if len(landmarks) != 0:
        point1 = landmarks[4]
        point2 = landmarks[8]
        xCom = (point1[2]-point2[2])**2
        yCom = (point1[1]-point2[1]) ** 2
        distance = math.sqrt(xCom + yCom) - 10
        distance = max(distance, 0)
        distance = min(distance, 90)
        distance = int(distance)
        print(distance)
        volume.SetMasterVolumeLevel(distance-90, None)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
