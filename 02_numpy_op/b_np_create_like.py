import cv2
import numpy as np

img = cv2.imread('../img/apple.jpg')
print(type(img))    # <class 'numpy.ndarray'>

a = np.empty_like(img)  # 특정값으로 초기화 하지 않는 것을 대입하자.
b = np.zeros_like(img)  # 0으로 채워진 값으로 리턴
c = np.ones_like(img)   # 1로 채워진 값으로 리턴
d = np.full_like(img, 255) # 255 값으로 채워진 값으로 리턴

print(a, a.shape, a.dtype)