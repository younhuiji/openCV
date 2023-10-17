import numpy as np
    # 데이터프로세싱 : 노이즈제거 = null(None), 0 연산이 된다.
a = np.empty((2,3))     # 쓰레기 값
b = np.empty((2,3), dtype=np.int16)     # 쓰레기 값 / 분석시에는 사용하지 않는다.

c = np.zeros((2,3))
d = np.ones((2,3), dtype=np.float32)
e = np.full((2,3,4), 255, dtype=np.uint8)

print(a, a.dtype, a.shape)
print(b, b.dtype, b.shape)
print(c, c.dtype, c.shape)
print(d, d.dtype, d.shape)
print(e, e.dtype, e.shape)