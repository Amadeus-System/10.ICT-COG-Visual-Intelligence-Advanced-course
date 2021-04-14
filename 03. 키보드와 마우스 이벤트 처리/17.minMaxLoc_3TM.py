# - 13.1 템플릿 매칭 slide 활용
# resize : https://076923.github.io/posts/Python-opencv-8/
# template mating : https://076923.github.io/posts/Python-opencv-37/
# https://opencv-python.readthedocs.io/en/latest/doc/24.imageTemplateMatch/imageTemplateMatch.html
# - 일반적으로 영상의 밝기 등에 덜 민감해지도록 정규화과정을 거쳐 매칭한다.
# - 이미지의 스케일링에 대해 약하므로, templit을 다양한 size로 resize하여 여러번 수행할 수 있다.

import cv2

# 1. View original image
src = cv2.imread("image/hats.png")
src = cv2.resize(src, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
templit = cv2.imread("image/hat.png")

cv2.imshow("hats", src)
cv2.imshow("hst", templit)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. open image for templete matching
src = cv2.imread("image/hats.png", cv2.IMREAD_GRAYSCALE)
templit = cv2.imread("image/hat.png", cv2.IMREAD_GRAYSCALE)

# - for output of templete matching
dst = cv2.imread("image/hats.png")

# 3. search templete image
# cv2.matchTemplate(img, template, method)
# - img: 원본이미지
# - template: 원본이미지에서 탐색할 이미지
# - method: 탐색방법
# - GrayScale image 리턴 : 원본의 픽셀이 템플릿 이미지와 유사한 정도
# --- TM_SQDIFF, TM_SQDIFF_NORMED는 최소값이 유사, 그 이외는 최대값이 유사
# --- CV_TM_CCORR, CV_TM_CCORR_NORMED : 상관관계를 이용한 유사도
# --- CV_TM_CCOEFF, CV_TM_CCOEFF_NORMED : 상관계수를 이용한 유사도
# --- result.shape = (W-w+1, H-h+1) : template 필터 공간에서의 유사도값
# --- src.shape = (H, W), temp.shape = (h, w)
result = cv2.matchTemplate(src, templit, cv2.TM_SQDIFF_NORMED)
print("src shape : ", src.shape)
print("templit shape : ", templit.shape)
print("result shape : ", result.shape)

# TM_SQDIFF_NORMED에서는 최소값이 유사하므로, 최소값 위치 찾기
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
x, y = minLoc
h, w = templit.shape

# - 매칭 이미지 localization
dst = cv2.rectangle(dst, (x, y), (x + w, y + h) , (0, 0, 255), 1)

# - 이미지 축소를 위한 resize
hH, hW = dst.shape[0] // 2, dst.shape[1] // 2
dst = cv2.resize(dst, dsize=(hW, hH), interpolation=cv2.INTER_CUBIC)
# dst = cv2.resize(dst, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
print(dst.shape)

# - 가장 어두운 위치가 매칭되는 박스의 좌상단 모서리
result = cv2.resize(result, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imshow("rst", result)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# [Quiz 1] hats_small.png 파일에서 템플릿 매칭을 수행하자.
# [Quiz 2] hats_smallDim.png 파일에서 템플릿 매칭을 수행하자.
# [Quiz 3] hats_smallDimInverse.png 파일에서 템플릿 매칭을 수행하자.
# [Quiz 4] 3에서 TM_CCOEFF_NORMED를 사용할 때의 결과를 출력해보자. maxValue를 선택해야 한다.