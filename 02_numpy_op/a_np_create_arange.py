import numpy as np

a = np.arange(5)    # 0 ~ 5-1 로 배열을 생성한다.
print(a.shape)
print(a.dtype)

b = np.arange(3.0)
print(b.dtype)

print(a, type(a))
print(b, type(b))