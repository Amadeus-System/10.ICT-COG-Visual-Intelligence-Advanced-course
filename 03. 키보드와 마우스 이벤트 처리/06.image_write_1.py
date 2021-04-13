# read color image as gray and save it as jpg

import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('img',img)
cv2.waitKey()

cv2.imwrite('img.jpg', img)
cv2.destroyAllWindows()

# [Quiz] cat.jpg 파일을 읽고,
# cat 이미지보다 폭이 2배 넓은 이미지를 생성하고
# 1. 왼쪽에는 컬러이미지를 담고
# 2. 오른쪽에는 흑배이미지를 담아
# cat_colgray.jpg로 저장하자.
