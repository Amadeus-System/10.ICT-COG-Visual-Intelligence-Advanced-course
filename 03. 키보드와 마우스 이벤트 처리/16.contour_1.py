# color based object detection with contour
# 13.color_space_6에 대해 contourArea로 filtering 추가

import cv2
import numpy as np

capture = cv2.VideoCapture('capture.avi')
fps = capture.get(cv2.CAP_PROP_FPS)
dt = int(1000./fps)

for i in range(30): capture.read()
_, img0 = capture.read()

img = img0.copy()
x0, y0 = -1, -1
pts = []

# 4개의 detector box를 찍는다.
def on_mouse(event, x, y, flags, param):
	global x0, y0, img
	if event == cv2.EVENT_LBUTTONDOWN:
		pts.append([x,y])
		if (x0,y0) != (-1,-1):
			cv2.line(img, (x0,y0), (x,y), (0,0,255))
		x0, y0 = x, y

cv2.namedWindow('img')
cv2.setMouseCallback('img', on_mouse)

while True:
	cv2.imshow('img', img)
	key = cv2.waitKey(30)
	if key == 27: break

print(pts)

# https://copycoding.tistory.com/150
# cv2.fillPoly(img, pts, color[, lineType[, shift[, offset]]]) → img
# - pts를 이용하여 채워진 다각형을 그린다.
cv2.fillPoly(img, [np.array(pts).reshape((-1,1,2))], (255,255,255))

mask = np.zeros(img.shape[0:2], np.uint8)
cv2.fillPoly(mask, [np.array(pts).reshape((-1,1,2))], 255)

hsv = cv2.cvtColor(img0, cv2.COLOR_BGR2HSV)
hmean, smean, vmean, _ = cv2.mean(hsv,mask)

cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.waitKey()

lower_range = np.array([max(hmean-20, 0), max(smean-40, 0), max(vmean-60, 0)])
upper_range = np.array([min(hmean+20, 180), min(smean+40, 255), min(vmean+60, 255)])

while True:
	ret, frame = capture.read()
	if not ret: break

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	# cv2.inRange(src, lowerb, upperb): 범위안은 값 그대로, 아니면 0로 이미지 리턴
	mask = cv2.inRange(hsv, lower_range, upper_range)
	# 마스크를 둘러싼 칸토어를 구한다
	contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

	# 노이즈를 둘러싼 칸토어는 제외하고 테두리를 그린다.
	for i, c in enumerate(contours):
		if cv2.contourArea(c) > 100:
			cv2.drawContours(frame, contours, i, (0, 0, 255), 2)
	cv2.imshow('frame', frame)
	if cv2.waitKey(dt) == 27: break

capture.release()