import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(rr'cascades/haar.xml')

pic = cv2.imread(r'beckham.jpg') #arnie_30_30_200_2001.jpg
#scale_factor = 0.5
scale_factor = 1.3

while 1:
    faces = face_cascade.detectMultiScale(pic, scale_factor, 5)
    # https://stackoverflow.com/questions/30240372/how-to-force-detectmultiscale-search-on-11-scale

    for (x, y, w, h) in faces:
        cv2.rectangle(pic, (x,y), (x + w, y + h), (255, 0, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        white = 255, 255, 255
        cv2.putText(pic, 'Beckham', (x, y), font, 2, white, 2, cv2.LINE_AA)

    print("Faces: {} ".format(len(faces)))
    cv2.imshow('Beckhams face', pic)

    if cv2.waitKey(1) & 0xFF == ord('\x1b'):
        break

cv2.destroyAllWindows()
