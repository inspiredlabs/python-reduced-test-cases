import cv2
import numpy

pic = cv2.imread(r'images/beckham.jpg')#test_image.jpg


matrix = 111 # Assertion failed >99 on low_res.jpg

matrix = 333 # Assertion failed >~333 on beckham.jpg

median = cv2.medianBlur(pic, matrix)

cv2.imshow('Median Blur Sample', pic)

cv2.waitKey()
cv2.destroyAllWindows()
