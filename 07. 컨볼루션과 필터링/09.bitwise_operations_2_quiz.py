# [Quiz] masking 연산을 numpy fancy indexing으로 처리하자

import cv2
import numpy as np

img = cv2.imread('bit_test.jpg', cv2.IMREAD_COLOR)
logo = cv2.imread('logo.jpg', cv2.IMREAD_COLOR)
cv2.imshow('orig', img)
cv2.imshow('logo', logo)

logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(logo_gray, 10, 255, cv2.THRESH_BINARY)

rows, cols = img.shape[:2]
logo_rows, logo_cols = logo.shape[:2]
starty, startx = (rows - logo_rows) // 2, (cols - logo_cols) // 2

roi = img[starty:starty+logo_rows, startx:startx+logo_cols]

roi[mask.astype(bool)] = logo[mask.astype(bool)]
# equivalent with cv2.copyTo(src, mask, dst)
# # cv2.copyTo(logo, mask, roi)

cv2.imshow('res', img)
cv2.waitKey(0)
cv2.destroyAllWindows()