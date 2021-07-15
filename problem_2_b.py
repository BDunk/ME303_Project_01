import sys
import time

import numpy as np
from matplotlib import pyplot as plt
from methods import rk_4

rho = 1000
mu = 10 ** -3
sigma = 72 * 10 ** -3
u_0 = 100
v_0 = 0
p_0 = 1.01 * 10 ** 5

# times
d_t = 10 ** -5
t_0 = 0
t_f = 100

# functions
w_func = lambda t, u, v: ((-p_0 - 4 * mu * v / u - 2 * sigma / u) - (3 / 2 * v ** 2 * rho)) / (rho * u)
v_func = lambda t, u, v: v

epsilon = 10 ** 0

# Part B
RK_4 = {'u': [u_0], 'v': [v_0], 't': [t_0]}

ii = 0
while RK_4['t'][ii] < t_f:
    if(ii % 10000) == 0:
        # just displaying percentages, doing it every 1000 times to not waste resources
        sys.stdout.write('\r')
        sys.stdout.flush()
        sys.stdout.write(f"{int(round(ii/((t_f-t_0)/d_t),2)*100)}%")

    u_i = RK_4['u'][ii]
    v_i = RK_4['v'][ii]
    t_i = RK_4['t'][ii]

    if u_i < epsilon:
        # the function is to 'stiff', and gets messed up near 0
        # hadn't read this before, but it is in the notes for the project here
        v_i = - v_i

    t_plus, u_plus, v_plus = rk_4(t_i, u_i, v_i, d_t, v_func, w_func)

    RK_4['t'].append(t_plus)
    RK_4['u'].append(u_plus)
    RK_4['v'].append(v_plus)
    ii += 1

RK_4['abs_v'] = []
for ii in range(len(RK_4['v'])):
    RK_4['abs_v'].append(np.abs(RK_4['v'][ii]))

fig, axs = plt.subplots(3)

axs[0].plot(RK_4['t'], RK_4['u'], label='radius')
axs[1].plot(RK_4['t'], RK_4['v'], label='velocity')
axs[2].plot(RK_4['t'], RK_4['abs_v'], label='speed')

axs[2].set_yscale('log')

axs[0].legend()
axs[1].legend()
axs[2].legend()
plt.show()




