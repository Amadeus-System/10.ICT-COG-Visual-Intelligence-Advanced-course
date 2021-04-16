import cv2
import numpy as np

s = 400

# img = np.zeros((s,s), dtype=np.uint8)  # generate underflow
img = np.zeros((s,s))
cv2.circle(img, (200,200), 200, 255, -1)

img[:200, 200:] = np.abs(img[:200, 200:] - 255)
img[200:, :200] = np.abs(img[200:, :200] - 255)

img = img.astype(np.uint8)

cv2.imshow('img', img)
cv2.waitKey()