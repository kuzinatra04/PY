# Поменять местами две строки в двумерном массиве NumPy - поменяйте  строки 1 и 3 массива а.
# a = np.arange(16).reshape(4,4)

import numpy as np

a = np.arange(16).reshape(4,4)
print('Первоначальный массив: ')
print(a)

a[[0, 2]] = a[[2, 0]]

print('')
print('Новый массив: ')
print(a)
