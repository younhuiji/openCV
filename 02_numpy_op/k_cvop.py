import cv2
import numpy as np
import matplotlib.pyplot as plt
## << 이미지 + <<사칙연산>> = 이미지의 명도 조정, 명암대비 변경

# 이미지 불러오기
img_road = cv2.imread('../img/apple.jpg')

# 컬러로 바꾼다. RGB -> BGR
img = cv2.cvtColor(img_road, cv2.COLOR_RGB2BGR)

# 각종 연산 수행
# 1) 이미지 + =  이미지가 밝아진다.
brighter_img = cv2.add(img, np.array([50.0]))

# 2) 이미지 - =  이미지가 어두워진다.
darker_img = cv2.subtract(img, np.array([50.0]))

# 3) 이미지 * =  명암 대비가 높아진다.
contrast_img = cv2.multiply(img, np.array([1.5]))

# 4) 이미지 / =  명암 대비가 낮아진다.
less_contrast_img = cv2.divide(img, np.array([1.5]))

# Matplotlib을 사용한 결과 표시
plt.figure(figsize=(12, 6))

plt.subplot(1, 5, 1)
plt.title('Original')
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 5, 2)
plt.title('Brighter')
plt.imshow(brighter_img, cmap='gray')
plt.axis('off')

plt.subplot(1, 5, 3)
plt.title('Darker')
plt.imshow(darker_img, cmap='gray')
plt.axis('off')

plt.subplot(1, 5, 4)
plt.title('More Contrast')
plt.imshow(contrast_img, cmap='gray')
plt.axis('off')

plt.subplot(1, 5, 5)
plt.title('Less Contrast')
plt.imshow(less_contrast_img, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
