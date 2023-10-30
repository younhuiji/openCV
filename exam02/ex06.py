# ex06.py

import cv2
import numpy as np
from matplotlib import pyplot as plt


def apply_fourier_transform(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 아래 코드를 채우세요
    f = np.fft.fft2(gray_image)
    fshift = np.fft.fftshift(f)

    magnitude_spectrum = 20 * np.log(np.abs(fshift))

    return magnitude_spectrum


# 이미지 불러오기
image = cv2.imread('apple.jpg')

# 푸리에 변환 적용
magnitude_spectrum = apply_fourier_transform(image)

# 결과 출력
(plt.subplot(121),
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Input Image'))
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray'), plt.title('Magnitude Spectrum')
plt.show()