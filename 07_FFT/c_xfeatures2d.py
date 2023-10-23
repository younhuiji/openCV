import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("kim.png"  ,0 )

# 1. 특징점 추출 알고리즘 메소드를 선언
sift = cv2.SIFT_create() # SIFT를 구한다.

# 2. 추출
res = sift.detect(img) # 주어진 이미지에서 핵심 포인터를 찾겠다.

# 3. 그리기
img_sift = cv2.drawKeypoints(img, res, None, flags=4)

plt.imshow(cv2.cvtColor(img_sift, cv2.COLOR_BGR2RGB))
plt.title('SIFT Keypoints')
plt.axis('off')
plt.show()
