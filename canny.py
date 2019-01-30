import cv2
import numpy

#pic = cv2.imread(r'images/beckham.jpg')#requires fit-to-window
#pic = cv2.imread(r'images/dice_small.jpg')#dice_large.jpg
pic = cv2.imread(r'images/usa_plates02.jpg')

threshold1 = 50
threshold2 = 100

filter = cv2.Canny(pic, threshold2, threshold2)
#Canny uses apertureSize=3 by default: https://docs.opencv.org/3.2.0/dd/d1a/group__imgproc__feature.html

cv2.imshow('Canny Edge Sample', filter)

cv2.waitKey()
cv2.destroyAllWindows()
