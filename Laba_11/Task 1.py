import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Параметры сигнала
amplitude = 1.0
sampling_frequency = 100  # Частота дискретизации
duration = 2.0  # Длительность сигнала в секундах
t = np.linspace(0, duration, int(sampling_frequency * duration), endpoint=False)

# Генерирование прямоугольного сигнала
rect_signal = amplitude * signal.square(2 * np.pi * 5 * t)  # Частота 5 Гц

# Отрисовка сигнала
plt.figure(figsize=(10, 4))
plt.plot(t, rect_signal)
plt.title('Прямоугольный сигнал')
plt.xlabel('Время (сек)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.show()