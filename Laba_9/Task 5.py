# Реализовать функцию вычисления логарифма плотности многомерного нормального распределения.
# Входные параметры: точки X, размер (N, D), мат. ожидание m, вектор длины D, матрица ковариаций C, размер (D, D).
# Разрешается использовать библиотечные функции для подсчета определителя матрицы, а также обратной матрицы, в том числе в невекторизованном варианте.
# Сравнить с scipy.stats.multivariate_normal(m, C).logpdf(X) как по скорости работы, так и по точности вычислений.

import time
import numpy as np
from scipy.stats import multivariate_normal


def logarifm(X, m, C):
    detCov = np.linalg.det(C)
    invCov = np.linalg.inv(C)

    X_centered = X - m
    exponent = -0.5 * np.sum(X_centered @ invCov * X_centered, axis=1)
    # X_centered @ invCov: матричное умножение X_centered на обратную матрицу inv_C
    normalization = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(detCov)
    log = exponent + normalization
    return log


N = 10
D = 7
X = np.random.randn(N, D)
m = np.random.randn(D)
C = np.random.randn(D, D)
C = np.dot(C, C.T)

# Измерение времени выполнения собственной реализации
start_time = time.time()
result_custom = logarifm(X, m, C)
custom_duration = time.time() - start_time

# Измерение времени выполнения с использованием scipy.stats.multivariate_normal
start_time = time.time()
result_scipy = multivariate_normal(m, C).logpdf(X)
scipy_duration = time.time() - start_time

# Печать результатов
print(f"\nMy result: \n{result_custom}\n")
print(f"Scipy result:\n{result_scipy}\n")

# Сравнение времени выполнения
print(f"\nMy time: {custom_duration} seconds\n")
print(f"Scipy time: {scipy_duration} seconds\n")