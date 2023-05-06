import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

cv2.imshow("Frame", frame)
cv2.waitKey(0)