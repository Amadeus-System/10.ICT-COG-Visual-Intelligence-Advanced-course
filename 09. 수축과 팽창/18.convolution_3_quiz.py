# [Quiz] filter size를 3, 5, 9로 할 때, 이미지의 변화를 그려보자.
# - 이때, zero-padding, 또는 edge-padding을 적용해하여 변화가 있는 지 확인한다.

import cv2 as cv
import numpy as np


def filter_gray(img, kernel, border_type):

	kh, kw = kernel.shape[0:2]
	kh2, kw2 = kh//2, kw//2

	tmp_shape = list(img.shape)
	tmp_shape[0] += (kh2*2)
	tmp_shape[1] += (kw2*2)

	tmp = np.zeros(tmp_shape, img.dtype)
	np.copyto(tmp[kh2:kh2+img.shape[0], kw2:kw2+img.shape[1]], img)

	if border_type == 1:
		tmpH, tmpW = tmp.shape
		tmp[0        : kh2 ] = tmp[kh2]
		tmp[tmpH-kh2 : tmpH] = tmp[tmpH-kh2-1]
		tmp[:, 0        : kw2 ] = tmp[:, kw2        : kw2+1   ]
		tmp[:, tmpW-kw2 : tmpW] = tmp[:, tmpW-kw2-1 : tmpW-kw2]

	dst = np.zeros(img.shape, img.dtype)

	for i in range(dst.shape[0]):
		for j in range(dst.shape[1]):
			dst[i,j] = (tmp[i:i+kh, j:j+kw] * kernel).sum()

	return dst


def filter(img, kernel, border_type=0):
	channels = cv.split(img)
	channels_filtered = []
	for channel in channels:
		channels_filtered.append(filter_gray(channel, kernel, border_type))
	img_filtered = cv.merge(channels_filtered)
	return img_filtered


img = cv.imread('image/filter_blur.jpg', cv.IMREAD_COLOR)
cv.imshow('original', img)

ksizes = [3, 5, 9]
for ksize in ksizes:
	kernel = np.full((ksize,ksize), 1./(ksize*ksize))
	img_filtered = filter(img, kernel)
	cv.imshow(f'{ksize}filtered', img_filtered)
	border = 1
	img_filtered = filter(img, kernel, border)
	cv.imshow(f'{ksize}filterBordered', img_filtered)

cv.waitKey()