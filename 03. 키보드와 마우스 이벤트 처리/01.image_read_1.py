# read image as gray and show array info

import cv2
# IMREAD_UNCHANGED = -1, IMREAD_GRAYSCALE = 0, IMREAD_COLOR = 1(default)
img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)
# img: numpy.ndarray, it's value is in range(0, 256)
# - GRAYSCALE img has 1 channel. it's ndim = 2
# - COLOR img has 3 channel. it's ndim = 3

print('type(img) =', type(img))
print('img.shape, img.dtype =', img.shape, img.dtype)

# https://opencv-python.readthedocs.io/en/latest/doc/01.imageStart/imageStart.html