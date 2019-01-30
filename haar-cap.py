import cv2
import numpy as np
# HAAR https://github.com/Itseez/opencv/treemaster/data/haarcascades
# haarcascade_frontalface_default.xml

face_cascade = cv2.CascadeClassifier(r'cascades/haar.xml')

vidCap = cv2.VideoCapture(0)
scale_factor = 1.1

while 1:
    ret, pic = vidCap.read()
    faces = face_cascade.detectMultiScale(pic, scale_factor, 5)
    # https://stackoverflow.com/questions/30240372/how-to-force-detectmultiscale-search-on-11-scale

    for (x, y, w, h) in faces:
        cv2.rectangle(pic, (x,y), (x + w, y + h), (255, 0, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        white = 255, 255, 255
        cv2.putText(pic, 'Capture', (x, y), font, 2, white, 2, cv2.LINE_AA)

    print("Faces: {} ".format(len(faces)))
    cv2.imshow('Capture', pic)

    if cv2.waitKey(1) & 0xFF == ord('\x1b'):
        break

vidCap.release() # required for: cv2.VideoCapture
cv2.destroyAllWindows()
