#-*- coding:utf-8 -*-
# https://opencv-python.readthedocs.io/en/latest/doc/03.drawShape/drawShape.html
# input 'r' then retangular, 'c' then circle with mouse LBUTTON

# [Quiz] 이전에는 마우스를 이동할 때 마다 그림을 그렸다.
# - 이 경우 우리가 원하는 크기를 확정하기 전에 미리 그림을 그리므로, 크기 조절이 어렵다.
# - 사각형의 경우, 사각형의 크기를 최종적으로 LBUTTONUP한 위치의 크기로 맞추어라.
# - 사격형은 내부를 채우지 말고, 두께 3을 사용하자.

import cv2
import numpy as np
from math import sqrt

drawing = False     # Mouse LBUTOON DOWN state
mode = False        # True: Retangular, false: Circle
ix,iy = -1,-1


# Mouse Callback function
def draw_circle(event, x,y, flags, param):
    global ix,iy, drawing, mode
    dist = int(sqrt((x-ix)**2 + (y-iy)**2))

    if event == cv2.EVENT_LBUTTONDOWN: # LBOOTN DOWN state
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE: # Mouse Move
        if drawing == True:            # LBOOTN DOWN : Drawing start
            if mode == False:
                # circle(img, center, radian, color, line-thickness)
                cv2.circle(img, (ix,iy), dist, (0,255,0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 3)
        drawing = False             # LBUTTON UP : drawing close.
        # if mode == True:
        #     cv2.rectangle(img, (ix,iy),(x,y), (255,0,0), -1)
        # else:
        #     cv2.circle(img, (ix,iy), dist, (0,255,0), -1)


img = np.zeros((512,512,3), np.uint8)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1)

    if k == ord('r'):    # Mode change
        mode = True
    elif k == ord('c'):
        mode = False
    elif k == 27:        # esc to close
        break

cv2.destroyAllWindows()