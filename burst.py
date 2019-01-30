import numpy as np
import cv2

a = np.zeros((256,256), dtype=np.uint8)
for u in np.exp(np.linspace(0,1j*2*np.pi,25)):
    cv2.line(a, (100, 100), (int(100+100*u.real+.5), int(100+100*u.imag+.5)), 255, 2)
cv2.imwrite('burst.png', a)
cv2.waitKey(0)
cv2.destroyAllWindows()
# PID appears to hang: https://stackoverflow.com/questions/24682797/python-opencv-drawing-line-width#24687564 
