# https://bkshin.tistory.com/entry/OpenCV-7-%E3%85%87%E3%85%87
# color image projected in hsv plane
# you can control brightness with UP / DOWN key

import cv2
import numpy as np

# zero image generated with height smax, width hmax
wmax = 256
hmax = 180

himg = np.zeros((hmax, wmax), np.uint8)
wimg = np.zeros((hmax, wmax), np.uint8)
vimg = np.zeros((hmax, wmax), np.uint8)

for h in range(hmax):
	himg[h, :] = h

for w in range(wmax):
	wimg[:, w] = w

cv2.imshow('himg', himg)
cv2.imshow('wimg', wimg)

v = 128
dv = 10

while True:
	# img.fill(value): Fill the array with a scalar value.
	vimg.fill(v)
	# combine with RGB channel with 2D image to 3D image
	hsv = cv2.merge((himg, wimg, vimg))
	bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
	cv2.imshow('vimg', vimg)
	cv2.imshow('bgr', bgr)
	key = cv2.waitKeyEx()
	if key == 27: break

	# Left: 2424832 | up: 2490368 | Right: 2555904 | Down: 2621440
	elif key == 2490368: v += dv  # up key
	elif key == 2621440: v -= dv  # down key

cv2.destroyAllWindows()

# [QUIZ] VIMAG와 BGR 이미지의 관계를 설명해보자.