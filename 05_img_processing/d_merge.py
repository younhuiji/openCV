import cv2 as cv
import matplotlib.pyplot as plt

# 이미지 불러오기
im1 = cv.imread('../img/apple.jpg')

# 채널 분리
b, g, r = cv.split(im1)

# 채널 병합
merged_im1 = cv.merge([b, g, r])

# matplotlib을 이용한 시각화
plt.figure(figsize=(5, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv.cvtColor(im1, cv.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Merged Image')
plt.imshow(cv.cvtColor(merged_im1, cv.COLOR_BGR2RGB))

plt.show()
