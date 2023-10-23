import cv2
import numpy as np

img = cv2.imread('../img/apple.jpg')

# 구조화 요소 커널, 사각형 (3x3) 생성
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# 침식 연산 적용 : 커널 내의 모든 픽셀이 1일때만 원본 이미지의 픽셀을 1로 설정하자.
# << 객체크기의 줄임, 작은 흰색의 노이즈 제거, 객체간의 간격을 확장 >>
erosion = cv2.erode(img, k) # 바이너리 이미지에 사용되는 메소드

# 결과 출력
merged = np.hstack((img, erosion))
cv2.imshow('Erode', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()