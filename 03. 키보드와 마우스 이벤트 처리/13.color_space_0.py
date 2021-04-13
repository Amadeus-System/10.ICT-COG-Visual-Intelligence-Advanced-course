import cv2
import numpy as np

# YUV color model is called with YCrCb,
# - Y는 밝기(Luma): equal to GRAY,
# - U는 밝기와 파란색과의 색상 차(Chroma Blue, Cb),
# - V는 밝기와 빨간색과의 색상 차(Chroma Red, Cr).

bgr = cv2.imread('cat.jpg')

gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
YCrCb = cv2.cvtColor(bgr, cv2.COLOR_BGR2YCrCb)
print(gray.shape, gray.dtype)
print(YCrCb.shape, YCrCb.dtype)

Y, Cr, Cb = cv2.split(YCrCb)

# np.array_equal(A, B) : np.all(A==B)
print('np.array_equal(gray, Y) =', np.array_equal(gray, Y))

cv2.imshow('bgr', bgr)
cv2.imshow('gray', gray)
cv2.imshow('Y', Y)
cv2.imshow('Cr', Cr)
cv2.imshow('Cb', Cb)
cv2.waitKey()
cv2.destroyAllWindows()