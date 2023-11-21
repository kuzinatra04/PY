# Найти максимальный элемент в векторе x среди элементов, перед которыми стоит нулевой.
# Для x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0]) ответ 5.

import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
i = len(x)
while i != 0:
    i -= 1
    if x[i - 1] != 0:
        x = np.delete(x, i)

print(f"Максимальный элемент, перед которым стоит нулевой: {x.max()}")
