# Simulate paint rectangle drawing

import cv2
import numpy as np

x0, y0 = 0, 0
draw = False
old = np.zeros((480,640,3), np.uint8)
new = np.copy(old)


def on_mouse(event, x, y, flags, param):
	global x0, y0, old, draw

	if event == cv2.EVENT_LBUTTONDOWN:
		draw = True
		x0, y0 = x, y
	elif draw and event == cv2.EVENT_MOUSEMOVE:
		np.copyto(new, old)
		cv2.rectangle(new, (x0,y0), (x,y), (0,255,0), 2)
	elif event == cv2.EVENT_LBUTTONUP:
		draw = False
		np.copyto(old, new)


cv2.namedWindow('img')
cv2.setMouseCallback('img', on_mouse)

while True:
	cv2.imshow('img', new)
	key = cv2.waitKey(30)
	if key == 27: break