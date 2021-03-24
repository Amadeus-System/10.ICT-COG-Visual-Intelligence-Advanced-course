# [Quiz] cat.jpg 파일을 show하는 'img' 윈도우에서
# 1. Lbutton을 클릭하면 왼쪽으로 10 이동
# 2. Rbutton을 클릭하면 오른쪽으로 10 이동
# 3. SCROLL UP 위로 10 이동
# 4. SCROLL DOWN 아래와 10 이동


import cv2

delta = 10
xpos = 200
ypos = 200

def on_mouse(event, x, y, flags, param):
	global delta, xpos, ypos

	if event == cv2.EVENT_LBUTTONDOWN:
		print('Left mouse button down at', x, y)
	elif event == cv2.EVENT_LBUTTONUP:
		print('Left mouse button up at', x, y)
		xpos -= delta
		cv2.moveWindow('img', xpos, ypos)
	elif event == cv2.EVENT_RBUTTONDOWN:
		print('right mouse button down at', x, y)
	elif event == cv2.EVENT_RBUTTONUP:
		print('right mouse button up at', x, y)
		xpos += delta
		cv2.moveWindow('img', xpos, ypos)
	elif event == cv2.EVENT_LBUTTONDBLCLK:
		print('Left mouse button double clicked at', x, y)
	elif event == cv2.EVENT_RBUTTONDBLCLK:
		print('right mouse button double clicked at', x, y)
	elif event == cv2.EVENT_MOUSEWHEEL:
		if flags > 0:
			print('mouse wheel scrolled up at', x, y)
			ypos -= delta
			cv2.moveWindow('img', xpos, ypos)
		else:
			print('mouse wheel scrolled down at', x, y)
			ypos += delta
			cv2.moveWindow('img', xpos, ypos)


img = cv2.imread('image/cat.jpg', cv2.IMREAD_UNCHANGED)
cv2.namedWindow('img')
cv2.moveWindow('img', xpos, ypos)
cv2.imshow('img', img)

cv2.setMouseCallback('img', on_mouse)

while True:
	key = cv2.waitKey()
	if key == 27: break
cv2.destroyAllWindows()