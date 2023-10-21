import matplotlib.pyplot as plt
import numpy as np

# 시간 벡터 생성 : # 0부터 1까지의 범위에서 500개의 샘플 포인트를 생성
t = np.linspace(0, 1, 500, endpoint=False)
print(t)

# 파라미터 설정
A = 1       # 진폭
f = 5       # 주파수 (Hz)
phi = 0    # 위상 (라디안)

# 2 * np.pi * f : 각 주파수의 수

# 정현파와 여현파 생성
y_sin = A * np.sin(2 * np.pi * f * t + phi)
y_cos = A * np.cos(2 * np.pi * f * t + phi)

# 그래프 그리기
plt.figure()

# 정현파 그래프
plt.subplot(2, 1, 1)  # 2행 1열의 첫 번째 위치
plt.title('Sinusoidal Wave')
plt.plot(t, y_sin)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# 여현파 그래프
plt.subplot(2, 1, 2)  # 2행 1열의 두 번째 위치
plt.title('Cosinusoidal Wave')
plt.plot(t, y_cos)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
