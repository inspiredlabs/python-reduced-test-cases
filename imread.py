import numpy as np
import cv2

img = cv2.imread(r'images/test_image.jpg', 0)#0 is greyscale.
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
