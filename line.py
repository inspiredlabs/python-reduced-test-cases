import numpy as np
import cv2
# 'uint8' assigns an 8bit unsigned integer to the colour values in the array
pic = np.zeros((512, 512, 3), dtype = 'uint8')
# Draw a rectangle from 0px to 512px

cv2.line(pic, (350, 350), (512, 350), (0, 0, 255))
cv2.imshow('Red Line', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
