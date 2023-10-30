 #ex03.py

import cv2

def flip_image(image, flip_code):
    flipped_image = cv2.flip(image, flip_code)
    return flipped_image

# 이미지 불러오기
image = cv2.imread('apple.jpg')

# 이미지 뒤집기
flipped = flip_image(image, 1)

# 이미지 출력
cv2.imshow('Flipped Image', flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()