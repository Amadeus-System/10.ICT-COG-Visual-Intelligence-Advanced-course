# 흑백 src에서 (7,7) 필터 내에 min값 max값으로 dst 대체.
import cv2 as cv
import numpy as np

def minMaxFilterGray(img, kernel_size, flag):

	kh = kw = kernel_size  # 커널의 가로, 세로 크기
	kh2, kw2 = kh//2, kw//2

	dst = np.zeros(img.shape, img.dtype)

	# 모든 픽셀들을 방문하며 해당하는 결과값 계산
	for i in range(dst.shape[0]):      # 모든 행을 방문
		for j in range(dst.shape[1]):  # 모든 열을 방문
			# 해당 픽셀주위의 영역을 추출
			roi = img[max(i-kh2,0):i+kh2+1, max(j-kw2,0):j+kw2+1]
			minVal, maxVal, _, _ = cv.minMaxLoc(roi)
			if flag == 0:
				dst[i,j] = minVal
			else:
				dst[i,j] = maxVal

	return dst

img = cv.imread('image/min_max.jpg', cv.IMREAD_GRAYSCALE)
minFiltered = minMaxFilterGray(img, 7, 0) # min filter
maxFiltered = minMaxFilterGray(img, 7, 1) # max filter

cv.imshow('img', img)
cv.imshow('minFiltered', minFiltered)
cv.imshow('maxFiltered', maxFiltered)
cv.waitKey()
