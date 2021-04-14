# show histogram for each channel

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)

color = ['b', 'g', 'r']

# 루프를 세번 돌며 각각의 컬러별로 히스토그램 계산
for i, c in enumerate(color):
	hist = cv2.calcHist([img], [i], None, [256], [0,256])
	plt.plot(hist, color=c)
	plt.xlim([0,256])

plt.show()

# [Quiz] cat 이미지에 contrast 1.5 조정해서, 원본과 조정된 이미지의 채널별 히스토그램을 그려보자.