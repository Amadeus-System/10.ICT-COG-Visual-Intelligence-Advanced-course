## confirm key code at windows platform.
# - LSB: Least Significant Byte
import cv2

img = cv2.imread('image/cat.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('cat', img)

while True:
    res = cv2.waitKeyEx(0)
    print('You pressed %d (0x%x), LSB: %d (%s)' % (res, res, res % 256,
        repr(chr(res%256)) if res%256 < 128 else '?'))
    
    if res == 27: break

cv2.destroyAllWindows()