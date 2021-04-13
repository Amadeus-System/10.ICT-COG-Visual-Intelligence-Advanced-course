# https://copycoding.tistory.com/155
# contrast : The difference between light and dark areas in an image
import cv2

img0 = cv2.imread('cat.jpg')
# cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]]) → dst
# - return weighted sum of 2 image. gamma is bias
# - max = 120, min = 40 : range = 80 => max = 144, min = 48 : range = 96
img12 = cv2.addWeighted(img0, 1.2, img0, 0, 0)
img14 = cv2.addWeighted(img0, 1.4, img0, 0, 0)

cv2.imshow('img0', img0)
cv2.imshow('img12', img12)
cv2.imshow('img14', img14)
cv2.waitKey()