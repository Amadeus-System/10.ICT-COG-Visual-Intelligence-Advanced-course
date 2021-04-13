# color based object detection
# 1. 첫 이미지에서 L버튼으로 4개의 검출 박스영역을 지정하고 ESC
# 2. 이미지의 검출영역과 마스크를 확인한 후 임의의 버튼
# 3. 동영상에 검출되는 이미지 검출 영역과 마스크를 확인한다.

import cv2
import numpy as np

# 미리 저장한 동영상 파일을 읽어옵니다.
capture = cv2.VideoCapture('capture.avi')
# 동영상을 저장할 때 지정한 FPS
fps = capture.get(cv2.CAP_PROP_FPS)
# 정상 속도를 위해 한장 당 보여줄 시간
dt = int(1000./fps)

# 카메라가 처음 시작될때 노출때문에 제대로 읽어오지 못할 수 있으므로 처음 몇장은 버립니다.
for i in range(30): capture.read()
_, img0 = capture.read()

img = img0.copy()
x0, y0 = -1, -1
pts = [] # 마우스를 클릭할 좌표를 저장 하게됨

# 4개의 점을 찍어 영역표시 후, ESC
def on_mouse(event, x, y, flags, param):
	global x0, y0, img
	if event == cv2.EVENT_LBUTTONDOWN:
		pts.append([x,y]) # 클릭좌표 저장
		if (x0,y0) != (-1,-1):
			cv2.line(img, (x0,y0), (x,y), (0,0,255))
		x0, y0 = x, y

cv2.namedWindow('img')
cv2.setMouseCallback('img', on_mouse)

while True:
	cv2.imshow('img', img)
	if cv2.waitKey(dt) == 27: break

print(pts)

# 어느영역을 지정했는지 표시
cv2.fillPoly(img, [np.array(pts).reshape((-1,1,2))], (255,255,255))

# 지정한 영역으로 마스크 생성
mask = np.zeros(img.shape[0:2], np.uint8)
cv2.fillPoly(mask, [np.array(pts).reshape((-1,1,2))], 255)

# HSV 컬러공간으로 변환
hsv = cv2.cvtColor(img0, cv2.COLOR_BGR2HSV)
# 지정한 공간의 컬러, 채도, 밝기 평균 :
# hmean, smean, vmean = np.mean(hsv[mask.astype(np.bool)], axis=[0,1])
hmean, smean, vmean, _ = cv2.mean(hsv, mask)
print('hmean =', hmean)
print('smean =', smean)
print('vmean =', vmean)

cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.waitKey()

# 다음과 같은 범위에 들어가는 이미지의 픽셀만 추출
lower_range = np.array([max(hmean-20,0), max(smean-40,0), max(vmean-60,0)])
upper_range = np.array([min(hmean+20,180), min(smean+40,255), min(vmean+60,255)])
print('lower_range =', lower_range)
print('upper_range =', upper_range)

while True:
	ret, frame = capture.read()
	if not ret: break

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	# 범위안의 값들을 가진 픽셀들만으로 마스크 생성
	mask = cv2.inRange(hsv, lower_range, upper_range)

	# 이미지에서 추적한 사물 이외의 배경은 검정으로 만듬
	obj = cv2.bitwise_and(frame, frame, mask=mask)
	cv2.imshow('obj', obj)
	cv2.imshow('mask', mask)
	if cv2.waitKey(dt) == 27: break

capture.release()

# [Quiz] YCrCb 색상공간에서 적절한 값의 범위를 찾아 object detection을 수행합니다.