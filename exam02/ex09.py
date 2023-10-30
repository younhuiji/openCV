# ex09.py

# 1. OpenCV 라이브러리를 import 하세요.
import cv2  # 답: cv2

# 2. "apple.jpg" 이미지를 불러와 'image' 변수에 저장하세요.
image = cv2.imread('apple.jpg')  # 답: imread

# 3. 이미지를 그레이스케일로 변환하여 'gray_image' 변수에 저장하세요.
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 답: cvtColor

# 4. 바이너리 이미지로 변환합니다.
_, thresh = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)  # 답: threshold

# 5. 커널을 생성합니다. np.ones((5,5), np.uint8)을 사용하세요.
import numpy as np
kernel = np.ones((5,5), np.uint8)  # 답: np.ones

# 6. Dilation을 적용하여 'dilated' 변수에 저장하세요.
dilated = cv2.dilate(thresh, kernel, iterations=1)  # 답: dilate

# 7. 이미지를 화면에 표시합니다.
cv2.imshow('Dilated Image', dilated)  # 답: imshow

# 8. 키보드 입력을 기다리는 함수를 작성하세요.
cv2.waitKey(0)  # 답: waitKey

# 9. 모든 OpenCV 창을 닫는 함수를 작성하세요.
cv2.destroyAllWindows()  # 답: destroyAllWindows