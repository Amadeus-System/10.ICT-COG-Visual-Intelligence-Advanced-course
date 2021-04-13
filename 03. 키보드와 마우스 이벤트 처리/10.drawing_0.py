# https://opencv-python.readthedocs.io/en/latest/doc/03.drawShape/drawShape.html

import cv2
import numpy as np

# row = y = 480, column = 640 = x
img = np.zeros((480,640,3), np.uint8)

# from (x1, y1) to (x2, y2) 
cv2.line(img, (20,20), (620,460), (0,255,0), 3)
# cv2.rectangle(img, start, end, color, thickness) : negative thickness fill the region
# - if thickness == -1, fill inner space with color
cv2.rectangle(img, (100,100), (400,400), (0,0,255), 3)
cv2.rectangle(img, (500,100), (600,200), (255,0,0), -1)

# center circle with b and r
cv2.circle(img, (320,240), 100, (255,255,0), 3)

# cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]) → img
# - axes : long axis distance, short axis distance
# - angle : clock-wise rotate angle
cv2.ellipse(img, (320,240), (300,200), 10, 0, 360, (0,255,255), 3)

# cv2.polylines(img, pts, isClosed, color, thickness) => purple unfilled polygon
# - pts: list of array that vertex is connected
pts = np.array([[50,150], [200,80], [350,120], [300,200]], np.int32)
cv2.polylines(img, [pts.reshape((-1,2))], True, (255,0,255), 3)

# cv2.fillPoly(img, pts, color[, lineType[, shift[, offset]]]) → img
pts = np.array([[350,350], [500,280], [630,320], [520,320]], np.int32)
cv2.fillPoly(img, [pts.reshape((-1,2))], (0,0,255))

# cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) → None
# - write text starting with org(x, y) at img using fontFace, fontscale
cv2.putText(img, 'Hello', (10,450), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 3)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

# [Quiz] h=480, w=640 size의 검은색 이미지에 본인의 이름을 하얀색으로 하여
# 이미지의 정중앙에 fontScale을 4로 하여 그려놓고,
# 보인의 이름을 감싸는 사각형을 그려서 채팅창에 올려두세요.
