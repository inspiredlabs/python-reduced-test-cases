import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(r'cascades/haar.xml')

vidCap = cv2.VideoCapture(0)
scale_factor = 1.1

fgbg = cv2.createBackgroundSubtractorMOG2()

while 1:
    ret, pic = vidCap.read()
    bgMask = fgbg.apply(pic)

    # blurRad = 11
    # matrix = (blurRad)
    # blur = cv2.medianBlur(pic, matrix)

    #blur = cv2.blur(pic, (16,16))

    faces = face_cascade.detectMultiScale(bgMask, scale_factor, 5)

    for (x, y, w, h) in faces:
        font = cv2.FONT_HERSHEY_SIMPLEX
        hint = 0, 0, 255
        cv2.rectangle(bgMask, (x,y), (x + w, y + h), hint, 2)
        cv2.putText(bgMask, 'Viso:', (x, y), font, 2, hint, 2, cv2.LINE_8)#Canny, HAAR Capture

    print("Faces: {} ".format(len(faces)))
    cv2.imshow('Capture', bgMask)
    if cv2.waitKey(1) & 0xFF == ord('\x1b'):
        break

cv2.destroyAllWindows()
