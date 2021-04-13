# or xor not !mask
import cv2
import numpy as np

img1 = np.zeros((300,300), np.uint8)
img2 = np.zeros((300,300), np.uint8)
mask = np.zeros((300,300), np.uint8)
# mask = np.full_like(img1, 128+32+8+2, np.uint8)

cv2.circle(img1, (150,150), 100, 255, -1)
cv2.rectangle(img2, (0,0), (150,300), 255, -1)
cv2.rectangle(mask, (0,0), (300, 150), 255, -1)

# img1_or_img2 = np.zeros((300, 300), np.uint8)
# cv2.bitwise_or(img1, img2, dst=img1_or_img2)
img1_or_img2 = cv2.bitwise_or(img1, img2)
img1_or_img2_with_mask = cv2.bitwise_or(img1, img2, mask=mask)

img1_xor_img2 = cv2.bitwise_xor(img1, img2)
img1_xor_img2_with_mask = cv2.bitwise_xor(img1, img2, mask=mask)

img1_not = cv2.bitwise_not(img1)
img1_not_with_mask = cv2.bitwise_not(img1, mask=mask)
img2_not = cv2.bitwise_not(img2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('mask', mask)
cv2.imshow('img_or', img1_or_img2)
cv2.imshow('img_or_mask', img1_or_img2_with_mask)
cv2.imshow('img_xor', img1_xor_img2)
cv2.imshow('img_xor_mask', img1_xor_img2_with_mask)
cv2.imshow("img1 not", img1_not)
cv2.imshow("img1 not with mask", img1_not_with_mask)
cv2.imshow("img2 not", img2_not)

cv2.waitKey()
cv2.destroyAllWindows()
