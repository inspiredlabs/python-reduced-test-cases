import numpy as np
import cv2
# 'uint8' assigns an 8bit unsigned integer to the colour values in the array
pic = np.zeros((512, 512, 3), dtype = 'uint8')
# Draw a rectangle from 0px to 512px

# Magenta colour, not color
colour = (255, 0, 255)

# Circles overview: https://www.khanacademy.org/math/basic-geo/basic-geo-area-and-perimeter/area-circumference-circle/a/radius-diameter-circumference
# Radius is "from the centre to any point on the circle itself"
# Diameter is "from any point on the circle through the centre itself all the way to the other side (which is 2x the radius!)"
# Circumference is "the distance of circle itself all the way around (diameter * 3.14159 or C/d = π)"


# Draws an unaliased circle with a diameter of 128px
cv2.circle(pic, (256, 256), 128, colour)

# Learn more: https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html

# Antialiasing should be straightforward: https://stackoverflow.com/questions/11055837/drawing-a-line-in-opencv-with-cv-aa-flags-is-not-producing-an-anti-aliased-line#25420463

cv2.imshow('Circle', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
