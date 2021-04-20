# [Quiz] filter size를 (0,0)두고, sigmaX, sigmaY의 값을 1 ~ 3로 trackbar를 이용하여 조절하자.
# - kernel size를 0으로 두면, sigma 값을 이용하여 자동으로 kernel size를 조정해준다.
# - sigma는 분산값이므로, float이다. 따라서, 실제 입력값의 최대값을 30으로 주는 것이 좋겠다.

import cv2 as cv

img = cv.imread('image/filter_blur.jpg')

init_sigX, init_sigY = 1, 1

def onChangeX(val):
    global init_sigX, init_sigY
    init_sigX = val/10
    img_blurred = cv.GaussianBlur(img, (0,0), sigmaX=init_sigX, sigmaY=init_sigY)
    cv.imshow('GaussianBlurred', img_blurred)


def onChangeY(val):
    global init_sigX, init_sigY
    init_sigY = val/10
    img_blurred = cv.GaussianBlur(img, (0,0), sigmaX=init_sigX, sigmaY=init_sigY)
    cv.imshow('GaussianBlurred', img_blurred)


cv.imshow('img', img)
cv.namedWindow('GaussianBlurred')
cv.imshow('GaussianBlurred', img)
cv.createTrackbar('sigX*10', 'GaussianBlurred', init_sigX, 30, onChangeX)
cv.createTrackbar('sigY*10', 'GaussianBlurred', init_sigY, 30, onChangeY)
cv.waitKey()
cv.destroyAllWindows()

