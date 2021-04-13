# YUV color model is called with YCrCb,
# - Y는 밝기(Luma): equal to GRAY,
# - U는 밝기와 파란색과의 색상 차(Chroma Blue, Cb),
# - V는 밝기와 빨간색과의 색상 차(Chroma Red, Cr).
# - https://bkshin.tistory.com/entry/OpenCV-7-%E3%85%87%E3%85%87

import cv2
import numpy as np

rmax = 256
bmax = 256

yimg = np.zeros((rmax,bmax), np.uint8)  # y: brightness
bimg = np.zeros((rmax,bmax), np.uint8)  # b: blue - y
rimg = np.zeros((rmax,bmax), np.uint8)  # r: red - y

for r in range(rmax):
	rimg[r,:] = r

for b in range(bmax):
	bimg[:,b] = b

y = 128
dy = 10
while True:
	yimg.fill(y)
	YCrCb = cv2.merge((yimg,rimg,bimg))
	bgr = cv2.cvtColor(YCrCb, cv2.COLOR_YCrCb2BGR)
	cv2.imshow('YUV color-space', bgr)
	key = cv2.waitKeyEx()
	if key == 27: break
	elif key == 2490368: y += dy
	elif key == 2621440: y -= dy

# 참고 : [0, 255] 색 공간 표현을 위한 개선 수식
# Y = 0.299R + 0.587G + 0.114B
# U = (B-Y) * 0.565
# V = (R-Y) * 0.713
#
# R = Y + 1.403 V
# G = Y - 0.344 U - 0.714 V
# B = Y + 1.770 U