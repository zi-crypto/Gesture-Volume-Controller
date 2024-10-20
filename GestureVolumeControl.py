from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import cv2
import mediapipe as mp
import time
import handdetectionmodule as hdm
import numpy as np
import math
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
key = " "


# Max:270, Min:30
pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
#cap.set(3, 640)
#cap.set(4, 480)
detector = hdm.HandDetector(detectionCon=0.9, maxHands=1)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()

minvol = volRange[0]
maxvol = volRange[1]
volbar = np.interp(volume.GetMasterVolumeLevel(), [minvol, maxvol], [400, 150])
while True:
    success, img = cap.read()
    img = detector.findhands(img)
    lms = detector.findpositions(img,draw=False)
    if len(lms) != 0:
        x1, y1 = lms[4][1], lms[4][2]
        x2, y2 = lms[8][1], lms[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2
        
        #cv2.circle(img, (x1,y1), 5, (255,0,0), cv2.FILLED)
        #cv2.circle(img, (x2,y2), 5, (255,0,0), cv2.FILLED)
        #cv2.circle(img, (cx,cy), 15, (0,0,255), cv2.FILLED) 
        length = int(math.hypot(x2-x1,y2-y1))
        
        #cv2.line(img, (x1, y1), (x2,y2), (0,0,225), 3)

        x3, y3 = lms[12][1], lms[12][2]        
        #cv2.circle(img, (x3,y3), 5, (255,255,255), cv2.FILLED)
        length2 = int(math.hypot(x3-x1,y3-y1))

        x4, y4 = lms[19][1], lms[19][2]        
        #cv2.circle(img, (x4,y4), 5, (255,255,255), cv2.FILLED)
        length3 = int(math.hypot(x4-x1,y4-y1))

        x5, y5 = lms[15][1], lms[15][2]        
        #cv2.circle(img, (x5,y5), 5, (255,255,255), cv2.FILLED)
        length4 = int(math.hypot(x5-x1,y5-y1))

        x6, y6 = lms[20][1], lms[20][2]        
        #cv2.circle(img, (x6,y6), 5, (255,255,255), cv2.FILLED)
        length5 = int(math.hypot(x6-x1,y6-y1))

        

        if length2 <= 35:
            keyboard.press(key)
            keyboard.release(key)
            time.sleep(.5)

        if length3 <= 35:
            keyboard.press(Key.left)
            keyboard.release(Key.left)
            time.sleep(.5)

        if length4 <= 35:
            keyboard.press(Key.right)
            keyboard.release(Key.right)
            time.sleep(.5)

        #if length5 <= 25:
        #    with keyboard.pressed(Key.shift):
        #        keyboard.press('n')
        #    time.sleep(.5)
        
        vol = np.interp(length, [30, 150], [minvol, maxvol])
        volbar = np.interp(length, [30, 150], [400, 150])
        volume.SetMasterVolumeLevel(vol, None) 

        #if  vol < -53:
        #    cv2.circle(img, (cx,cy), 15, (100,100,100), cv2.FILLED)
        #    cv2.line(img, (x1, y1), (x2,y2), (100,100,100), 3)
        #elif vol > -53 and vol < -10:
        #    cv2.circle(img, (cx,cy), 15, (0,255,0), cv2.FILLED)
        #    cv2.line(img, (x1, y1), (x2,y2), (0,255,0), 3)
        #elif vol > -10 and vol < 0:
        #    cv2.circle(img, (cx,cy), 15, (0,0,255), cv2.FILLED)
        #    cv2.line(img, (x1, y1), (x2,y2), (0,0,255), 3)
            
    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
    cv2.rectangle(img, (50, int(volbar)), (85, 400), (0, 255, 0), cv2.FILLED)
            

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, 'FPS: {}'.format(str(int(fps))), (40,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    cv2.imshow('Volume', img)
    cv2.waitKey(1)
    

if __name__ == "__main__":
    main()




