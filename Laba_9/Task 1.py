import numpy as np

filedata = np.genfromtxt('matrix.txt', delimiter=',')
filedata = filedata.astype('int32')

print(f"Матрица: \n{filedata}")
print(f"Сумма элементов матрицы: {filedata.sum()}")
print(f"Минимальный элемент матрицы: {filedata.min()}")
print(f"Максимальный элемент матрицы: {filedata.max()}")