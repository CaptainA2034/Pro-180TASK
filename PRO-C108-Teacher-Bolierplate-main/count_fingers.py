import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_dectection_confidence = 0.8,min_tracking_confidence = 0.5)
def drawHandLandMarks(image,hand_landMarks):
    if hand_landMarks:
        for landmarks in hand_landMarks:
            mp_drawing.draw_landMarks(image,landmarks,mp_hands.HAND_CONNETIONS)

while True:
    success, image = cap.read()
    image = cv2.flip(image,1)
    results = hands.process(image)
    hand_landMarks = results.multi_hand_landMarks
    drawHandLandMarks(image,hand_landMarks)

    cv2.imshow("Media Controller", image)

    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()