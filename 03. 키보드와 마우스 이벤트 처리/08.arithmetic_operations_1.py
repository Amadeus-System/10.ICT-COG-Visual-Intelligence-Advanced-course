# add two images : 이미지 합성
import cv2

img1 = cv2.imread('image/add1.jpg', cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('image/add2.jpg', cv2.IMREAD_UNCHANGED)
print(10 // 3)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
# numpy addition generate trivial image - 1. astype(float) 2. op 3. astype(uint8)
cv2.imshow('numpy_+', img1 + img2)            # img1 + img2 == img1 + img2 - 256 @ UINT8
cv2.imshow('numpy_mean', (img1 + img2) // 2)

# cv2 add could generate reasonable image, but reduce information.
cv2.imshow('opencv_add', cv2.add(img1,img2))         # limit 255
# cv2.mean(img1) == img1.mean(axis=(0,1))
cv2.imshow('opencv_addm', cv2.add(img1,img2) // 2)

# very good operation
cv2.imshow('opencv_madd', cv2.add(img1//2,img2//2))
cv2.imshow('opencv_mwadd', cv2.addWeighted(img1, .5, img2, .5, 0))
cv2.imshow('numpy_madd', img1//2 + img2//2)

cv2.waitKey()
cv2.destroyAllWindows()
