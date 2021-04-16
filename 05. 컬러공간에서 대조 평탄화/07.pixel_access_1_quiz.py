# [Quiz] (400, 400) 검은 사각형을 꽉 채우는 하얀 원을 그리고, / 방향의 녹색 대각선을 그린다.

import cv2
import numpy as np

s = 400

img = np.zeros((s,s,3), dtype=np.uint8)
cv2.circle(img, (200,200), 200, (255,255,255), -1)
cv2.line(img, (0,400), (400,0), (0,255,0), 3)

cv2.imshow('img', img)
cv2.waitKey()