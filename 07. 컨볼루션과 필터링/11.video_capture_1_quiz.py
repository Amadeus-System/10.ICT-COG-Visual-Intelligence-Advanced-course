# play video file
# [Quiz] 입력된 비디오로 부터 정상출력과 반전출력을 2개의 윈도우로 모두 출력하자.
# - 반전출력(255 - image)은 bitwise_not 연산을 수행한 결과

import cv2

capture = cv2.VideoCapture("capture.avi")
fps = capture.get(cv2.CAP_PROP_FPS)
print("fps = ", fps)
# delay time used to waitKey ESC
dt = int(1000./fps)
print("dt = ", dt)

while True:
    # ret = frame read ok? (bool)
    # frame: captured frame
    ret, frame = capture.read()
    if ret:
        cv2.imshow("frame", frame)
        cv2.imshow("inversed", 255 - frame)
        # cv2.imshow("inversed", cv2.bitwise_not(frame))
    # ret == False => break
    else:
        break
    # ESC break
    # delay time is equal to the frame interval
    if cv2.waitKey(dt) == 27:
        break

capture.release()
cv2.destroyAllWindows()