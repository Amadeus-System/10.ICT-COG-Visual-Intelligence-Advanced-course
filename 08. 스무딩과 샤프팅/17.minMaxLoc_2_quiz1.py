# 컬러 src에서 (7,7) 필터 내에 min값 max값으로 이미지 변환.
# [Quiz] BGR 체널 각각에 대해 minMaxFilterGray를 적용하여 merge한 후, hsvmerge와 비교해보자.

import cv2 as cv
import numpy as np

FILTER_SIZE = 7

def minMaxFilterGray(img, kernel_size, flag):

	kh = kw = kernel_size # 커널의 가로, 세로 크기
	kh2, kw2 = kh//2, kw//2

	dst = np.zeros(img.shape, img.dtype)

	#모든 픽셀들을 방문하며 해당하는 결과값 계산
	for i in range(dst.shape[0]): # 모든 행을 방문
		for j in range(dst.shape[1]): # 모든 열을 방문
			# 해당 픽셀주위의 영역을 추출
			roi = img[max(i-kh2,0):i+kh2+1, max(j-kw2,0):j+kw2+1]
			minVal, maxVal, _, _ = cv.minMaxLoc(roi)
			if flag == 0:
				dst[i,j] = minVal
			else:
				dst[i,j] = maxVal

	return dst

# color 이미지 각 채널에 대해 minMaxFiltering
def minMaxFilterBGR(img, kernel_size, flag):

	if len(img.shape) == 2:
		return minMaxFilterGray(img, kernel_size, flag)

	CHs = list(cv.split(img))
	for i, C in enumerate(CHs):
		filtered = minMaxFilterGray(C, kernel_size, flag)
		CHs[i] = filtered

	return cv.merge(CHs)

# color 이미지에 대해 밝기(V) 정보만을 minMaxFiltering
def minMaxFilter(img, kernel_size, flag):

	if len(img.shape) == 2:
		return minMaxFilterGray(img, kernel_size, flag)

	HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
	H, S, V = cv.split(HSV)
	Vfiltered = minMaxFilterGray(V, kernel_size, flag)
	HSVfiltered = cv.merge((H,S,Vfiltered))

	return cv.cvtColor(HSVfiltered, cv.COLOR_HSV2BGR)


img = cv.imread('image/min_max.jpg', cv.IMREAD_COLOR)
minFiltered = minMaxFilter(img, FILTER_SIZE, 0) # min filter
maxFiltered = minMaxFilter(img, FILTER_SIZE, 1) # max filter

minFilteredBGR = minMaxFilterBGR(img, FILTER_SIZE, 0) # min filter
maxFilteredBGR = minMaxFilterBGR(img, FILTER_SIZE, 1) # max filter

cv.imshow('img', img)
cv.imshow('minFiltered', minFiltered)
cv.imshow('maxFiltered', maxFiltered)
cv.imshow('minFilteredBGR', minFilteredBGR)
cv.imshow('maxFilteredBGR', maxFilteredBGR)
cv.waitKey()