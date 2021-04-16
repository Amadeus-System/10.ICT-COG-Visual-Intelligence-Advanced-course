# [Quiz]
# 1. cat이미지의 명도를 1/2로 줄인 half 이미지와
# 2. cat이미지의 명도를 2배로 늘린 twice 이미지를 생성하세요.

import cv2
import numpy as np

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('orig', img)

half = img // 2
cv2.imshow('half', half)

twice = np.where(img > 127, 255, img*2)
cv2.imshow('twice', twice)

# 잘 못된 예 - overflow 발생
chan_mean = img.mean(axis=(0,1))
print(chan_mean)
twice2 = img*2
# twice2 = np.zeros_like(img, dtype=np.int32)
# twice2 = img*2*chan_mean.sum()/chan_mean
# twice2 = np.where(twice2 > 255, 255, twice2).astype(np.uint8)
cv2.imshow('twice2', twice2)

cv2.waitKey()

