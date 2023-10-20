'''
2. 이미지 회전과 상하 좌우 반전

회전 : cv.rotate(ndarray , rotate_code) , np.rot90()

상하 좌우 반전 : cv.flip(ndarray , flip_code) , np.flip()
                 flip_code=0 상하 반전 ,    flip_code > 0  좌우 반전  ,flip_code< 0
'''
# 이미지 회전을 해보자.
import cv2 as cv
import matplotlib.pyplot as plt

# 이미지 불러오기
image = cv.imread('../img/Lenna.png')
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)  # OpenCV는 BGR을 사용하므로 RGB로 변환

# 회전된 이미지 생성
rotate_90_clockwise = cv.rotate(image_rgb, cv.ROTATE_90_CLOCKWISE)
rotate_180 = cv.rotate(image_rgb, cv.ROTATE_180)
rotate_90_counterclockwise = cv.rotate(image_rgb, cv.ROTATE_90_COUNTERCLOCKWISE)

# Matplotlib을 사용하여 이미지 출력
fig, axes = plt.subplots(1, 4, figsize=(20, 5))

axes[0].imshow(image_rgb)
axes[0].set_title("Original")
axes[0].axis('off')

axes[1].imshow(rotate_90_clockwise)
axes[1].set_title("Rotate 90 Clockwise")
axes[1].axis('off')

axes[2].imshow(rotate_180)
axes[2].set_title("Rotate 180")
axes[2].axis('off')

axes[3].imshow(rotate_90_counterclockwise)
axes[3].set_title("Rotate 90 Counterclockwise")
axes[3].axis('off')

plt.show()
