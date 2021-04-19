# [Quiz] drawContours 대신에 polylines를 이용하여 등고선을 그려보자.

import cv2
import numpy as np

img = np.zeros((480,640,3), np.uint8)

cv2.circle(img, (200,150), 80, (255,255,0), -1)
cv2.circle(img, (500,150), 50, (255,0,0), -1)
cv2.rectangle(img, (300,300), (500,400), (0,255,255), -1)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 150 을 기준으로 더 큰값은 255 아니면 0으로 이진 이미지 생성
_, img_thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(img_thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

print(type(contours[0])) # contour is numpy.ndarray
print('contours')

for c in contours:
	print(c.shape, c.dtype, cv2.contourArea(c))

colors = [(0,255,0), (0,0,255)]

for c in range(len(contours)):
	# cv2.drawContours(img, contours, c, colors[c], 3)
	cv2.polylines(img, [contours[c].reshape((-1,2))], True, colors[c], 3)

# 모든 칸토어를 그린다.
# cv2.drawContours(img, contours, -1, (0,0,255), 3)
# cv2.polylines(img, [c.reshape((-1,2)) for c in contours], True, (0,0,255), 3)

cv2.imshow('img', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_thresh', img_thresh)
cv2.waitKey()