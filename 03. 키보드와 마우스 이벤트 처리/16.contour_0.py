# https://opencv-python.readthedocs.io/en/latest/doc/15.imageContours/imageContours.html
# https://076923.github.io/posts/Python-opencv-21/
import cv2
import numpy as np

# Contours란 동일한 색 또는 동일한 강도를 가지고 있는 영역의 경계선을 연결한 선입니다.
# 1. cv2.threshold를 이용하여 이미지에서 threshold를 생성한다.
# 2. cv2.findContours로 threshold에서 윤곽선(contours)을 찾아낸다.
# 3. 모든 contour에 투프를 돌며, cv2.drawContours로 contour를 그린다.

img = np.zeros((480,640,3), np.uint8)

cv2.circle(img, (200,150), 80, (255,255,0), -1)
# blue는 GRAY로 변환시 값이 낮아, contour로 잘 표시되지 않는다.
cv2.circle(img, (500,150), 50, (255,0,0), -1)
cv2.rectangle(img, (300,300), (500,400), (0,255,255), -1)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 150 을 기준으로 더 큰값은 255 아니면 0으로 이진 이미지 생성
_, img_thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

# cv2.findContours(image, mode, method[, contours[, hierarchy[, offset]]]) → [image, ]contours, hierarchy
# 물체를 둘러싼 칸토어를 구한다.
# mode는 검색방법을 지정하며, 이에 따랴 return 값이 달라진다. RETR_TREE는 3개
# - cv2.RETR_EXTERNAL : 외곽 윤곽선만 검출하며, 계층 구조를 구성하지 않습니다.
# - cv2.RETR_LIST : 모든 윤곽선을 검출하며, 계층 구조를 구성하지 않습니다.
# - cv2.RETR_CCOMP : 모든 윤곽선을 검출하며, 계층 구조는 2단계로 구성합니다.
# - cv2.RETR_TREE : 모든 윤곽선을 검출하며, 계층 구조를 모두 형성합니다. (Tree 구조)
# method는 근사화 방법을 지정한다.
# - cv2.CHAIN_APPROX_NONE : 윤곽선들의 모든 점을 반환합니다.
# - cv2.CHAIN_APPROX_SIMPLE : 윤곽점들 단순화 수평, 수직 및 대각선 요소를 압축하고 끝점만 남겨 둡니다.(사각형이면 4개)
# - cv2.CHAIN_APPROX_TC89_L1 : 프리먼 체인 코드에서의 윤곽선으로 적용합니다.
# - cv2.CHAIN_APPROX_TC89_KCOS : 프리먼 체인 코드에서의 윤곽선으로 적용합니다.

contours, _ = cv2.findContours(img_thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

print(type(contours[0])) # contour is numpy.ndarray
print('contours')
# c.shape[0]: 각 contour의 연결점의 수, c.shape[-1]: 연결점의 x, y좌표
for c in contours:
	print(c.shape, c.dtype, cv2.contourArea(c))
	# (4, 1, 2) 	int32 	20000.0 - 사각형
	# (244, 1, 2) 	int32 	19854.0 - 원

# 0번째 칸토어의 3번째 점의 x, y 좌표
print(contours[0][2][0][0], contours[0][2][0][1])

# 2개의 contour가 있다는 것을 사전에 알고 있으므로, coutour에 대한 색을 지정
colors = [(0,255,0), (0,0,255)]

# 모든 contour에 투프를 돌며, contour를 그린다.
# cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]]) → dst
for c in range(len(contours)):
	# 선의 두께 3으로 c 번째 칸토어를 그린다.
	cv2.drawContours(img, contours, c, colors[c], 3)
	# cv2.polylines(img, [contours[c].reshape((-1,2))], True, colors[c], 3)

# 모든 칸토어를 그린다.
# cv2.drawContours(img, contours, -1, (0,0,255), 3)
# cv2.polylines(img, [c.reshape((-1,2)) for c in contours], True, (0,0,255), 3)


cv2.imshow('img', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_thresh', img_thresh)
cv2.waitKey()

# [Quiz] drawContours 대신에 polylines를 이용하여 등고선을 그려보자.