# change the contrast keeping the average brightness the same
# [Quiz] for 문으로 scale을 1.0 ~ 1.6까지 0.1씩증가시키면서 그 결과를 출력하자.

import cv2
import numpy as np

img0 = cv2.imread('cat.jpg')
mean = np.zeros(img0.shape, np.uint8)
# 이미지의 컬러채널별 평균 밝기
mean[:,:] = np.mean(img0, (0,1))

for scale in np.linspace(1.0, 1.6, 7):
    tmp = cv2.addWeighted(img0, scale, mean, 1-scale, 0)
    cv2.imshow('img'+str(round(scale, 1)), tmp)

cv2.waitKey()