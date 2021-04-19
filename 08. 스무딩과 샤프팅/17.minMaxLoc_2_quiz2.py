# 컬러 src에서 (7,7) 필터 내에 min값 max값으로 이미지 변환.
# [Quiz] HSV 공간에서, V의 FS=5, H,S에 대한 FS는 3, 5, 7 등으로 변환해서 비교해보자.

import cv2 as cv
import numpy as np

KERNEL_SIZE = 5

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

# color 이미지에 대해 밝기(V) 정보에 대해 H,S를 튜닝하는 minMaxFiltering
def minMaxFilterHSV(img, kernel_size, flag):

	if len(img.shape) == 2:
		return minMaxFilterGray(img, kernel_size, flag)

	HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
	H, S, V = cv.split(HSV)
	Vfiltered = minMaxFilterGray(V, kernel_size, flag)

	tuning_IMGs = []
	for ks in [kernel_size-2, kernel_size, kernel_size+2]:
		Hfiltered = minMaxFilterGray(H, ks, flag)
		Sfiltered = minMaxFilterGray(S, ks, flag)
		HSVfiltered = cv.merge((Hfiltered, Sfiltered, Vfiltered))
		tuning_IMGs.append(cv.cvtColor(HSVfiltered, cv.COLOR_HSV2BGR))

	return tuning_IMGs


img = cv.imread('image/min_max.jpg', cv.IMREAD_COLOR)
minFiltered = minMaxFilter(img, KERNEL_SIZE, 0) # min filter
maxFiltered = minMaxFilter(img, KERNEL_SIZE, 1) # max filter

minFilteredBGR = minMaxFilterBGR(img, KERNEL_SIZE, 0) # min filter
maxFilteredBGR = minMaxFilterBGR(img, KERNEL_SIZE, 1) # max filter

minFilteredHSVs = minMaxFilterHSV(img, KERNEL_SIZE, 0) # min filter
maxFilteredHSVs = minMaxFilterHSV(img, KERNEL_SIZE, 1) # max filter

cv.imshow('img', img)
cv.imshow('minFiltered', minFiltered)
cv.imshow('maxFiltered', maxFiltered)
cv.imshow('minFilteredBGR', minFilteredBGR)
cv.imshow('maxFilteredBGR', maxFilteredBGR)
for i, (minHSVFiltered, maxHSVFiltered) in enumerate(zip(minFilteredHSVs,
														 maxFilteredHSVs)):
	MinwindowName = 'minFiltered HSV with %d' %(3 + 2*i)
	MaxwindowName = 'maxFiltered HSV with %d' %(3 + 2*i)
	cv.imshow(MinwindowName, minHSVFiltered)
	cv.imshow(MaxwindowName, maxHSVFiltered)

cv.waitKey()