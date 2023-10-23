import cv2, time
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../img/Lenna.png",0)

# 가우시안 블러링  커널크기  5*5  ------ 1
blurred_img= cv2.GaussianBlur(img, (5, 5), 0)

# 케니 엣지 적용
#100이하의  픽셀은 엣지로 간주하지 않는다.
#200이상을 엣지로 간주 한다. / 엣지에 해당하는 부분은 흰색,  그렇지 않은 부분은  0으로 리턴
#가우시안 블러  -> 케니엣지
edges = cv2.Canny(blurred_img,100,200)  #하위, 상위 임계값   ----- 2

print(edges)
# 결과 출력
plt.figure(figsize=(10, 10))

plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(blurred_img, cmap='gray')
plt.title("Blurred Image")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(edges, cmap='gray')
plt.title("Canny Edges")
plt.axis('off')

plt.show()




