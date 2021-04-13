#-*- coding:utf-8 -*-
import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

# Create named window for display the img.
cv2.namedWindow('img')
cv2.moveWindow('img', 0, 0)
cv2.waitKey()
cv2.imshow('img', img)
cv2.waitKey()
cv2.moveWindow('img', 400, 400)
cv2.waitKey()
cv2.destroyAllWindows()

## - cv2.namedWindow Flags
# WINDOW_NORMAL : the user can resize the window (no constraint).
# WINDOW_AUTOSIZE : the window size is automatically adjusted to the image 
# - you cannot change the window size manually.
# WINDOW_OPENGL : the window will be created with OpenGL support.

cv2.namedWindow('img-autosize', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('img-normal', cv2.WINDOW_NORMAL)
cv2.imshow('img-autosize', img)
cv2.imshow('img-normal', img)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.namedWindow('img-autosize', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('img-normal', cv2.WINDOW_NORMAL)
cv2.resizeWindow('img-autosize', 1000, 1000)
cv2.resizeWindow('img-normal', 500, 500)
cv2.imshow('img-autosize', img)
cv2.imshow('img-normal', img)
cv2.waitKey()
cv2.destroyAllWindows()