# Canny edge detector with a trackbar
# - thresh1, thresh2의 순서가 없다. 큰 것이 how, 낮은 것이 low threshold

import cv2 as cv
import numpy as np


def onChangeThresh1(val):
	global thresh1, thresh2
	thresh1 = val
	print('thresh1, thresh2 =', thresh1, thresh2)
	edge = cv.Canny(img, thresh1, thresh2)
	cv.imshow('edge', edge)


def onChangeThresh2(val):
	global thresh1, thresh2
	thresh2 = val
	print('thresh1, thresh2 =', thresh1, thresh2)
	edge = cv.Canny(img, thresh1, thresh2)
	cv.imshow('edge', edge)


img = cv.imread('image/edge_test1.jpg', cv.IMREAD_COLOR)

thresh1 = 50
thresh2 = 120
cv.namedWindow('edge')
cv.createTrackbar('thresh1', 'edge', thresh1, 255, onChangeThresh1)
cv.createTrackbar('thresh2', 'edge', thresh2, 255, onChangeThresh2)

edge = cv.Canny(img, thresh1, thresh2)

cv.imshow('img', img)
cv.imshow('edge', edge)
cv.waitKey()

# [Quiz] GaussianBlurr를 적용한 이후, Canny를 사용한다.
# - 이때 커널 사이즈는 (0, 0)하고, sx=1을 디폴트로하고,
# - 이값을 0.1 ~ 2까지 변화시키는 트랙바를 추가하라.