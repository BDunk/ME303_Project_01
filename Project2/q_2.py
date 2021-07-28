import math
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

x_0 = 0
x_1 = 1
y_0 = 0
y_1 = 1
t_0 = 0
t_1 = 5 * 10 ** -1
d_s = 10 ** -2
d_t = 10 ** -3
alpha = 10 ** -2


values = np.empty((int((t_1 - t_0) / d_t) + 1, int((x_1 - x_0) / d_s) + 1, int((y_1 - y_0) / d_s) + 1))

for t_index in range(int((t_1 - t_0) / d_t) + 1):
    t = t_index * d_t
    print(t / t_1)
    for x_index in range(int((x_1 - x_0) / d_s) + 1):
        x = x_index * d_s
        for y_index in range(int((y_1 - y_0) / d_s) + 1):
            y = y_index * d_s
            if math.isclose(t, 0):
                values[t_index, x_index, y_index] = np.sin(4 * np.pi * x) * np.cos(4 * np.pi * y)
            elif math.isclose(x, 0):
                values[t_index, x_index, y_index] = 0
            elif math.isclose(x, 1):
                values[t_index, x_index, y_index] = 0
            elif math.isclose(y, 0):
                values[t_index, x_index, y_index] = np.sin(np.pi * x)
            elif math.isclose(y, 1):
                values[t_index, x_index, y_index] = np.cos(2 * np.pi * x) - 1
            else:
                x_term = (values[t_index-1, x_index + 1, y_index] - 2 * values[t_index-1, x_index, y_index] + values[
                    t_index-1, x_index - 1, y_index]) / d_s ** 2
                y_term = (values[t_index-1, x_index, y_index + 1] - 2 * values[t_index-1, x_index, y_index] + values[
                    t_index-1, x_index, y_index - 1]) / d_s ** 2

                values[t_index, x_index, y_index] = d_t * alpha * (x_term + y_term) + values[t_index-1, x_index, y_index]



fig, ax = plt.subplots()
def plot(t_index):
    x = np.arange(x_0, x_1+d_s, d_s)
    y = np.arange(y_0, y_1+d_s, d_s)
    heatmap = ax.pcolormesh(x,y,values[t_index], shading='auto')
    plt.title(t_index*d_s)

ani = animation.FuncAnimation(fig, plot,int((t_1 - t_0) / d_t) + 1, interval=10)
ani.save('./animation.mp4', writer='ffmpeg', fps=15)

plt.show()




