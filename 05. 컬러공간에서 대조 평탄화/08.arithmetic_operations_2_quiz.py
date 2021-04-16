# blend two images with various weights and moving

import cv2
import numpy as np

org = cv2.imread('image/cat.jpg', cv2.IMREAD_COLOR)
mov = cv2.imread('image/add2.jpg', cv2.IMREAD_COLOR)
print(org.shape)
print(mov.shape)
W = mov.shape[1]

# wt: weighted add factor, step: mov's sliding step,
# delta: wt's increment, turn: step's increment
wt, step, delta, turn = 0, 0, 1, 1

while True:
    step += turn
    wt += delta

    cat = org.copy()
    # cat[:, step:step+W] = cv2.addWeighted(cat[:, step:step+W], wt/100,
    #                                       mov, 1-wt/100, 0)

    # other solution
    roi = cat[:, step:step+W]
    cvt = cv2.addWeighted(roi, 1-wt/100, mov, wt/100, 0)
    np.copyto(roi, cvt)

    # wrong example
    # roi = cvt  # roi that refer to the View of cat, refer to cvt
    cv2.imshow('cvt', cat)

    if step == 120: turn = -1
    elif step == 0: turn = 1
    if wt == 100: delta = -1
    elif wt == 0: delta = 1

    if cv2.waitKey(100) == 27: break

cv2.destroyAllWindows()