import cv2
import numpy as np

img1 = np.zeros((300,300), np.uint8)
img2 = np.zeros((300,300), np.uint8)
mask = np.zeros((300,300), np.uint8)

# display white circle into img1: center (150,150), radius 100.
# - circle(img, center(x, y), radius, color, line-thickness)
cv2.circle(img1, (150,150), 100, 255, -1)
# display white rectangular into img2 left-side
# - cv2.rectangle(img, start(x1, y1), end(x2, y2), color, thickness)
cv2.rectangle(img2, (0,0), (150,300), 255, -1)
# display white rectangular into mask up-side
cv2.rectangle(mask, (0,0), (300,150), 255, -1)

# bit-wise boolean production with img1 and img2
img1_and_img2 = cv2.bitwise_and(img1, img2)
#img1_and_img2 = np.zeros((300,300), dtype=np.uint8)
#cv2.bitwise_and(img1, img2, dst=img1_and_img2)

# is operated in masked region(up-side mask)
img1_and_img2_with_mask = cv2.bitwise_and(img1, img2, mask=mask)
# img1_and_img2_with_mask = cv2.bitwise_and(img1_and_img2, mask)

# img1_and_img2_with_mask = np.zeros_like(img1, dtype=np.uint8)
# cv2.bitwise_and(img1, img2, dst=img1_and_img2_with_mask, mask=mask)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('mask', mask)
cv2.imshow('img1_and_img2', img1_and_img2)
cv2.imshow('img1_and_img2_with_mask', img1_and_img2_with_mask)
cv2.waitKey()
cv2.destroyAllWindows()
