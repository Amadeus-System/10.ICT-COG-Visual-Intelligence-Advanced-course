# [Quiz] image/hats_small.png 파일의 명도를 20% 줄여
# image/hats_smallDim.png로 저장하자.
import cv2
img = cv2.imread("image/hats_small.png")
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(HSV)

# V *= 0.8
V = cv2.addWeighted(V, 0.8, V, 0, 0)

HSV = cv2.merge((H,S,V))
BGR = cv2.cvtColor(HSV, cv2.COLOR_HSV2BGR)
cv2.imwrite('image/hats_smallDim.png', BGR)

cv2.imshow('original', img)
cv2.imshow('lowV', BGR)
cv2.waitKey()