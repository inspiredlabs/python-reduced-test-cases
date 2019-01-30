#https://www.udemy.com/pythoncv/learn/v4/t/lecture/5563978?start=0
import numpy as np
import cv2

pic = cv2.imread(r'images/beckham.jpg')
cols = pic.shape[1]
rows = pic.shape[0]

M = np.float32([[1, 0, 150], [0, 1, 70]])

shifted = cv2.warpAffine(pic, M, (cols, rows))
cv2.imshow('shifted', shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
