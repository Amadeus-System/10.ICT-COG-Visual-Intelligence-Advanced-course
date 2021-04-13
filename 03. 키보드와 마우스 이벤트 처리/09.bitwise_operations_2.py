# logo

import cv2
import numpy as np

img = cv2.imread('bit_test.jpg', cv2.IMREAD_COLOR)
logo = cv2.imread('logo.jpg', cv2.IMREAD_COLOR)

# 컬러를 흑백이미지로 변환
# - PAL, NTSC: Y = 0.299 * R + 0.587 * G + 0.114 * B
# - HDTV, IUT-R BT.709: Y = 0.2126 * R + 0.7152 * G + 0.0722 * B
logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

# 10 보다 큰 값을 가진 픽셀은 255로 아니면 0으로 이진 이미지 생성
_, mask = cv2.threshold(logo_gray, 15, 255, cv2.THRESH_BINARY)
print(_) # threshold 값을 리턴한다.

img_rows, img_cols = img.shape[0:2]
logo_rows, logo_cols = logo.shape[0:2]
roi_x = (img_cols - logo_cols)//2
roi_y = (img_rows - logo_rows)//2
img_target = np.copy(img)

#img_target 과 roi 는 이미지를 공유, 즉 View
roi = img_target[roi_y:roi_y+logo_rows, roi_x:roi_x+logo_cols]

logo_fg = cv2.bitwise_and(logo, logo, mask=mask)
mask_inv = cv2.bitwise_not(mask)
img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# roi = cv2.add(logo_fg, img_bg)  # not good. roi View is reference to another array
np.copyto(roi, cv2.add(logo_fg, img_bg))
# dst = cv2.add(logo_fg, img_bg)
# img[starty:starty+logo_rows, startx:startx+logo_cols] = dst

cv2.imshow('img', img)
cv2.imshow('logo', logo)
cv2.imshow('logo_gray', logo_gray)
cv2.imshow('mask', mask)
cv2.imshow('roi', roi)
cv2.imshow('logo_fg', logo_fg)
cv2.imshow('img_bg', img_bg)
cv2.imshow('img_target', img_target)
cv2.waitKey()

# [Quiz] 코드가 상당히 복잡하다. 간략화된 빠른 연산으로 변경해보자.