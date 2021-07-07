from matplotlib import pyplot as plt
from methods import rk_4

rho = 1000
mu = 10**-3
sigma = 72*10**-3
u_0 = 100
v_0 = 0
p_0 = 100100000

# times
d_t = 10**-6
t_0 = 0
t_f = 0.3

#functions
w_func = lambda t, u, v : ((-p_0 - 4 * mu * v / u - 2 * sigma / u) - (3 / 2 * v ** 2 * rho)) / (rho * u)
v_func = lambda t, u, v : v


# Part B
# TODO: LMAO, it doesn't converge, that can't be right, wondering if it causes a divide by zero when u is exactly 0
RK_4 = {'u': [u_0], 'v': [v_0], 't': [t_0]}

for ii in range(round((t_f-t_0)/d_t)):
    print(ii/((t_f-t_0)/d_t))
    u_i = RK_4['u'][ii]
    v_i = RK_4['v'][ii]
    t_i = RK_4['t'][ii]

    t_plus, u_plus, v_plus = rk_4(t_i, u_i, v_i, d_t, v_func, w_func)

    RK_4['t'].append(t_plus)
    RK_4['u'].append(u_plus)
    RK_4['v'].append(v_plus)

plot = plt.plot(RK_4['t'], RK_4['u'], label = 'rk_4')

plt.legend()
plt.show()

