# [Quiz] imgs/hats.png 데이터를 흑백이미지로 읽어들이고,
# # 1. 마우스로 hat.png와 같은 이미지 영역에 대해 mask를 만들고,
# # 2. 이 mask 영역에 대해서만 bluring을 수행한 후, 출력한다.
# # 3. blur kernel의 size = 5로 한다.

import cv2 as cv
import numpy as np

def filter_gray(img, kernel, border_type=0):
	kh, kw = kernel.shape[0:2]
	kh2, kw2 = kh//2, kw//2

	tmp_shape = list(img.shape)
	tmp_shape[0] += (kh2*2)
	tmp_shape[1] += (kw2*2)

	tmp = np.zeros(tmp_shape, img.dtype)
	np.copyto(tmp[kh2:kh2+img.shape[0], kw2:kw2+img.shape[1]], img)

	# 원본 이미지의 가장자리를 상, 하, 좌, 우 남는 영역에 복사해 넣음
	if border_type == 1:
		tmpH, tmpW = tmp.shape
		tmp[0        : kh2 ] = tmp[kh2] # top
		tmp[tmpH-kh2 : tmpH] = tmp[tmpH-kh2-1] # bottom
		tmp[:, 0        : kw2 ] = tmp[:, kw2        : kw2+1   ] # left
		tmp[:, tmpW-kw2 : tmpW] = tmp[:, tmpW-kw2-1 : tmpW-kw2] # right

	dst = np.zeros(img.shape, img.dtype)

	for i in range(dst.shape[0]):
		for j in range(dst.shape[1]):
			dst[i, j] = (tmp[i:i+kh, j:j+kw] * kernel).sum()

	return dst

ix, iy, dw, dh = -1, -1, 0, 0
drawing = False

def draw_rectangular(event, x,y, flags, param):
	global ix, iy, dw, dh, drawing

	if event == cv.EVENT_LBUTTONDOWN:  # LBOOTN DOWN state
		drawing = True
		ix, iy = x, y

	elif event == cv.EVENT_MOUSEMOVE:  # Mouse Move
		if drawing == True:  # LBOOTN DOWN : Drawing start
			# rectangle(img, start(x,y), end(x,y), color, line-thickness)
			np.copyto(cpy, img)
			cv.rectangle(cpy, (ix, iy), (x, y), 0, 1)
			cv.rectangle(mask, (ix, iy), (x, y), 255, -1)

	elif event == cv.EVENT_LBUTTONUP:
		# dw, dh = x - ix, y - iy
		dw, dh = np.abs(x - ix), np.abs(y - iy)
		ix, iy = min(x, ix), min(y, iy)
		drawing = False

img = cv.imread('image/hats_small.png', cv.IMREAD_GRAYSCALE)
cpy = img.copy()
mask = np.zeros_like(cpy, np.uint8)
cv.namedWindow('img')
cv.setMouseCallback('img', draw_rectangular)


while True:
	cv.imshow('img', cpy)
	key = cv.waitKey(50)
	if key == 27: break

cv.destroyAllWindows()

ksize = 5
kernel = np.full((ksize,ksize), 1./(ksize*ksize))
small = filter_gray(img[iy:iy+dh, ix:ix+dw], kernel, 1)
# print(small)
np.copyto(img[iy:iy+dh, ix:ix+dw], small)

cv.imshow('filtered', img)
cv.imshow('small', small)
# cv.imshow('filtered', img_filtered)
cv.waitKey()
cv.destroyAllWindows()