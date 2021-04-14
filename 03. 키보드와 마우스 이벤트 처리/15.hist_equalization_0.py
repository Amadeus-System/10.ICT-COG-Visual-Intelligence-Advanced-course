# https://parkaparka.tistory.com/26

import cv2
from matplotlib import pyplot as plt

img0 = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)
# 히스토그램을 평평하게 변형한 이미지
img1 = cv2.equalizeHist(img0)

cv2.imshow('img0', img0)
cv2.imshow('img1', img1)
cv2.waitKey()

plt.figure(figsize=(14,5))

#원본 히스토그램, 상자수 32
plt.subplot(1,2,1)
plt.hist(img0.ravel(), 32, [0,256])
plt.xlim([0,256])

#평평해진 히스토그램, 상자수 32
plt.subplot(1,2,2)
plt.hist(img1.ravel(), 32, [0,256])
plt.xlim([0,256])

plt.show()

# [Quiz] RGB 색상별로 bin 64의 히스토그램을 그리고, 원본과 평활화이미지를 비교해보자.