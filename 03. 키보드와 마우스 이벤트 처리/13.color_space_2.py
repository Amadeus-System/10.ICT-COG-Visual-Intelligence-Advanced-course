import cv2
import numpy as np

H = cv2.imread('cat-h.png', cv2.IMREAD_GRAYSCALE)
S = cv2.imread('cat-s.png', cv2.IMREAD_UNCHANGED)
V = cv2.imread('cat-v.png', cv2.IMREAD_UNCHANGED)

# BGR 처럼 merge할 경우 잘 못된 이미지를 생성한다.
HSV = cv2.merge((H,S,V))
BGR = cv2.cvtColor(HSV, cv2.COLOR_HSV2BGR)

cv2.imshow('H', H)
cv2.imshow('S', S)
cv2.imshow('V', V)
cv2.imshow('HSV', HSV)
cv2.imshow('BGR', BGR)
cv2.waitKey()

# [Quiz] image/hats_small.png 파일의 명도를 20% 줄여
# - image/hats_smallDim.png로 저장하자.