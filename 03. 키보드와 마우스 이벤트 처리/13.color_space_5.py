# decrease the color saturation, increase the color saturation, change the hue
import cv2

bgr = cv2.imread('cat.jpg')

hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
s1 = cv2.addWeighted(s, 0.5, s, 0, 0)      # 채도를 절반으로
s2 = cv2.addWeighted(s, 2.0, s, 0, 0)      # 채도를 2배로
h1 = cv2.addWeighted(h, 1.0, h, 0, 180//2) # 색상에 대해 90을 추가

hs1v = cv2.merge((h,s1,v))
hs2v = cv2.merge((h,s2,v))
h1sv = cv2.merge((h1,s,v))

cv2.imshow('bgr', bgr) # 원본 이미지
cv2.imshow('h', h)
cv2.imshow('s', s)
cv2.imshow('v', v)
cv2.imshow('hs1v', cv2.cvtColor(hs1v, cv2.COLOR_HSV2BGR)) # 채도를 절반으로
cv2.imshow('hs2v', cv2.cvtColor(hs2v, cv2.COLOR_HSV2BGR)) # 채도를 두배로
cv2.imshow('h1sv', cv2.cvtColor(h1sv, cv2.COLOR_HSV2BGR)) # 색상에 90을 추가
# - R -> GB, G -> RB, B -> GR

cv2.waitKey()