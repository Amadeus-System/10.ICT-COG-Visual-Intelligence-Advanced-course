# https://webnautes.tistory.com/1004
# https://076923.github.io/posts/Python-opencv-37/
# - template matching: 원본 이미지에서 템플릿 이미지와 일치하는 영역을 찾는 알고리즘
# - 원본 이미지 위에 템플릿 이미지를 놓고 조금씩 이동해가며 이미지 끝에 도달할 때 까지 찾는다.
# - 이 방식을 통해, 템플릿 이미지와 동일하거나, 가장 유사한 영역을 원본 이미지에서 검출

import cv2 as cv
import numpy as np

img = np.array([[2, 1, 3],
                [7, 5, 4]], np.uint8)

# cv2.minMaxLoc: GrayScale 이미지에서 최대최소값과 그 위치(x,y)를 반환
# - maxVal, minVal을 이용하는 것은 이미지를 변환할 때
# - minLoc, maxLoc을 이용하는 것은 이미지에서 탐색할 때
minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(img)

print('img')
print(img)
print('minVal minLoc =', minVal, minLoc)
print('maxVal maxLoc =', maxVal, maxLoc)

mask = np.array([[0, 1, 1],
                 [0, 1, 1]], np.uint8)

minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(img, mask=mask)

print('mask')
print(mask)
print('minVal minLoc =', minVal, minLoc)
print('maxVal maxLoc =', maxVal, maxLoc)