# [Quiz] h=480, w=640 size의 검은색 이미지에 본인의 이름을 하얀색으로 하여
# 이미지의 정중앙에 fontScale을 4로 하여 그려놓고,
# 본인의 이름을 감싸는 사각형을 그려서 채팅창에 올려두세요.

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# row = y = 480, column = 640 = x
img = np.zeros((480,640,3), np.uint8)
pImg = Image.fromarray(img)
draw = ImageDraw.Draw(pImg)

text = "권오성"
font = ImageFont.truetype("gulim.ttc", 50)
draw.text((240,210), text, font=font, fill=(255,255,255))
img = np.array(pImg)

cv2.rectangle(img, (220,190), (410,280), (0,255,255), 3)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

# [참고]
# 1. https://jvvp.tistory.com/1076
# 2. https://stackoverflow.com/questions/59008322/pillow-imagedraw-text-coordinates-to-center