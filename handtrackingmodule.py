from sre_constants import SUCCESS
import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self,mode = False, maxHands=2, model_complexity = 1, detectionConfidence = 0.5, trackConfidence = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence
        self.model_complexity = model_complexity

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.model_complexity,
                                        self.detectionConfidence, self.trackConfidence)
        
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    
    def findPosition(self, img, handID = 0, draw = True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            h = self.results.multi_hand_landmarks[handID]
            for id, lm in enumerate(h.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmlist.append([id, cx, cy])
                
        return lmlist
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmlist = detector.findPosition(img)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        if len(lmlist) != 0:
            print(lmlist[4])
            ll = lmlist[4]
            ox, oy = ll[1], ll[2]
            cv2.circle(img, (int(ox), int(oy)), 15, (255,255,255), 1)
        
        cv2.putText(img, str(int(fps)), (10,100), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),1)
        cv2.imshow('Image', img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
