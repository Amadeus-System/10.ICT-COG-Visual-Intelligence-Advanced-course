# y can change mode 1:line, 2:rectangle, 3:circle, 4:free

import cv2
import numpy as np

x0, y0 = 0, 0
draw = False
mode = 1
img = np.zeros((480,640,3), np.uint8)
img0 = np.copy(img)

def on_mouse(event, x, y, flags, param):
	global x0, y0, draw, mode, img0, img

	if event == cv2.EVENT_LBUTTONDOWN:
		draw = True
		x0, y0 = x, y
	elif draw and event == cv2.EVENT_MOUSEMOVE:
		# np.copyto(dst, src)
		if mode < 4: np.copyto(img, img0)
		if mode == 1:
			cv2.line(img, (x0,y0), (x,y), (0,0,255), 2)
		elif mode == 2:
			cv2.rectangle(img, (x0,y0), (x,y), (0,255,0), 2)
		elif mode == 3:
			r = np.sqrt((x-x0)*(x-x0) + (y-y0)*(y-y0))
			cv2.circle(img, (x0,y0), int(r), (0,255,255), 2)
		elif mode == 4:
			cv2.line(img, (x0,y0), (x,y), (255,0,255), 2)
			x0, y0 = x, y
	elif event == cv2.EVENT_LBUTTONUP:
		draw = False
		np.copyto(img0, img)


cv2.namedWindow('img')
cv2.setMouseCallback('img', on_mouse)

while True:
	cv2.imshow('img', img)
	key = cv2.waitKey(5)
	if key > 48 and key < 53: mode = key - 48
	elif key == 27: break

cv2.destroyAllWindows()

# [Quiz] 위 코드에서:
# 1. r, g, b, y, p, s를 입력받으면 red, green, blue, yellow, purple, sky로 색을 바꾼다.
#  - 바귄 색은 모든 draw 객체에 적용된다.
# 2. f를 누르면 다각형을 채우고, l을 누르면 thickness를 2로 적용한다.
# - 단, 자유형인 경우는 예외로 한다.
# 3. 방향키가 눌려진 경우, 마지막 draw를 방향키의 방향으로 이동시킨다.