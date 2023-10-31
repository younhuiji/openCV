#하얀색 사각형이 있는 검은색 배경에 대한 거리 변환을 해보자.
import cv2
import numpy as np
import matplotlib.pyplot as plt
'''
1. 객체 내부에서 거리 계산시 유용 
2. 이진 이미지에서 각 픽셀의 값이 0인 위치로 부터 가장 가까운 픽셀의 값이 255인 위치까지의 거리를 계산
3. 거리 변환의 결과는 원본 이진 이미지에서 각 픽셀이 '1' (또는 255, 흰색)로부터 얼마나 떨어져 있는 지를 나타냄

모든 픽셀에 대해 이웃하는 픽셀의 거리값과 자신과의 거리를 더한 값을 비교해서 더 작은 값으로 업데이트 한다.
1.9100037 중심값
'''
#1. 검은색 배경에 힌색 사각형
image  = np.zeros((5,5), dtype= np.uint8)
image[1:4, 1:4] = 255

# 이진화
_, binary_img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 거리 변환 적용  : 가장 가까운 배경 픽셀의 거리를 계산
dist_transform = cv2.distanceTransform(binary_img, cv2.DIST_L2, 3)
normalized = cv2.normalize(dist_transform, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
print(image)
print(dist_transform )
print(normalized)