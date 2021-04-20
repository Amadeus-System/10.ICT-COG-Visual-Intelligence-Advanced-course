# 허프 원 검출 (hough_circle.py)
# [Quiz] 여러개의 공을 검출할 수 있도록 수정해보자.

import cv2
import numpy as np

img = cv2.imread('image/coins.jpg')
# 그레이 스케일 변환 ---①
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 노이즈 제거를 위한 가우시안 블러 ---②
blur = cv2.GaussianBlur(gray, (3,3), 0.5)
# blur = cv2.medianBlur(gray, 5)
# 허프 원 변환 적용( dp=1.2, minDist=30, cany_max=200 ) ---③
# - dp: 입력 영상과 축적 배열의 크기 비율
# - minDist: 인접 원 중심의 최소 거리
# - param1: Canny edge 검출기의 높은 임계값. 작은 임계값은 이의 절반값 할당
# - param2: 축적 배열에서 원 검출을 위한 임계값
# - minRadius: 검출할 원의 최소 반지름

circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 0.5, 20, 50, 5)
print(circles.shape)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # 원 둘레에 초록색 원 그리기
        cv2.circle(img,(i[0], i[1]), i[2], (0, 255, 0), 2)
        # 원 중심점에 빨강색 원 그리기
        cv2.circle(img, (i[0], i[1]), 2, (0,0,255), 5)

# 결과 출력
cv2.imshow('blur', blur)
cv2.imshow('hough circle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()