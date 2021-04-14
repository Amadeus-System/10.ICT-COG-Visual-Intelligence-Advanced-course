# https://076923.github.io/posts/Python-opencv-21/
# contour hierarchy
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

cv2.imshow('img', img)
cv2.waitKey()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 리스트형식으로 칸토어들을 반환
# contours, _ = cv2.findContours(img_gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# 트리형식으로 칸토어들을 반환 hierarchy 에 트리 정보
# - hierarchy는 윤곽선의 계층 구조를 의미합니다. 각 윤곽선에 해당하는 속성 정보들이 담겨있습니다.
contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print('number of contours :', len(contours))        # 9
print('1st contour[0] shape :', contours[0].shape)  # (4,1,2): 4pts with 2(x,y)
print('hierarchy.shape', hierarchy.shape)           # (1,9,4): 9contours with next, before, child, parent

for i in range(hierarchy.shape[1]):
	# [같은 부모의 자식중에 다음 칸토어 인덱스, 전 칸토어 인덱스, 첫번째 자식 인덱스, 부모 인덱스]
	print(i, hierarchy[0][i])

colors = [(0,0,255), (0,255,0), (255,0,0), (0,255,255), (255,0,255), (255,255,0), (0,0,255), (0,255,0), (255,0,0)]
for i in range(len(contours)):
	cv2.drawContours(img, contours, i, colors[i], 3)
	# contour의 첫번째 점의 위치 보다 약간 위 좌표
	pos = contours[i][0][0][0], contours[i][0][0][1]-7
	# cv2.putText(img, text, org, font, fontSacle, color[, thickness])
	cv2.putText(img, str(i), pos, cv2.FONT_HERSHEY_SIMPLEX, 1.2, colors[i], 3)

cv2.imshow('img', img)
cv2.waitKey()

# [Quiz] 아래와 같은 출력을 하세요.
# main object: 0, 1, 6
# number of chile: 0, 1, 2