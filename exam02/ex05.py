# ex05.py

import cv2

def put_text_on_image(image, text, position, font, font_scale, color, thickness):
    cv2.putText(image, text, position, font, font_scale, color, thickness)

# 이미지 불러오기
image = cv2.imread('example.jpg')

# 텍스트 삽입
put_text_on_image(image, 'Hello', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# 이미지 출력
cv2.imshow('Text on Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
