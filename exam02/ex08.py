#ex08.py
# 1. OpenCV 라이브러리를 import 하세요.
import cv2  # 답: cv2

# 2. "apple.jpg" 이미지를 불러와 'image' 변수에 저장하세요.
image = cv2.imread('apple.jpg')  # 답: imread

# 3. 이미지를 그레이스케일로 변환하여 'gray_image' 변수에 저장하세요.
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 답: cvtColor

# 4. 캐니 엣지 디텍션을 적용하여 'edges' 변수에 저장하세요. 임계값은 100과 200을 사용하세요.
edges = cv2.Canny(gray_image, 100, 200)  # 답: Canny

# 5. 원본 이미지와 엣지 검출된 이미지를 각각 화면에 표시하세요.
cv2.imshow('Original Image', image)  # 답: image
cv2.imshow('Canny Edges', edges)  # 답: edges

# 6. 키보드 입력을 기다리는 함수를 작성하세요.
cv2.waitKey(0)  # 답: waitKey

# 7. 모든 OpenCV 창을 닫는 함수를 작성하세요.
cv2.destroyAllWindows()  # 답: destroyAllWindows

