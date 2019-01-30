import cv2
import numpy


# matrix = (21,21)
# blur = cv2.GaussianBlur(pic, matrix, 0)
# # Output GaussianBlur to screen:
# #cv2.imshow('Gaussian Blur Sample', blur)

#lanes_cap00.mp4 = test2.mp4 from github: URI
#lanes_cap01.mp4 = skully-fenix.pm4
#lanes_cap02.mp4 = 2019 CanAm Ryker Rally Edition _ First Ride.pm4

cap = cv2.VideoCapture('lanes_cap00.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    blurRad = 11
    #matrix = (blurRad,blurRad)
    #blur = cv2.GaussianBlur(frame, matrix, 0)

    matrix = (blurRad)
    blur = cv2.medianBlur(frame, matrix)


    threshold1 = 50
    threshold2 = 100
    filter = cv2.Canny(blur, threshold2, threshold2)

    cv2.imshow('Canny Edge Video Sample', filter)
    if cv2.waitKey(1) & 0xFF == ord('\x1b'):
        break
        # ord('q') is inssufficient: https://stackoverflow.com/questions/14494101/using-other-keys-for-the-waitkey-function-of-opencv#14494131

cap.release()
cv2.destroyAllWindows()
