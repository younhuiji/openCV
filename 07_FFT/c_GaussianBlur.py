import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지를 불러옵니다.
image = cv2.imread("kim.png", 0)  # 0은 grayscale로 읽어들입니다.


gaussian_blur1 = cv2.GaussianBlur(image, (5, 5), 1)
gaussian_blur2 = cv2.GaussianBlur(image, (5, 5), 30)

# 두 가우시안 블러 이미지의 차이를 구합니다 (Difference of Gaussians).
DoG = gaussian_blur2 - gaussian_blur1
print(DoG[350:400,400:450])

# <참고 자료> : https://docs.opencv.org/4.x/da/df5/tutorial_py_sift_intro.html
'''
# 결과를 하나의 그래프에 보여줍니다.
fig, axs = plt.subplots(1, 4, figsize=(20, 5))

# 원본 이미지
axs[0].imshow(image, cmap='gray')
axs[0].axis('off')
axs[0].set_title('Original Image')

# 첫 번째 가우시안 블러 이미지
axs[1].imshow(gaussian_blur1, cmap='gray')
axs[1].axis('off')
axs[1].set_title('Gaussian Blur 1')

# 두 번째 가우시안 블러 이미지
axs[2].imshow(gaussian_blur2, cmap='gray')
axs[2].axis('off')
axs[2].set_title('Gaussian Blur 2')

# Difference of Gaussians
axs[3].imshow(DoG, cmap='gray')
axs[3].axis('off')
axs[3].set_title('Difference of Gaussians')

plt.show()
'''