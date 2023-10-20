# 이미지에서 특정 영역을 추출하거나 이미지를 다른 시점에서 보기 위한 함수
# 3x3 투영 행렬을 사용하여 점의 집합을 다른 투영으로 변환
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 불러오기
image = cv2.imread('../img/Lenna.png')

# 이미지가 제대로 불러와졌는지 확인
if image is None:
    print('Could not open or find the image.')
    exit()

# OpenCV는 BGR을 사용하므로 RGB로 변환
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 원본 이미지에 적용할 4개의 점 (왼쪽 상단, 오른쪽 상단, 왼쪽 하단, 오른쪽 하단)
pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])

# 결과 이미지에서 위의 4개의 점에 대응하는 점
pts2 = np.float32([[10, 100], [200, 50], [100, 250], [300, 200]])

# 투영 행렬 계산
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# 투영 변환 수행
result = cv2.warpPerspective(image, matrix, (450, 300))
result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

# Matplotlib를 사용하여 원본 이미지와 결과 이미지를 나란히 표시
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image_rgb)

plt.subplot(1, 2, 2)
plt.title("Perspective Transformation")
plt.imshow(result_rgb)

plt.show()

'''
투영변환 : 3D 객체에서 2D 표면에 표현할 대상을 변환할 때 사용 (직선 투영, 원근 투영_카메라 렌즈에서 이미지 생성하는 것)
1. 그래픽 3D 좌표를 2D로 변환할 때
2. 카메라에서 3D 재구성 할 때 : (카메라 3D를 2D의 이미지로 투영) + ovenCV = 재구성
    => 로봇공학, 의료이미징, 가상, 증강현실, 지리정보 시스템
3. 이미지 스티칭
4. AR : 가상 객체를 실제 객체에다가 놓을 때
5. 기하학 교정 : 이미지 왜곡 제거하거나 특정 투영을 이용해서 이미지 교정할 때

'''
