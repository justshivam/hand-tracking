from HandTrackingModule import handDetector as hd
import cv2


def countFingersInHand(img, hand):
    x = 0
    tips = [20, 16, 12, 8]
    anchors = [19, 15, 11, 7]
    for i in range(4):
        if hand[tips[i]][2] <= hand[anchors[i]][2] and hand[tips[i]][2] <= hand[anchors[i]+1][2]:
            x += 1
    # print(hand[tips[0]], hand[anchors[0]])
    if hand[17][1] < hand[4][1]:
        if hand[4][1] >= hand[5][1]:
            x += 1
    else:
        if hand[4][1] <= hand[5][1]:
            x += 1
    return x


cap = cv2.VideoCapture(0)
detector = hd()
while True:
    success, img = cap.read()
    img = detector.findHands(img,)
    handcount = detector.numberOfHands()
    if handcount == 0:
        cv2.putText(img, "No Hands Detected", (10, 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
    else:
        count = 0
        for i in range(detector.numberOfHands()):
            lmList = detector.findPosition(img, draw=False, handNo=i)
            count += countFingersInHand(img, lmList)
        cv2.putText(img, str(count), (10, 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
    # if len(lmList) != 0:
    #     print(lmList[4])

    # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
    #             (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
