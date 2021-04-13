## cv2 EVENT
# https://opencv-python.readthedocs.io/en/latest/doc/04.drawWithMouse/drawWithMouse.html
# https://cinema4dr12.tistory.com/809

import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

# cv::MouseEventType, cv::MouseEventFlag
def on_mouse(event, x, y, flags, param):
	print(event, x, y, flags, param)


img = cv2.imread('image/cat.jpg', cv2.IMREAD_UNCHANGED)

cv2.namedWindow('img')
# Sensing MOUSE EVENT with option userdata
cv2.setMouseCallback('img', on_mouse)

cv2.imshow('img', img)

while True:
	key = cv2.waitKey()
	print(repr(chr(key%256)) if key%256 < 128 else '?')
	if key == 27: break

cv2.destroyAllWindows()