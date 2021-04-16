#-*- coding:utf-8 -*-
# https://opencv-python.readthedocs.io/en/latest/doc/03.drawShape/drawShape.html
# input 'r' then retangular, 'c' then circle with mouse LBUTTON

# [Quiz] 이전에는 마우스를 이동할 때 마다 그림을 그렸다.
# - 이 경우 우리가 원하는 크기를 확정하기 전에 미리 그림을 그리므로, 크기 조절이 어렵다.
# - 마우스를 움질일 때마다, 자유롭게 그 크기가 변경될 수 있도록 수정한다.
# - 단, 사격형은 내부를 채우지 말고, 두께 3을 사용하자.
# - [힌트] :
# -- 원본과 복사본을 두고
# # -- 마우스이동때마다, 원본으로 복사본을 복사하여 복사복에 그린다.
# # -- L 버튼 업할 때, 원본을 복사복으로 복사하여, 변경사항을 확정한다.


import cv2
import numpy as np
from math import sqrt

drawing = False     # Mouse LBUTOON DOWN state
mode = False        # True: Retangular, false: Circle
ix,iy = -1,-1


# Mouse Callback function
def draw_circle(event, x,y, flags, param):
    global ix,iy, drawing, mode, tmp, img
    dist = int(sqrt((x-ix)**2 + (y-iy)**2))

    if event == cv2.EVENT_LBUTTONDOWN: # LBOOTN DOWN state
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE: # Mouse Move
        if drawing == True:            # LBOOTN DOWN : Drawing start
            if mode == False:
                tmp = img.copy()
                cv2.circle(tmp, (ix,iy), dist, (0,255,0), -1)
            if mode == True:
                tmp = img.copy()
                cv2.rectangle(tmp, (ix,iy), (x,y), (255, 0, 0), 3)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        img = tmp

img = np.zeros((512,512,3), np.uint8)
tmp = img.copy()

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', tmp)
    k = cv2.waitKey(1)

    if k == ord('r'):    # Mode change
        mode = True
    elif k == ord('c'):
        mode = False
    elif k == 27:        # esc to close
        break

cv2.destroyAllWindows()