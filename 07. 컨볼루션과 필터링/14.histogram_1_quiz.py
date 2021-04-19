# show histogram for each channel
# [Quiz] cat 이미지에 contrast 1.5 조정해서, 원본과 조정된 이미지의 채널별 히스토그램을 그려보자.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)
mean = np.zeros(img.shape, np.uint8)
#이미지의 컬러채널별 평균 밝기
mean[:,:] = np.mean(img, (0,1))
print(np.mean(img, (0,1)))

scale = 1.5
# img1 = (img0-mean)*scale + mean
img1 = cv2.addWeighted(img, scale, mean, 1-scale, 0)
color = ['b', 'g', 'r']

fig, axes = plt.subplots(1,2, sharex=True, sharey=True, figsize=(14,5))
# 원본 img에 대해 루프를 세번 돌며 각각의 컬러별로 히스토그램 계산
for i, c in enumerate(color):
	hist = cv2.calcHist([img], [i], None, [256], [0,256])
	axes[0].plot(hist, color=c)
	axes[0].set_xlim([0,256])
	axes[0].set_ylim([0,3000])
	axes[0].set_title("original")

# 루프를 세번 돌며 각각의 컬러별로 히스토그램 계산
for i, c in enumerate(color):
	hist = cv2.calcHist([img1], [i], None, [256], [0,256])
	axes[1].plot(hist, color=c)
	axes[1].set_xlim([0,256])
	axes[0].set_ylim([0,3000])
	axes[1].set_title("contrasted")

plt.show()