import numpy as np
# Numpy 모듈의 array로 배열을 생성하고 데이터 타입과 형태를 확인

a = np.array([1,2,3,4])     # 정수를 갖는 리스트로 생성
b = np.array([[1,2,3,4],    # 2차원 리스트로 생성
              [5,6,7,8]])
c = np.array([1,2,3.14,4])  # 정수와 소수점이 혼재된 리스트
d = np.array([1,2,3,4], dtype=np.float64)   # dtype을 지정해서 생성

print(a, a.dtype, a.shape)  # --- ① 1차원 배열 / int64 (4,)
print(b, b.dtype, b.shape)  # --- ② 2차원 배열 / int64 (2, 4)
print(c, c.dtype, c.shape)  # --- ③ 정수와 소숫점 혼재된 1차원 배열 / float64 (4,)
print(d, d.dtype, d.shape)  # --- ④ dtype을 지정한 1차원 배열 / float64 (4,)