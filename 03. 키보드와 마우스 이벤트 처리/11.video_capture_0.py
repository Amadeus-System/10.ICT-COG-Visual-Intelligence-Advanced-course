# https://076923.github.io/posts/Python-opencv-4/
# https://thebook.io/006939/ch04/01/01-07/
import cv2

# video capture with video device 0
capture = cv2.VideoCapture(0)
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = capture.get(cv2.CAP_PROP_FPS)
print('width =', width)
print('height =', height)
print('fps =', fps)

# cv2.VideoWriter_fourcc(*'DX50'): Specify Video codec with 4 character code
# fourcc = cv2.VideoWriter_fourcc(*'DX50')
# fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# cv2.VideoWriter(outputFile, fourcc, frame, size)
writer = cv2.VideoWriter('capture.avi', fourcc, fps, (width, height))

while True:
    # ret: 잘 읽으면 True, 못 읽으면 False
    ret, frame = capture.read()
    cv2.imshow('divx_VIDEO', frame)
    writer.write(frame)

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

writer.release()
capture.release()
cv2.destroyAllWindows()