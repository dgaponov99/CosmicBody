from scipy.integrate import *
import matplotlib.pyplot as plt

import data_on_num
import config

t_array = data_on_num.t
t0 = t_array[0]
t_bound = config.tn
t_step = config.t_step[config.t_i]

y0 = data_on_num.x
fun = data_on_num.ode

# sol = solve_ivp(fun=fun, t_span=(t0, t_bound), y0=y0, rtol=10 ** -6)


def fun2(X, t):
    return fun(t, X)


data = odeint(fun2, y0, t_array, rtol=10**-13)

energy = (data_on_num.k) * (data[:, 0] ** 2 + data[:, 1] ** 2) ** -0.5 + 0.5 * (
        data[:, 2] ** 2 + data[:, 3] ** 2)

# y = sol.y
# plt.plot(y[0, :], y[1, :], '*')
# plt.plot(data[:, 0], data[:, 1], '-')
plt.plot(t_array, -energy)
# plt.axis('equal')
plt.show()
