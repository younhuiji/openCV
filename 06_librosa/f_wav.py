import numpy as np
import matplotlib.pyplot as plt

N = 600
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)

# FFT 적용
yf = np.fft.fft(y)
xf = np.fft.fftfreq(N, T)[:N//2]

# 결과 출력
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()

plt.xlabel('주파수', fontproperties='Malgun Gothic')
plt.ylabel('신호성분(db)', fontproperties='Malgun Gothic')
