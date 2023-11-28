import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def generate_lisajhu(a, b, delta):
    t = np.linspace(0, 2*np.pi, 1000)
    x = np.sin(a*t + delta)
    y = np.sin(b*t)
    return x, y

fig, ax = plt.subplots(figsize=(6, 6))
line, = ax.plot([], [], lw=2)

def init():
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    return line,

def update(frame):
    ratio = frame / 100
    x, y = generate_lisajhu(1, ratio, 0)
    line.set_data(x, y)
    return line,

animation = FuncAnimation(fig, update, frames=100, interval=50, init_func=init, blit=True)

plt.show()