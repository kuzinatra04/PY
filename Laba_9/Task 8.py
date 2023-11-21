# Найти индексы ненулевых элементов в [0, 1, 2, 0, 0, 4, 0, 6, 9]

import numpy as np

x = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])
i = len(x)
index = np.array([])
for i in range(len(x)):
    if x[i] != 0:
        index = np.append(index, i)

index = index.astype('int32')
print(f"Индексы ненулевых элементов массива: {index}")
