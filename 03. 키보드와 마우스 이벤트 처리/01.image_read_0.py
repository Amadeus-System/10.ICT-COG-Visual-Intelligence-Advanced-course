import cv2

# bmp, jpg, jp2, png, pbm, tif, gif
img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

# shape = (360, 480, 3)
print('img.shape, img.dtype =', img.shape, img.dtype)
# print(img[12:24, 12:24, 1]) : 0 ~ 255 값을 갖는다.
print(img[12:14, 12:14, :])

# img.shape = (height, width, channel)
# - channel : (R, G, B) @ matplotlib, PIL
# - channel : (B, G, R) @ matplotlib, PIL