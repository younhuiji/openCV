# ex07.py

import cv2

# 이미지 불러오기
image = cv2.imread('apple.jpg')

# 블러링 적용하기 (Gaussian Blur)
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# 원본 이미지와 블러링된 이미지를 화면에 표시
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)

# 키보드 입력을 기다린다.
cv2.waitKey(0)

# 모든 OpenCV 창을 닫는다.
cv2.destroyAllWindows()