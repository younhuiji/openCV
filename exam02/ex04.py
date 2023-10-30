# ex04.py
import cv2

def change_color_space(image, color_flag):
    converted_image = cv2.cvtColor(image, color_flag)
    return converted_image

# 이미지 불러오기
image = cv2.imread('apple.jpg')

# 색상 공간 변경
gray_image = change_color_space(image, cv2.COLOR_BGR2GRAY)

# 이미지 출력
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()