# color image histogram equalization

import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)

#컬러별로 분리한후 각각 히스토그램 평평하게 변환
b, g, r = cv2.split(img)
b1 = cv2.equalizeHist(b)
g1 = cv2.equalizeHist(g)
r1 = cv2.equalizeHist(r)
img_bgr_eq = cv2.merge((b1,g1,r1)) #변형된 각각 채널을 합침

# HSV 컬러공간으로 변환후 Value 채널만 평평히
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
v1 = cv2.equalizeHist(v)
hsv1 = cv2.merge((h,s,v1)) #평평해진 Value 채널로 대체
img_hsv_eq = cv2.cvtColor(hsv1, cv2.COLOR_HSV2BGR)

# YCrCb 컬러공간으로 변환후 Y 채널만 평평히
YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
y, r, b = cv2.split(YCrCb)
y1 = cv2.equalizeHist(y)
Y1CrCb = cv2.merge((y1,r,b)) #평평해진 Y 채널로 대체
img_YCrCb_eq = cv2.cvtColor(Y1CrCb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('img', img)
cv2.imshow('img_bgr_eq', img_bgr_eq) # 컬러가 변형되었습니다.
cv2.imshow('img_hsv_eq', img_hsv_eq) # 컬러가 변형되지 않습니다.
cv2.imshow('img_YCrCb_eq', img_YCrCb_eq) # 컬러가 변형되지 않습니다.
cv2.waitKey()