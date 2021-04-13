# bgr->rgb using slicing [start:stop:step]

# cv2 read 3 channels with sequence of BGR
import cv2

# matplotlib read 3 channels with sequence of RGB
from matplotlib import pyplot as plt

img = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)

# cv2: bgr format, but plt: rgb format
# plt.imshow(img, interpolation = 'bicubic')
plt.imshow(img[:,:,::-1], interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
# ESC will quit the program