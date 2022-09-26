from handDetector import HandDetector
import cv2
import math
import serial
import time
import numpy as np


handDetector = HandDetector(min_detection_confidence=0.7, max_num_hands=33)
webcamFeed = cv2.VideoCapture(0)

dev="0"
time.sleep(2)
while True:
    status, image = webcamFeed.read()
    handLandmarks = handDetector.findHandLandMarks(image=image, draw=True)
    count=0;
    cad="lol"

    if(len(handLandmarks) != 0):
        #we will get y coordinate of finger-tip and check if it lies above middle landmark of that finger
        #details: https://google.github.io/mediapipe/solutions/hands

        if handLandmarks[4][3] == "Right" and handLandmarks[4][1] > handLandmarks[3][1]:       #Right Thumb
            #dev.write(b'J')
            print('P')
        else:
            if handLandmarks[4][3] == "Right" and handLandmarks[4][1] < handLandmarks[3][1]:
                #dev.write(b'I')
                print("N")

        if handLandmarks[8][2] < handLandmarks[6][2]:       #Index finger
            #dev.write(b'H')
            print('P')
        else:
            if handLandmarks[8][2] > handLandmarks[6][2]:
                #dev.write(b'G')
                print("N")

        if handLandmarks[12][2] < handLandmarks[10][2]:     #Middle finger
            #dev.write(b'E')
            print('P')
        else:
            if handLandmarks[12][2] > handLandmarks[10][2]:
                #dev.write(b'F')
                print("N")
        if handLandmarks[16][2] < handLandmarks[14][2]:     #Ring finger
            #dev.write(b'D')
            print('P')
        else:
            if handLandmarks[16][2] > handLandmarks[14][2]:
                #dev.write(b'C')
                print("N")
        if handLandmarks[20][2] < handLandmarks[18][2]:     #Little finger
            #dev.write(b'B')
            print('P')
        else:
            if handLandmarks[20][2] > handLandmarks[18][2]:
                #dev.write(b'A')
                print("N")

    cv2.putText(image, str("Hola "), (700, 100), cv2.FONT_HERSHEY_PLAIN , 6, (0, 0, 0), 10)

    cv2.imshow("Volume", image)
    cv2.waitKey(1)