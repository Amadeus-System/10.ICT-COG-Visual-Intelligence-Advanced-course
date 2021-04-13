import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

# create window with WINDOW_AUTOSIZE
cv2.imshow('img', img)
cv2.imshow('img2', img)

print(img.shape)
# milisecond delay. <= 0 infinitely delay.
cv2.waitKey(1000)

# Just img2 window is closed
cv2.destroyWindow('img2')
cv2.waitKey(0)

# all windows is closed
cv2.destroyAllWindows()

# [Quiz] image 폴더에 있는 min_max.jpg 파일을
# 1. 흑백영상으로 읽고
# 2. 그 shape을 출력하고
# 3. 그 이미지를 IMG 창에 출력한다.
# 4. 이미지에서 20 ~ 40 색인의 height와 width 값을 0으로 변경한 배열을 img2로 하고
# 5. img2 배열을 IMG2 창에 출력한다.