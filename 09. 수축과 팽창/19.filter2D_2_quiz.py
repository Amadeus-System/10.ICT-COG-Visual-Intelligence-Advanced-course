# [Quiz] 아래와 같이 kernel3/4가 있을 때 어떤 결과가 나타나는 지 확인해보자.
# kernel3 = np.array([[ 0,  0,  0],
#                     [ 0,  1,  0],
#                     [-1,  0,  0]])
# kernel4 = np.array([[ 0,  0,  0],
#                     [ 0,  1,  0],
#                     [ 0,  0, -1]])

import cv2 as cv
import numpy as np

img = cv.imread('image/edge_test.jpg', cv.IMREAD_GRAYSCALE)

# 전진 미분
# 왼쪽 위에서 오른쪽 아래 방향으로의 변화를 감지 - 주름 정보가 사라고, 잎 줄기를 잘 감지
kernel1 = np.array([[-1,  0,  0],
                    [ 0,  1,  0],
                    [ 0,  0,  0]])
# 오른쪽 위에서 왼쪽 아래 방향으로의 변화를 감지 - 주름 정보를 감지하고, 잎 줄기를 정보가 사라짐
kernel2 = np.array([[ 0,  0, -1],
                    [ 0,  1,  0],
                    [ 0,  0,  0]])

# 후진미분 = 전진과 같이 하나의 엣지를 하나로 검출
kernel3 = np.array([[ 0,  0,  0],
                    [ 0,  1,  0],
                    [ 0,  0, -1]])
kernel4 = np.array([[ 0,  0,  0],
                    [ 0,  1,  0],
                    [-1,  0,  0]])

# 중간미분 : 미분 공식에 의해 2로 나눠야하며,
# - 그렇지 않은 경우 하나의 엣지를 두꺼운 두개의 엣지로 검출
kernel5 = .5*np.array([[ 1,  0,  0],
                    [ 0,  0,  0],
                    [ 0,  0, -1]])
kernel6 = .5*np.array([[ 0,  0,  1],
                    [ 0,  0,  0],
                    [-1,  0,  0]])

dst1 = cv.filter2D(img, cv.CV_32F, kernel1) # 음수가 나올 수 있으므로 실수형으로 계산
dst2 = cv.filter2D(img, cv.CV_32F, kernel2)
dst3 = cv.filter2D(img, cv.CV_32F, kernel3)
dst4 = cv.filter2D(img, cv.CV_32F, kernel4)
dst5 = cv.filter2D(img, cv.CV_32F, kernel5)
dst6 = cv.filter2D(img, cv.CV_32F, kernel6)

# cv2.magnitude(a, b) : return np.sqrt(a**2, b**2)
dst12 = cv.magnitude(dst1, dst2) # 두방향으로 검출된 에지의 L2 similarity. 적절한 검출
dst34 = cv.magnitude(dst3, dst4)
dst56 = cv.magnitude(dst5, dst6)

# 전진미분, 후진미분, 중간미분 : 결과는 유사하다.
cv.imshow('img', img)
cv.imshow('dst1', np.abs(dst1).astype(np.uint8)) # 절대값 변환후 8 bit로 형변환
cv.imshow('dst2', np.abs(dst2).astype(np.uint8))
cv.imshow('dst12', dst12.astype(np.uint8))
cv.imshow('dst3', np.abs(dst3).astype(np.uint8))
cv.imshow('dst4', np.abs(dst4).astype(np.uint8))
cv.imshow('dst34', dst34.astype(np.uint8))
cv.imshow('dst5', np.abs(dst5).astype(np.uint8))
cv.imshow('dst6', np.abs(dst6).astype(np.uint8))
cv.imshow('dst56', dst56.astype(np.uint8))
cv.waitKey()