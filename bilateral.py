import cv2
import numpy

pic = cv2.imread(r'images/test_image.jpg')#test_image.jpg
dimpixel = 7
colour = 100
space = 100
filter = cv2.bilateralFilter(pic, dimpixel, colour, space)

#Apparently, this executes slower than Median
cv2.imshow('Bilateral Filter Sample', filter)
cv2.waitKey()
cv2.destroyAllWindows()
