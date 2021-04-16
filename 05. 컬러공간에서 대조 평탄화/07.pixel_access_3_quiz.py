# [Quiz] cat 컬러이미지와 회색만 있는 이미지의 평균 이미지를 생성하자.
import cv2
import numpy as np

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)
gray = np.full_like(img, 127, dtype=np.uint8)

dst = img // 2 + gray // 2
cv2.imshow('org', img)
cv2.imshow('grayed', dst)

# incorrect example: img + gray generate overflow
bad = (img + gray) // 2
cv2.imshow('bad', bad)

# safe operation example
safe = (img.astype(np.int32) + gray.astype(np.int32)) // 2
safe = (img.astype(np.float32) + gray.astype(np.float32)) / 2
safe = safe.astype(np.uint8)
cv2.imshow('safe', safe)

cv2.waitKey(0)
cv2.destroyAllWindows()