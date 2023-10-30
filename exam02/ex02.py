#ex02.py
import cv2

def draw_rectangle(image, top_left, bottom_right, color, thickness):
    # 빈칸: 사각형을 그리는 코드를 작성하세요.
    cv2.rectangle(image, top_left, bottom_right, color, thickness)

# 이미지 불러오기
image = cv2.imread('example.jpg')

# 사각형 그리기
draw_rectangle(image, (50, 50), (200, 200), (0, 255, 0), 5)

# 이미지 출력
cv2.imshow('Rectangle on Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()