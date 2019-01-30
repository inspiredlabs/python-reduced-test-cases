import cv2
import numpy

# In this canny sample we return license plates...
# canny-gaussian-prefilter.py returns nicer letters,
# but with diminished corners.
pic = cv2.imread(r'images/usa_plates02.jpg')#usa_plates01.jpg


# RTFM: https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html#gaussianblur
kernel = (21,17) # Gaussian kernels *must* be odd
stdev = 3 # 0.1 introduces much detail
blur = cv2.GaussianBlur(pic, kernel, stdev)
# Returning an image called blur, convolving low-probability high-amplitude noise from the image.

# Aggressivly reduce noise
# Output GaussianBlur to screen:
#cv2.imshow('Gaussian Blur Sample', blur)

threshold1 = 50
threshold2 = 100

filter = cv2.Canny(blur, threshold2, threshold2)
#Canny uses apertureSize=3 by default: https://docs.opencv.org/3.2.0/dd/d1a/group__imgproc__feature.html
cv2.imshow('Canny Edge Sample', filter)
cv2.waitKey()
cv2.destroyAllWindows()
