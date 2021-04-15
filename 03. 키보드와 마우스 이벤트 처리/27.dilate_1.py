# remove noise from image using erode iter and deliate iter
# 1. 이미지를 grayscale로 읽고, 이를 이진화한 mask를 생성
# 2. mask를 delate하고, unmasking하여 백그라운만의 평균 값을 취함
# 3. mask를 침식팽창하여 노이즈를 제거한 객체 이미지 윤곽 mask를 생성
# 4. 윤곽 mask와 윤곽 unmask를 이용하여 face와 backgraound를 결합

import cv2 as cv
import numpy as np

img = cv.imread('face_with_noise.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, mask = cv.threshold(img_gray, 100, 255, cv.THRESH_BINARY)

# kernel = None -> kernel = 3 by 3 filled with 1s
mask_dilated = cv.dilate(mask, None, iterations=6)
# background_mean : 이미지에서 배경이 되는 부분의 평균 컬러
background_mean = cv.mean(img, mask=cv.bitwise_not(mask_dilated))

print(background_mean) # 청색이 강한 배경 이미지 = 춧 픽셀값과 같다
print(img[0,0])
background = np.full(img.shape, background_mean[0:3], dtype=np.uint8)

# kernel = None -> kernel = 3 by 3 filled with 1s. eliminate noise
mask_eroded = cv.erode(mask, None, iterations=3)

# generate denoised images - delated face mask
mask_eroded_dilated = cv.dilate(mask_eroded, None, iterations=6)
mask_eroded_dilated_not = cv.bitwise_not(mask_eroded_dilated)
face = cv.bitwise_and(img, img, mask=mask_eroded_dilated)
not_face = cv.bitwise_and(background, background, mask=mask_eroded_dilated_not)
img_without_noise = cv.add(face, not_face)

face_without_noise = cv.imread('face_without_noise.png')
print('Success =', np.array_equal(img_without_noise, face_without_noise))

face_mask = cv.bitwise_and(mask, mask_eroded_dilated)
print('mask =? face mask', np.array_equal(mask, face_mask))

cv.imshow('img', img)
cv.imshow('img_gray', img_gray)
cv.imshow('mask', mask)
cv.imshow('mask_dilated', mask_dilated)
cv.imshow('mask_eroded', mask_eroded)
cv.imshow('mask_eroded_dilated', mask_eroded_dilated)
cv.imshow('mask_eroded_dilated_not', mask_eroded_dilated_not)
cv.imshow('face', face)
cv.imshow('not_face', not_face)
cv.imshow('img_without_noise', img_without_noise)
cv.imshow('face_mask', face_mask)
cv.waitKey()

# [Quiz] face 객체를 얻어내는 과정을 좀 더 단순화하여 구현해보자.