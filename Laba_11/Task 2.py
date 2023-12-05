import numpy as np
import matplotlib.pyplot as plt

#Генерируем выборку из нормального распределения
sr = 0  # среднее значение
otklon = 1  # стандартное отклонение
s_size = 1000  # размер выборки

samples = np.random.normal(sr, otklon, s_size)

#Отрисовываем гистограмму
plt.hist(samples, bins=30, density=True, alpha=0.7)
plt.xlabel('Значение')
plt.ylabel('Вероятность')
plt.title('Нормальное распределение')
plt.grid(True)
plt.show()