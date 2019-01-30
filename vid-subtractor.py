import cv2
import numpy

cap = cv2.VideoCapture('lanes_cap00.mp4')

fgbg = cv2.createBackgroundSubtractorMOG2()

while(cap.isOpened()):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('Video Capture', fgmask)
    if cv2.waitKey(1) & 0xFF == ord('\x1b'):
        break

cap.release()
cv2.destroyAllWindows()
