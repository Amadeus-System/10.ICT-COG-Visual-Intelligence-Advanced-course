# blend two images with various weights

import cv2

img0 = cv2.imread('image/add1.jpg', cv2.IMREAD_COLOR)
img1 = cv2.imread('image/add2.jpg', cv2.IMREAD_COLOR)

cv2.imshow('img0', img0)
cv2.imshow('img1', img1)
cv2.waitKey()

num_images = 100

for i in range(9999):
	# alpha

	# i = 0, (0 % 5) / (5-1) -> 0/4 -> 0
	# i = 1, (1 % 5) / (5-1) -> 1/4 -> 0.25
	# i = 2, (2 % 5) / (5-1) -> 2/4 -> 0.5
	# i = 3, (3 % 5) / (5-1) -> 3/4 -> 0.75
	# i = 4, (4 % 5) / (5-1) -> 4/4 -> 1

	# i = 5, (5 % 5) / (5-1) -> 0/4 -> 0
	w0 = (i%num_images)/(num_images-1)
	# beta or 1-alpha
	w1 = 1 - w0
	# addWeighted(src1, w, src2, 1-w, bias): w*s1+(1-w)*s2 + b
	img = cv2.addWeighted(img0, w0, img1, w1, 0)
	cv2.imshow("img", img)
	if cv2.waitKey(30) == 27:
		break

cv2.destroyAllWindows()