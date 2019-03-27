import config
import numpy as np

# Коэффициент интегрирования, -G*M
k = -1 * config.G * config.M

# Перенос начала координат в точку, где находится массивное тело
x0 = config.x0 - config.Mx0
y0 = config.y0 - config.My0

# Создание временного диапазона
t = np.arange(config.t0, config.tn, config.t_step[config.t_i])

# Начальные значения
x = [x0, y0, config.v0x, config.v0y]


def ode(X, t):
    return [
        X[2],
        X[3],
        k * X[0] * (X[0] ** 2 + X[1] ** 2) ** (-1.5),
        k * X[1] * (X[0] ** 2 + X[1] ** 2) ** (-1.5)
    ]
