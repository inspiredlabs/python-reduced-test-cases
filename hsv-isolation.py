import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range in HSV
    lower_lime = np.array([30, 60, 60])
    upper_lime = np.array([100, 255, 255])
    # How to convert values: https://www.rapidtables.com/convert/color/rgb-to-hsv.html


    # Threshold the HSV image to get only lime:
    # Example: https://www.toysperiod.com/lego-set-reference/parts/bionicle/heads/bion009pb01_bionicle-head-connector-block-toa-inika-with-white-bottom/


    mask = cv2.inRange(hsv, lower_lime, upper_lime)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('HSV isolation', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
