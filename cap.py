import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    cv2.imshow(r'cap.release() # required', frame)

    if cv2.waitKey(1) & 0xFF == ord('\x1b'):
        break

cap.release() # required
cv2.destroyAllWindows()
