import numpy as np
import cv2
# 'uint8' assigns an 8bit unsigned integer to the colour values in the array
pic = np.zeros((512, 512, 3), dtype = 'uint8')
# Draw a rectangle from 0px to 512px
# Is this in RGB or BGR?
# https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_matplotlib_rgb_brg_image_load_display_save.php
# https://duckduckgo.com/?q=red%3A98+green%3A200+blue%3A123&t=ffab&ia=answer

cv2.rectangle(pic, (0, 0), (512, 150), (123, 200, 98), 3, lineType=8, shift=1)
cv2.imshow('Dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
