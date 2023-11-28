import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

x = np.linspace(-1, 1, 100)

fig, ax = plt.subplots()

for i in range(1, 8):
    y = legendre(i)(x)
    ax.plot(x, y, label=f'n = {i}')

ax.set_xlabel('x')
ax.set_ylabel('Pn(x)')
ax.set_title('Legendre Polynomials')
ax.legend()

plt.show()