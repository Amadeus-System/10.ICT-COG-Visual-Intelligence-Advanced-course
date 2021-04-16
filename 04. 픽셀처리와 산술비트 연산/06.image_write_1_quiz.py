# [Quiz] cat.jpg 파일을 읽고,
# cat 이미지보다 폭이 2배 넓은 이미지를 생성하고
# 1. 왼쪽에는 컬러이미지를 담고
# 2. 오른쪽에는 흑배이미지를 담아
# cat_colgray.jpg로 저장하자.

import cv2
import numpy as np

# col.shape = (h, w, 3), gray.shape = (h, w)
col = cv2.imread('cat.jpg')
gray = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)
h, w, c = col.shape

dst = np.zeros((h, w*2, c), dtype=np.uint8)
dst[:,:w], dst[:, w:] = col, gray.reshape((h,w,1))

cv2.imshow('dst',dst)
cv2.waitKey()

# using cv2.cvtColor(src, FLAGS)
dst2 = np.zeros((h,w*2,c), dtype=np.uint8)
dst2[:,:w], dst2[:, w:] = col, cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
cv2.imshow('dst2',dst2)
cv2.waitKey()

cv2.imwrite('cat_colgray.jpg', dst2)
cv2.destroyAllWindows()

