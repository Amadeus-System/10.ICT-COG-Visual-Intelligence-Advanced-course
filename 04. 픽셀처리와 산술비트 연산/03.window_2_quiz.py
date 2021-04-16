# control the window position with arrow keys using cv2.waitKeyEx
# [Quiz] 'img1', 'img2' 2개의 윈도우를 생성한다.
# 각각 위치를 (100, 100)   (400, 100)로 먼저 설정한다.
# 20ms를 대기하면서 key를 입력받는다.
# 1이면 img1을 이동할 준비를 한다.
# 2이면 img2를 이동할 준비를 한다.
# 그리고 화살표키를 입력받으면 그 만큼 10씩 이동한다.
# ESC 키를 만나면 종료한다.

import cv2

# platform dependent key code.
arrowL = 2424832
arrowR = 2555904
arrowU = 2490368
arrowD = 2621440
delta = 10
xpos1 = 100
ypos1 = 100
xpos2 = 700
ypos2 = 100

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

cv2.namedWindow('img1')
cv2.moveWindow('img1', xpos1, ypos1)
cv2.imshow('img1', img)
cv2.namedWindow('img2')
cv2.moveWindow('img2', xpos2, ypos2)
cv2.imshow('img2', img)
active = 'img1'
pos = {}
pos['img1'] = [xpos1, ypos1]
pos['img2'] = [xpos2, ypos2]

while True:
	cv2.moveWindow(active, *pos[active])
	cv2.imshow(active, img)
	key = cv2.waitKeyEx(30)

	if key == 27: break
	elif key == arrowL: pos[active][0] -= delta
	elif key == arrowR: pos[active][0] += delta
	elif key == arrowU: pos[active][1] -= delta
	elif key == arrowD: pos[active][1] += delta
	elif key == 49:
		active = 'img1'
		print('current active window is ' + active)
	elif key == 50:
		active = 'img2'
		print('current active window is ' + active)

cv2.destroyAllWindows()