# blur gray image
# - 블러링은 거친 느낌의 입력 영상을 부드럽게 만드는 용도로 사용되기도 하고,
# - 혹은 입력 영상에 존재하는 잡음의 영향을 제거하는 전처리 과정으로도 사용됨

import cv2 as cv
import numpy as np


def filter_gray(img, kernel):
	# 9, 9
	kh, kw = kernel.shape[0:2]
	# 9//2 -> 4
	kh2, kw2 = kh//2, kw//2

	# if img.shape = 10, 10
	tmp_shape = list(img.shape)
	tmp_shape[0] += (kh2*2)
	tmp_shape[1] += (kw2*2)
	# tmp shape [10, 10] + 4*2 -> [18, 18]

	# 18, 18 -> 0 으로 초기화
	tmp = np.zeros(tmp_shape, img.dtype)

	# kh2 = 4, img.shape = 10
	# kh2:kh2+img.shape[0] == 4:4+10, kw2:kw2+img.shape[1] == 4:4+10
	# - tmp: padded img with 4 edge pixels with zero values.
	np.copyto(tmp[kh2:kh2+img.shape[0], kw2:kw2+img.shape[1]], img)
	# tmp[kh2:-kh2, kw2:-kw2] = img.copy()

	# convolution return value's shape is 10, 10
	dst = np.zeros(img.shape, img.dtype)

	# i in 10, j in 10
	for i in range(dst.shape[0]):
		for j in range(dst.shape[1]):
			# dst[i,j] = tmp[행시작:행끝, 열시작:열끝] * kernel ->합계
			# i, j == 0 일때, tmp[0:0+5, 0:0+5] * kernel -> dst[0, 0]
			# i = 0, j = 1 일때, tmp[0:0+5, 1:1+5] * kernel -> dst[0, 1]
			# i = 0, j = 2 일때, tmp[0:0+5, 2:2+5] * kernel -> dst[0, 2]
			dst[i, j] = (tmp[i:i+kh, j:j+kw] * kernel).sum()

	return dst


img = cv.imread('image/filter_blur.jpg', cv.IMREAD_GRAYSCALE)
ksize = 9

# kernel의 값을 1./(ksize*ksize)로 하는 이유는 무엇일까?
kernel = np.full((ksize,ksize), 1./(ksize*ksize))
img_filtered = filter_gray(img, kernel)

cv.imshow('original', img)
cv.imshow('filtered', img_filtered)
cv.waitKey()

# [Quiz] imgs/hats.png 데이터를 흑백이미지로 읽어들이고,
# # 1. 마우스로 hat.png와 같은 이미지 영역에 대해 mask를 만들고,
# # 2. 이 mask 영역에 대해서만 bluring을 수행한 후, 출력한다.
# # 3. blur kernel의 size = 5로 한다.