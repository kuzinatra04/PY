import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)

std_dev = np.std(Z, axis=1)
mse = np.mean(Z**2, axis=1)

fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')
ax1.set_zlabel('Z-axis')
ax1.set_title('Standard Deviation Function (MSE)')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, Z, cmap='viridis')
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')
ax2.set_zlabel('Z-axis (log scale)')
ax2.set_title('Standard Deviation Function (MSE) with log scale')
ax2.set_zscale('log')

plt.show()