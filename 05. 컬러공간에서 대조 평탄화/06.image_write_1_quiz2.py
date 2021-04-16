# [Quiz] cat.jpg 파일을 흑백이미지로 읽고,
# 가운데는 밝고, 외곽으로 갈 수록 어두어져서
# fade-in과 같은 효과를 가지도록 이미지를 생성하여 저장하자.

import cv2
import numpy as np

img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)
fade = np.zeros_like(img)
h, w = img.shape
for i in range(h):
    for j in range(w):
        fade[i, j] = int((h/2*w/2 - abs(i - h/2) * abs(j - w/2)) / (h/2*w/2) * 255)

dst = np.zeros_like(img)
dst = img // 2 + fade // 2

cv2.imshow('cat',img)
cv2.imshow('dst',dst)
cv2.imshow('fade', fade)
cv2.waitKey()

# 잘 못된 예
dst2 = np.zeros_like(img)
dst2 = (img + fade) // 2
cv2.imshow('dst2',dst2)
cv2.waitKey()

cv2.imwrite('fade.jpg', dst)
cv2.destroyAllWindows()