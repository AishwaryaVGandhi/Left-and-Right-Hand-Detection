import cv2
from cvzone import HandTrackingModule

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandTrackingModule.HandDetector()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img, flipType=False)

    cv2.imshow("Hand Detection", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
