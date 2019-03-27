from scipy.integrate import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import data_on_num
import config

data = odeint(data_on_num.ode, data_on_num.x, data_on_num.t)

m = config.skipper  # коэффициент ускорения
fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)
ax1.set_title(u'Track')
ax2 = fig.add_subplot(1, 2, 2)
ax2.set_title(u'Velocity')
ax1.grid()
ax2.grid()

mk, = ax1.plot([], [], 'bo', ms=10)
ln, = ax1.plot([], [], 'g-')
ln2, = ax1.plot([], [], 'g-')

pl = config.pl


def update_plot_data(i, m):
    mk.set_data(data[i * m][0] + config.Mx0, data[i * m][1] + config.My0)
    if i * m > pl:
        ln.set_data([data[i * m - pl][0], config.Mx0], [data[i * m - pl][1], config.My0])
        ln2.set_data([data[i * m][0], config.Mx0], [data[i * m][1], config.My0])
    return mk, ln, ln2,


def ini():
    ax1.plot(data[:, 0] + config.Mx0, data[:, 1] + config.My0, 'k-', lw=1)
    ax1.plot(config.Mx0, config.My0, 'ro', ms=20)

    ax1.plot([data[pl][0], config.Mx0], [data[pl][1], config.My0], 'r-')
    ax1.plot([data[0][0], config.Mx0], [data[0][1], config.My0], 'r-')

    ax1.axis('equal')
    return mk, ln, ln2,


anim = animation.FuncAnimation(fig, update_plot_data, len(data) // m, init_func=ini, fargs=[m],
                               interval=config.interval, blit=True, repeat=False)

mk2, = ax2.plot([], [], 'bo', ms=5)


def update_plot(i, m):
    mk2.set_data(data_on_num.t[i * m], (data[i * m][2] ** 2 + data[i * m][3] ** 2) ** 0.5)
    return mk2,


def ini2():
    ax2.plot(data_on_num.t, (data[:, 2] ** 2 + data[:, 3] ** 2) ** 0.5, '-')
    return mk2,


anim2 = animation.FuncAnimation(fig, update_plot, len(data) // m, init_func=ini2, fargs=[m], interval=config.interval,
                                blit=True, repeat=False)

# plt.plot(data[:, 0], data[:, 1])
# plt.grid()
# plt.axis('equal')
plt.show()
