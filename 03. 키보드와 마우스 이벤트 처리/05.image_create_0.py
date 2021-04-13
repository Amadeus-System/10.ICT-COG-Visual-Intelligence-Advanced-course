# black image drawn and any key will destroy the image.
import cv2
import numpy as np

# array.shape = (height, width, channel)
img = np.zeros((480,640,3), dtype=np.uint8)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()