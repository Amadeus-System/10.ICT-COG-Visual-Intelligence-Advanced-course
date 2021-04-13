# set all red channels to 0

import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('org', img)

img[:,:,2] = 0

cv2.imshow('cvt',img)
cv2.waitKey()

# [Quiz]
# 1. cat이미지의 명도를 1/2로 줄인 half 이미지와
# 2. cat이미지의 명도를 2배로 늘린 twice 이미지를 생성하세요.