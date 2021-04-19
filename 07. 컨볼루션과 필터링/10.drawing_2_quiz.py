# y can change mode 1:line, 2:rectangle, 3:circle, 4:free

# [Quiz] 위 코드에서:
# 1. r, g, b, y, p, s를 입력받으면 red, green, blue, yellow, purple, sky로 색을 바꾼다.
#  - 바귄 색은 모든 draw 객체에 적용된다.
# 2. f, l으로 누르면 다각형을 채우고, l을 누르면 thickness를 2로 적용한다.
# - 단, 자유형인 경우는 예외로 한다.
# 3. 방향키가 눌려진 경우, 마지막 draw를 방향키의 방향으로 이동시킨다.
# - 단, 자유형인 경우는 예외로 한다.

import cv2
import numpy as np

x0, y0, x, y, event = 0, 0, 0, 0, 0
draw = False
mode = 1
current = np.zeros((480, 640, 3), np.uint8)  # currently update image
commit = np.copy(current)                    # last update image
cancel = np.copy(current)                    # image canceled that is not updated to last changed of commit

arrowL = 2424832
arrowR = 2555904
arrowU = 2490368
arrowD = 2621440

cols = {}
colvecs = [0, 0, 0]
for i, c in enumerate(list("bgrsyp")):
    cvs = colvecs.copy()
    u, v = i%3, i//3
    cvs[u] += 255
    cols[c] = cvs
    if v > 0:
        cols[c][(u+v)%3] += 255

print(cols)
cur = 'y'
print(cols[cur])

thick= {}
thick['f'], thick['l'] = -1, 2
thickness = 'l'
print(thick[thickness])


def on_mouse(e, X, Y, flags=0, param=0):
    global x0, y0, draw, mode, current, commit, cancel, event, x , y
    event = e

    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        x0, y0 = X, Y
        # np.copyto(cancel, current)  # cancellation is impossible
        # np.copyto(cancel, commit)
    elif draw and event == cv2.EVENT_MOUSEMOVE:
        if mode < 4:
            np.copyto(current, commit)
            x, y = X, Y
        if mode == 1:
            cv2.line(current, (x0, y0), (x, y), cols[cur], thick[thickness])
        elif mode == 2:
            cv2.rectangle(current, (x0, y0), (x, y), cols[cur], thick[thickness])
        elif mode == 3:
            r = np.sqrt((x-x0)*(x-x0) + (y-y0)*(y-y0))
            cv2.circle(current, (x0, y0), int(r), cols[cur], thick[thickness])
        elif mode == 4:
            x, y = X, Y
            cv2.line(current, (x0, y0), (x, y), cols[cur], 2)
            x0, y0 = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        np.copyto(cancel, commit)
        np.copyto(commit, current)


cv2.namedWindow('img')
cv2.setMouseCallback('img', on_mouse)

# arrow key에 대한 drow를 설정할 수 있어야 한다.
# event에 따른 x0,y0,x,y 값을 조절해야 한다.
while True:
    cv2.imshow('img', current)
    key = cv2.waitKeyEx(5)
    # If we solve this, then we solve every
    # - We need convert current to commit
    if key == arrowL:
        draw = True
        # We want to change current to cancel, so that
        # - current is changed with commit using on_mouse FT
        # - you must change commit to cancel.
        np.copyto(commit, cancel)
        # cv2.imshow('cenceled', commit)
        # cv2.waitKey(-1)
        x0 -= 1

        on_mouse(cv2.EVENT_MOUSEMOVE, x-1, y)
        # np.copyto(cancel, commit)
        np.copyto(commit, current)
        draw = False
    elif key == arrowR:
        draw = True
        np.copyto(commit, cancel)
        x0 = x0 + 1
        on_mouse(cv2.EVENT_MOUSEMOVE, x+1, y)
        np.copyto(commit, current)
        draw = False
    elif key == arrowU:
        draw = True
        np.copyto(commit, cancel)
        y0 = y0 - 1
        on_mouse(event, x, y-1)
        np.copyto(commit, current)
        draw = False
    elif key == arrowD:
        draw = True
        np.copyto(commit, cancel)
        y0 = y0 + 1
        on_mouse(event, x, y+1)
        np.copyto(commit, current)
        draw = False
    elif key > 48 and key < 53: mode = key - 48
    elif (key < 128) and (key > -1):
        if chr(key) in list("bgrsyp"):
            cur = chr(key)
        elif chr(key) in list("fl"):
            thickness = chr(key)
        elif key == 27: break

cv2.destroyAllWindows()