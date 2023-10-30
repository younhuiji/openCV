# ex01.py

import cv2

# 이미지 불러오기
image = cv2.imread('apple.jpg')

# 이미지 출력
cv2.imshow('Example Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()