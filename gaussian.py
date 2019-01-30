import cv2
import numpy

pic = cv2.imread(r'images/test_image.jpg')

matrix = (7,7)

blur = cv2.GaussianBlur(pic, matrix, 0)
cv2.imshow('Gaussian Blur Sample', blur)

cv2.waitKey()
cv2.destroyAllWindows()
