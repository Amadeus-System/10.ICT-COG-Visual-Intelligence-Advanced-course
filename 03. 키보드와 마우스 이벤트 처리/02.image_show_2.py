# show image until 'esc' gets pressed

import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

# ASCII code 27 is mapping ESC key.
while True:
	cv2.imshow('img', img)
	key = cv2.waitKey(30)
	if key == 27: break

cv2.destroyAllWindows()