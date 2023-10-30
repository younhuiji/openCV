# ex10.py
'''
10 . 해리스 코너를 찾기 위한 코드를 완성하는 문제입니다.이 코드를 실행하면 "apple.jpg" 이미지에 대한 해리스 코너를 찾고, 코너가 있는 부분을 빨간색으로 표시하여 화면에 출력합니다.
'''
# 1. 필요한 라이브러리를 import 하세요.
import cv2  # 답: cv2
import numpy as np  # 답: numpy

# 2. 'apple.jpg' 이미지를 불러와 'image' 변수에 저장하세요.
image = cv2.imread('apple.jpg')  # 답: imread

# 3. 이미지를 그레이스케일로 변환하여 'gray_image' 변수에 저장하세요.
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 답: cvtColor

# 4. 그레이스케일 이미지를 float32 타입으로 변환하세요.
gray_image = np.float32(gray_image)  # 답: float32

# 5. cv2.cornerHarris() 함수를 사용해 'dst' 변수에 해리스 코너 응답을 저장하세요.
dst = cv2.cornerHarris(gray_image, 2, 3, 0.04)  # 답: cornerHarris

# 6. 해리스 코너 응답을 다듬기 위해 dilate 함수를 적용하세요.
dst = cv2.dilate(dst, None)  # 답: dilate

# 7. 코너 픽셀을 표시하기 위해 원본 이미지에서 코너 부분에 빨간색으로 표시하세요.
image[dst > 0.01 * dst.max()] = [0, 0, 255]

# 8. 이미지를 화면에 표시합니다.
cv2.imshow('Harris Corners', image)  # 답: imshow

# 9. 키보드 입력을 기다리는 함수를 작성하세요.
cv2.waitKey(0)  # 답: waitKey

# 10. 모든 OpenCV 창을 닫는 함수를 작성하세요.
cv2.destroyAllWindows()  # 답: destroyAllWindows
