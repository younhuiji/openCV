import cv2
import numpy as np
from matplotlib import pyplot as plt

fig, axes = plt.subplots(2, 6, figsize=(24, 8))
axes = axes.ravel()

img = cv2.imread('coin.jpg', 0)
axes[0].imshow(img, cmap='gray')
axes[0].set_title('1. Original Image')

ret, bin_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
axes[1].imshow(bin_img, cmap='gray')
axes[1].set_title('2. OTSU Binary Image')

# 3. K-means Clustering using OpenCV
img_flatten = img.reshape((-1,1)).astype('float32')
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
_, labels, centers = cv2.kmeans(img_flatten, 2, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
labels_reshape = labels.reshape(img.shape)
kmeans_img = np.choose(labels_reshape, centers)
axes[2].imshow(kmeans_img, cmap='gray')
axes[2].set_title('3. K-means Clustering (OpenCV)')

kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(bin_img, cv2.MORPH_OPEN, kernel, iterations=2)
axes[3].imshow(opening, cmap='gray')
axes[3].set_title('4. Noise Removal')

sure_bg = cv2.dilate(opening, kernel, iterations=2)
axes[4].imshow(sure_bg, cmap='gray')
axes[4].set_title('5. Background Extraction')

dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
axes[5].imshow(dist_transform, cmap='gray')
axes[5].set_title('6. Distance Transform')

ret, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)
axes[6].imshow(sure_fg, cmap='gray')
axes[6].set_title('7. Foreground Extraction')

sure_fg = np.uint8(sure_fg)
res = cv2.subtract(sure_bg, sure_fg)
axes[7].imshow(res, cmap='gray')
axes[7].set_title('8. Unknown Region')

ret, markers = cv2.connectedComponents(sure_fg)
axes[8].imshow(markers)
axes[8].set_title(f'9. Connected Components (Coins: {ret-1})')
print(f" 객체 카운터 개수는 {ret-1}개 입니다.")

markers = markers + 1
markers[res == 255] = 0
img_colored = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
markers = cv2.watershed(img_colored, markers)
img_colored[markers == -1] = [255, 0, 0]
axes[9].imshow(cv2.cvtColor(img_colored, cv2.COLOR_BGR2RGB))
axes[9].set_title('10. Watershed')

for ax in axes:
    ax.axis('off')

plt.show()
