# [Quiz] 작성한 이미지의 중심위치에서 반경 240인 원을 그린다.
# - 원의 내부색은
# - 파란색과 겹치는 부분은 보라색
# - 녹색과 겹치는 부분은 청록색
# - 빨간색과 겹치는 부분은 노란색
# 을 가지도록 설정하여, 그림을 그리고 출력합니다.

# 코드설계:
# 1. 원본 이미지를 생성
# 2. 색을 덜어낼 이미지2 생성
# 3. 이미지2에 하얀색 원을 그리고,
# 4. 덜어낼 영역에서 색을 빼주고
# 5. 음수 색을 0으로 변경한 후,
# 6. 두 이미지를 더한다.

import cv2
import numpy as np

h = 480
w = 640

img = np.zeros((h,w,3), dtype=np.uint8)
img[h*0//3:h*1//3, :] = (255,0,0)
img[h*1//3:h*2//3, :] = (0,255,0)
img[h*2//3:h*3//3, :] = (0,0,255)

img2 = np.zeros((h,w,3))
cv2.circle(img2, (320, 240), 240, (255, 255, 255), -1)
img2[:h*1//3, :] -= (255,255,0)
img2[h*1//3:h*2//3, :] -= (0,255,255)
img2[h*2//3:, :] -= (255,0,255)
img2[img2 < 0] = 0
img2 = img2.astype(np.uint8)

cv2.imshow('img1',img)
cv2.imshow('img2',img2)
cv2.waitKey()

dst = img + img2

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()