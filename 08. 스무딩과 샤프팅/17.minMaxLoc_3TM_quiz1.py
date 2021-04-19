# [Quiz 1] hats_small.png 파일에서 템플릿 매칭을 수행하자.
import cv2

# 1. View original image
TARGET = "image/hats_small.png"
src = cv2.imread(TARGET)
templit = cv2.imread("image/hat.png")

cv2.imshow("hats", src)
cv2.imshow("hst", templit)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. open image for templete matching
src = cv2.imread(TARGET, cv2.IMREAD_GRAYSCALE)
templit = cv2.imread("image/hat.png", cv2.IMREAD_GRAYSCALE)

# - for output of templete matching
dst = cv2.imread(TARGET)

# 3. search templete image
# cv2.matchTemplate(img, template, method)
# - method: 탐색방법
# --- TM_SQDIFF, TM_SQDIFF_NORMED는 최소값이 유사, 그 이외는 최대값이 유사
# --- CV_TM_CCORR, CV_TM_CCORR_NORMED : 상관관계를 이용한 유사도
# --- CV_TM_CCOEFF, CV_TM_CCOEFF_NORMED : 상관계수를 이용한 유사도
# --- result.shape = (W-w+1, H-h+1) : template 필터 공간에서의 유사도값

# --- templit의 크기를 줄여가며 matching한다.
print("src shape : ", src.shape)
best = {}
minLocs, minVals, tmpl_hws = [], [], []
MINVAL = 1
resizeFactors = [round(j*0.1, 1) for j in range(10, 0, -1)]
for rs in resizeFactors:
    print(f"templit is resized with {int(rs*100)} %")
    resized = cv2.resize(templit, dsize=(0, 0), fx=rs, fy=rs, interpolation=cv2.INTER_AREA)
    res = cv2.matchTemplate(src, resized, cv2.TM_SQDIFF_NORMED)
    print("templit shape : ", resized.shape)
    print("result shape : ", res.shape)

    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)
    minVals.append(minVal)
    minLocs.append(minLoc)
    tmpl_hws.append(resized.shape[:2])

    x, y = minLoc
    h, w = resized.shape
    cv2.rectangle(dst, (x, y), (x + w, y + h), (255, 0, 0), 1)
    cv2.putText(dst, str(rs), (x, max(y-4, 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)

    if minVal < MINVAL:
        print(f"In now, best min value is {minVal} at {int(rs*100)}% resized templit")
        best['minVal'] = minVal
        best['minLoc'] = minLoc
        best['hw'] = resized.shape[:2]
        best['result'] = res
        best['resizeRate'] = rs
        MINVAL = minVal

print(best)
x, y = best['minLoc']
h, w = best['hw']

# best 매칭 이미지 localization
dst = cv2.rectangle(dst, (x, y), (x + w, y + h) , (0, 0, 255), 3)
cv2.putText(dst, str(best['resizeRate']), (x, max(y-4, 4)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

cv2.imshow("rst", best['result'])
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()