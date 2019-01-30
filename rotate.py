#https://www.udemy.com/pythoncv/learn/v4/t/lecture/5562732?start=0
import numpy as np
import cv2

pic = cv2.imread(r'images/beckham.jpg')
cols = pic.shape[1]
rows = pic.shape[0]
centre =(cols/2,rows/2)
angle = 90

M = cv2.getRotationMatrix2D(centre, angle, 1)
rotate = cv2.warpAffine(pic, M, (cols, rows))
cv2.imshow('rotated', rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()
