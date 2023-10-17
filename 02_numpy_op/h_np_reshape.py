import numpy as np

a = np.arange(6)
b = a.reshape(2,3)

c = np.arange(24).reshape(2,3,4)

d = np.arange(100).reshape(2, -1) # 2행으로 선언하고, (-1:) = 나머지는 자동으로 재배열 해라
e = np.arange(100).reshape(-1, 5)


f = np.ravel(c) ##### -> 다차원 배열을 1차원 배열로 flatten(평탄화, 평활화)한다.

g = np.arange(10).reshape(2,-1)
'''
print(a, a.shape)
print(b, b.shape)
print(c, c.shape)
print(d, d.shape)
print(e, e.shape)
print(f, f.shape)
'''
print(g)
print(g.T)  # 전체행열
