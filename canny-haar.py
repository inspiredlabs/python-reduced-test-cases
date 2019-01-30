import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(rr'cascades/haar.xml')

vidCap = cv2.VideoCapture(0)
scale_factor = 1.1

while 1:
    ret, frame = vidCap.read()

    # blurRad = 11
    # matrix = (blurRad)
    # blur = cv2.medianBlur(frame, matrix)

    blur = cv2.blur(frame, (6,6))
    # from: https://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html

    faces = face_cascade.detectMultiScale(blur, scale_factor, 5)

    for (x, y, w, h) in faces:
        font = cv2.FONT_HERSHEY_SIMPLEX
        hint = 0, 0, 255
        cv2.rectangle(blur, (x,y), (x + w, y + h), hint, 2)
        cv2.putText(blur, 'Viso:', (x, y), font, 2, hint, 2, cv2.LINE_8)#Canny, HAAR Capture

    print("Faces: {} ".format(len(faces)))
    cv2.imshow('Capture', blur)
    if cv2.waitKey(1) & 0xFF == ord('\x1b'):
        break

cv2.destroyAllWindows()
