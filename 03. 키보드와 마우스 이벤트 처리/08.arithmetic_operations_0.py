# -*- coding: utf-8 -*-
# https://opencv-python.readthedocs.io/en/latest/doc/07.imageArithmetic/imageArithmetic.html
# prefer with jupyter notebook.
import cv2
import numpy as np

# naming method according to opencv c++ API
mat0 = np.uint8([[130,140],[150,160]])
mat1 = np.uint8([[100,100],[100,100]])
mat2 = np.uint8([[145,145],[145,145]])

print('mat0')
print(mat0)
print('mat1')
print(mat1)
print('mat2')
print(mat2)

# when using numpy.uint8 type, if result is over 255, then trivial value is return
## - overflow example : 대수값 - 256이 저장됨
print('mat0 + mat1')
print( mat0 + mat1 )

# cv2.add is type-safty addition. 259 -> 255 : bound to 255
print('cv2.add(mat0, mat1)')
print(cv2.add(mat0, mat1))

## - underflow example : 대수값 + 256이 저장됨
print('mat0 - mat2')
print( mat0 - mat2 )

# cv2.subtract is type-safty addition. 241 -> 0
print('cv2.subtract(mat0, mat2)')
print( cv2.subtract(mat0, mat2) )

# weighted addition, weighted subtract
print('cv2.addWeighted(mat0, 0.7, mat1, 0.3, 0)')
print( cv2.addWeighted(mat0, 0.7, mat1, 0.3, 0) )