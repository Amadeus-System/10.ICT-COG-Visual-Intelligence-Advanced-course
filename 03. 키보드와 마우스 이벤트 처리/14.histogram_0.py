import cv2
from matplotlib import pyplot as plt

img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)

print('img:', img.shape, img.dtype)
print('img.ravel()', img.ravel().shape, img.ravel().dtype)

# pyplot 을 사용한 히스토그램
plt.hist(img.ravel(), 256, [0,256]) # 256개의 상자, [0,256] 값에 대해서 계산
plt.xlim([0,256])
plt.show()

# 이미지의 0번째 채널을 256 개 상자를 사용하여 히스토그램 계산
hist = cv2.calcHist([img], [0], None, [256], [0,256])
print('hist :', hist.shape, hist.dtype)
plt.plot(hist)
plt.xlim([0,256])
plt.show()
