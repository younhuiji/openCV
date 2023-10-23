import numpy as np
import matplotlib.pyplot as plt

# 가우시안 함수
def gaussian(x, mu, sigma):
    return 1 / (np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(- (x - mu) ** 2 / (2 * sigma ** 2))

# 파라미터 설정 (평균과 표준편차) 평균은 0이고 표준편차가 1인 가우시안 함수를 그려 보자.
mu = 0      # 평균
sigma = 1  # 표준편차

# x 값 생성
x = np.linspace(-5, 5, 100) # x의 범위는 -5 ~ 5까지

# 가우시안 함수 적용
y = gaussian(x, mu, sigma)

# 그래프 그리기
plt.plot(x, y)
plt.title('Gaussian Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
