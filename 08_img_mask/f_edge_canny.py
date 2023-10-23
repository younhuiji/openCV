import cv2, time
import numpy as np

img = cv2.imread("../img/Lenna.png")

# 케니 엣지 적용
# 100 이하의 픽셀은 엣지로 간주하지 않는다.
# 200 이상을 엣지로 간주한다.
#가우시안 블러  -> 케니엣지
edges = cv2.Canny(img,100,200) # 하위, 상위 임계값

# 결과 출력
cv2.imshow('Original', img)
cv2.imshow('Canny', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
