# -*- coding: utf-8 -*-
# split each channels using cv2.split

import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

# img.shape = (h, w, c=3)
# split(img) return (h,w), (h,w), (h,w)
b, g, r = cv2.split(img)
# b, g, r = img[:,:,0], img[:,:,1], img[:,:,2]

cv2.imshow('original', img)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)
cv2.waitKey()
cv2.destroyAllWindows()

img_rgb = cv2.merge((r,g,b))  # wrong example
img_bgr = cv2.merge((b,g,r))
cv2.imshow('reversed', img_rgb)
cv2.imshow('original', img_bgr)
cv2.waitKey()
cv2.destroyAllWindows()

# [Quiz] cat 컬러이미지와 회색만 있는 이미지의 평균 이미지를 생성하자.
# - 회색 = (127, 127, 127)