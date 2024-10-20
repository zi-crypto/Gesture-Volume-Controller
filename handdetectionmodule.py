import cv2
import mediapipe as mp
import time


class HandDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands, min_detection_confidence=self.detectionCon,
                                        min_tracking_confidence=self.trackCon)
        self.mpdraw = mp.solutions.drawing_utils
        
    def findhands(self, img, draw=True):
        imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgrgb)
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(img, handlms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findpositions(self, img, handno=0, draw=True):
        lms = []
        if self.results.multi_hand_landmarks:
            hand =  self.results.multi_hand_landmarks[handno]
            for id, lm in enumerate(hand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lms.append((id, cx, cy))
                if draw:
                    cv2.circle(img, (cx,cy), 15,(0,255,0), cv2.FILLED)
        return lms
                

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = HandDetector(maxHands=1)
    while True:
        success, img = cap.read()
        img = detector.findhands(img)
        lms = detector.findpositions(img)
        if len(lms) != 0:
            print(lms[4])
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv2.imshow('Image', img)
        cv2.waitKey(1)
    

if __name__ == "__main__":
    main()




