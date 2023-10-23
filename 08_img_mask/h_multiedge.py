import cv2
import matplotlib.pyplot as plt
import numpy as np

# 이미지 로드
img = cv2.imread("../img/Lenna.png", cv2.IMREAD_GRAYSCALE)

# Sobel
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobel_x, sobel_y)

# Laplacian
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# Canny
canny = cv2.Canny(img, 50, 150)

# Prewitt
kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
kernely = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
prewitt = cv2.filter2D(img, -1, kernelx) + cv2.filter2D(img, -1, kernely)

# Scharr
scharr_x = cv2.Scharr(img, cv2.CV_64F, 1, 0)
scharr_y = cv2.Scharr(img, cv2.CV_64F, 0, 1)
scharr = cv2.magnitude(scharr_x, scharr_y)


titles = ['Original', 'Sobel', 'Laplacian', 'Canny', 'Prewitt', 'Scharr']
images = [img, sobel, laplacian, canny, prewitt, scharr]

plt.figure(figsize=(15,5))

for i in range(6):
    plt.subplot(1, 6, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()
