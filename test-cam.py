#!/usr/bin/env python3

import cv2
import numpy as np
import time

cam = cv2.VideoCapture(0)

                                           # False = no pics for you to shoot at.

# Lets check start/open your cam!
if cam.read() == False:
    cam.open()

if not cam.isOpened():
    print('Cannot open camera')

while True:
    ret,frame = cam.read()
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
