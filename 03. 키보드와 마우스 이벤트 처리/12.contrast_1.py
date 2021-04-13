# change the contrast keeping the average brightness the same

import cv2
import numpy as np

img0 = cv2.imread('cat.jpg')
mean = np.zeros(img0.shape, np.uint8)
# 이미지의 컬러채널별 평균 밝기
mean[:,:] = np.mean(img0, (0,1))
print(np.mean(img0, (0,1)))

scale = 1.5
# img1 = (img0-mean)*scale + mean
# img1 = img0 + a(img0 - mean) : a = scale - 1 < 1
img1 = cv2.addWeighted(img0, scale, mean, 1-scale, 0)
print(np.mean(img1, (0,1)))

cv2.imshow('img0', img0)
cv2.imshow('mean', mean)
cv2.imshow('img1', img1)
cv2.waitKey()

# [Quiz]
# for 문으로 scale을 1.0 ~ 1.6까지 0.1씩증가시키면서 그 결과를 출력하자.