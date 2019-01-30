import numpy as np
import cv2

# 'uint8' assigns an 8bit unsigned integer to the colour values in the array
pic = np.zeros((512, 512, 3), dtype = 'uint8')
# Draw a rectangle from 0px to 512px

# Change rendering font:
#   codeyarns.com/2015/03/11/fonts-in-opencv
font = cv2.FONT_HERSHEY_DUPLEX

# Check functional namespacing
white = (255, 255, 255)

# Simple, intuitive co-ordinates:
x = 0
y = 111

cv2.putText(pic, 'OpenCV2 3.4.2',(x, y), font, 2, white, 4, cv2.LINE_8) #LINE_AA for px alias

# Version: OpenCV2 3.4.2
cv2.imshow('OpenCV2 3.4.2', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
