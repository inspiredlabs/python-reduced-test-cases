import cv2
import numpy

pic = cv2.imread(r'images/test_image.jpg',0)

threshold_value = 100

(T_value,binary_threshold) = cv2.threshold(pic, threshold_value,255,cv2.THRESH_BINARY_INV)#cv2.THRESH_BINARY

cv2.imshow('binary', binary_threshold)
cv2.waitKey()
cv2.destroyAllWindows()
