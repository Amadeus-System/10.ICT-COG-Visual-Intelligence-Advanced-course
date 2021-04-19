# [Quiz] 아래와 같은 출력을 하세요.
# main object: 0, 1, 6
# number of chile: 0, 1, 2

import cv2
import numpy as np

img = np.zeros((480,640,3), np.uint8)

# if thickness == -1, fill inner space with color
cv2.rectangle(img, ( 40,40), (200, 440), (255,255,255), -1)  # left first big box
cv2.rectangle(img, (240,40), (400, 440), (255,255,255), -1)  # center big box
cv2.rectangle(img, (440,40), (600, 440), (255,255,255), -1)  # right last big box

cv2.rectangle(img, ( 80,120), (160, 200), (0,0,0), -1)  # 좌측 상단 작은 블랙 박스
cv2.rectangle(img, ( 80,280), (160, 360), (0,0,0), -1)  # 좌측 하단 작은 블랙 박스
cv2.rectangle(img, (270, 70), (370, 410), (0,0,0), -1)  # 중간 위치 블랙 박스
cv2.rectangle(img, (300,120), (340, 160), (255,255,255), -1)  # 중간 상단 작은 흰 박스
cv2.rectangle(img, (300,220), (340, 260), (255,255,255), -1)  # 중간 중단 작은 흰 박스
cv2.rectangle(img, (300,320), (340, 360), (255,255,255), -1)  # 중간 하단 작은 흰 박스

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print('number of contours :', len(contours))        # 9
print('1st contour[0] shape :', contours[0].shape)  # (4,1,2): 4pts with 2(x,y)
print('hierarchy.shape', hierarchy.shape)           # (1,9,4): 9contours with next, before, child, parent

for i in range(hierarchy.shape[1]):
	print(i, hierarchy[0][i])

def findObject(hier):
	import pandas as pd
	cols = ['next', 'before', 'child','parent']
	hier = pd.DataFrame(hier[0], columns=cols)
	mainObjs = []

	# start의 특징: before와 parent가 없는 node
	start = hier[(hier.before == -1) & (hier.parent == -1)].index[0]
	mainObjs.append(start)
	while True:
		if hier.loc[start, "next"] >= 0:
			start = hier.loc[start, "next"]
			mainObjs.append(start)
		else:
			break
	numOfChild = []
	for mo in mainObjs:
		nc = (hier.parent == mo).sum()
		numOfChild.append(nc)
	return pd.DataFrame({'mainObject':mainObjs, 'numOfChildren':numOfChild})

print(findObject(hierarchy))

colors = [(0,0,255), (0,255,0), (255,0,0), (0,255,255), (255,0,255), (255,255,0), (0,0,255), (0,255,0), (255,0,0)]
for i in range(len(contours)):
	cv2.drawContours(img, contours, i, colors[i], 3)
	# contour의 첫번째 점의 위치 보다 약간 위 좌표
	pos = contours[i][0][0][0], contours[i][0][0][1]-7
	# cv2.putText(img, text, org, font, fontSacle, color[, thickness])
	cv2.putText(img, str(i), pos, cv2.FONT_HERSHEY_SIMPLEX, 1.2, colors[i], 3)

cv2.imshow('img', img)
cv2.waitKey()