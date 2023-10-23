import cv2
import numpy as np
import matplotlib.pyplot as plt

def compare_histograms(img1, img2):
    # 이미지를 HSV (Hue, Saturation, Value) 형식으로 변환
    hsv_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    hsv_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    # HSV 이미지의 히스토그램 계산
    hist_img1 = cv2.calcHist([hsv_img1], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist_img2 = cv2.calcHist([hsv_img2], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])

    # 히스토그램 정규화
    cv2.normalize(hist_img1, hist_img1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    cv2.normalize(hist_img2, hist_img2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

    # 히스토그램 비교
    correlation = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_CORREL)

    return correlation

# 이미지 불러오기
img1 = cv2.imread("puppy.jpg")
img2 = cv2.imread("sample_puppy.jpg")

# 히스토그램 비교 후 유사도 출력
correlation = compare_histograms(img1, img2)
print(f"히스토그램 간의 상관관계: {correlation:.2f}")
# 히스토그램 간의 상관관계 : 8.45   -1 ~ 1 / 1(양의 상관관계 : 완벽), 0(관계없다), -1(을의 상관 관계)
# 양의 상관관계가 있지만 강황상관 관계는 아니다. -> 비교적 유사하다.
# 상관계수는 두 변수의 선형 관계의 강도와 방향만을 측정한다.

# 시각화
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("Template Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.text(0.5, 0.5, f"Correlation: {correlation:.2f}", fontsize=16, ha='center', va='center')
plt.title("Correlation")
plt.axis("off")

plt.show()
