import numpy as np
import matplotlib.pyplot as plt

def lisajhu_figure(a, b):
    t = np.linspace(0, 2 * np.pi, 1000)
    x = np.sin(a * t)
    y = np.sin(b * t)
    return x, y

ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]

fig, axs = plt.subplots(2, 2)

for i, ratio in enumerate(ratios):
    a, b = ratio
    x, y = lisajhu_figure(a, b)
    row = i // 2
    col = i % 2
    axs[row, col].plot(x, y)
    axs[row, col].set_title(f'{a}:{b}')

plt.tight_layout()

plt.show()