import cv2
import numpy

pic = cv2.imread(r'images/dice_small.jpg')#dice_large.jpg

blurRad = 15
matrix = (blurRad,blurRad)
blur = cv2.GaussianBlur(pic, matrix, 0)
# Output GaussianBlur to screen:
#cv2.imshow('Gaussian Blur Sample', blur)

threshold1 = 44
#threshold2 = threshold1 * 3
threshold2 = 132

filter = cv2.Canny(blur, threshold2, threshold2)
#Canny uses apertureSize=3 by default: https://docs.opencv.org/3.2.0/dd/d1a/group__imgproc__feature.html
cv2.imshow('Canny Edge Sample', filter)

cv2.waitKey()
cv2.destroyAllWindows()
