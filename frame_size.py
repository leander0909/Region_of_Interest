import cv2
import numpy as np

cap = cv2.VideoCapture('walking_vid3.mp4')
ret, frame = cap.read()

hs,ws, cs = frame.shape
print(hs,ws,cs)