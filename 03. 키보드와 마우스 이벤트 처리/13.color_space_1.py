# https://m.blog.naver.com/PostView.nhn?blogId=2idhse&logNo=50159750975&proxyReferer=https:%2F%2Fwww.google.com%2F

import cv2
import numpy as np

# HSV 방식의 3개 채널은 H(Hue, 색조), S(Saturation, 채도), V(Value, 명도)입니다.
# - H 값은 이미지가 어떤 색상인지를 나타냅니다. 빨간색 0도, 녹색 120도, 파란색이 240도
# # - opencv 에서는 (0 ~ 180). R이 0, G가 60, B가 120
# # - S는 이미지의 색상이 얼마나 순수하게 포함되어 있는지를 나타냅니다.
# # - V는 색상이 얼마나 밝은지 어두운지를 표현합니다.

bgr = cv2.imread('cat.jpg')

HSV = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

H, S, V = cv2.split(HSV)

cv2.imshow('bgr', bgr)
cv2.imshow('H', H)
cv2.imshow('S', S)
cv2.imshow('V', V)
cv2.waitKey()

cv2.imwrite('cat-h.png', H)
cv2.imwrite('cat-s.png', S)
cv2.imwrite('cat-v.png', V)