# show for at most 3 secs and display key value

import cv2

img = cv2.imread('image/cat.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('img', img)
key = cv2.waitKey(0)
print('key =', key)       # key 값은 ASCII 코드값
print('key =', chr(key))

cv2.destroyAllWindows()

# [Quiz] 입력된 키보드 값을 문자로 출력하고, ESC인 경우, 프로그램이 종료되도록 한다.