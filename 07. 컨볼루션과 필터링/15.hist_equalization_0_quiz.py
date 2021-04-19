# [Quiz] HSV, YCrCb 공간 각각에서 명도만 평활하고,
# - 원본과 각 이미지를 출력한 후,
# - 원본이미지와 비교하여 BGR 색상별로 bin 64의 히스토그램을 그려보자.
# - 추가로 BGR 채널 각각에 평활화를 할 경우는 어떤 현상이 생기는 지 알아보자.

import cv2
from matplotlib import pyplot as plt

img0 = cv2.imread('cat.jpg')
bins = 256

# HSV 컬러공간으로 변환후 Value 채널만 평평히
hsv = cv2.cvtColor(img0, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
v1 = cv2.equalizeHist(v)
hsv1 = cv2.merge((h,s,v1)) #평평해진 Value 채널로 대체
img_hsv = cv2.cvtColor(hsv1, cv2.COLOR_HSV2BGR)

# YCrCb 컬러공간으로 변환후 Y 채널만 평평히
YCrCb = cv2.cvtColor(img0, cv2.COLOR_BGR2YCrCb)
y, r, b = cv2.split(YCrCb)
y1 = cv2.equalizeHist(y)
Y1CrCb = cv2.merge((y1,r,b)) #평평해진 Y 채널로 대체
img_YCrCb = cv2.cvtColor(Y1CrCb, cv2.COLOR_YCrCb2BGR)

# 잘못된 예: RGB 모든 채널을 각각 평활화할 경우
b, g, r = cv2.split(img0)
b1 = cv2.equalizeHist(b)
g1 = cv2.equalizeHist(g)
r1 = cv2.equalizeHist(r)
rgb_equal = cv2.merge((b1,g1,r1)) #평평해진 Value 채널로 대체

cv2.imshow('img0', img0)
cv2.imshow('img_hsv', img_hsv)
cv2.imshow('img_YCrCb', img_YCrCb)
cv2.imshow('img_rgb_equal', rgb_equal)
cv2.waitKey()

color = ['b', 'g', 'r']

fig, axes = plt.subplots(1,4, sharex=True, sharey=True, figsize=(21,5))
# 원본 img에 대해 루프를 세번 돌며 각각의 컬러별로 히스토그램 계산
for i, c in enumerate(color):
	hist = cv2.calcHist([img0], [i], None, [bins], [0,256])
	axes[0].plot(hist, color=c)
	axes[0].set_xlim([0,bins])
	axes[0].set_ylim([0,10000])
	axes[0].set_title("original")

# 루프를 세번 돌며 각각의 컬러별로 히스토그램 계산
for i, c in enumerate(color):
	hist = cv2.calcHist([img_hsv], [i], None, [bins], [0,256])
	axes[1].plot(hist, color=c)
	axes[1].set_xlim([0,bins])
	axes[1].set_ylim([0,10000])
	axes[1].set_title("HSVEqualized")

# 루프를 세번 돌며 각각의 컬러별로 히스토그램 계산
for i, c in enumerate(color):
	hist = cv2.calcHist([img_YCrCb], [i], None, [bins], [0,256])
	axes[2].plot(hist, color=c)
	axes[2].set_xlim([0,bins])
	axes[2].set_ylim([0,10000])
	axes[2].set_title("YCrCbEqualized")

# 루프를 세번 돌며 각각의 컬러별로 히스토그램 계산
for i, c in enumerate(color):
	hist = cv2.calcHist([rgb_equal], [i], None, [bins], [0,256])
	axes[3].plot(hist, color=c)
	axes[3].set_xlim([0,bins])
	axes[3].set_ylim([0,10000])
	axes[3].set_title("rgb_equal")

plt.show()