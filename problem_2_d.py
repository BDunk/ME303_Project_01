import sys
import time
from matplotlib import pyplot as plt
from methods import rk_4

u_0_1 = 10
t_f_1 = 1
d_t_1 = 10 ** -7

u_0_2 = 1
t_f_2 = 10 ** -1.5
d_t_2 = 10 ** -8.5

u_0_3 = 0.001
t_f_3 = 10 ** -4.5
d_t_3 = 10 ** -12

def problem_2_d(u_0, t_f,d_t):
    rho = 1000
    mu = 10 ** -3
    sigma = 72 * 10 ** -3
    v_0 = 0
    p_0 = 100100000

    # times
    t_0 = 0
   
    # functions
    w_func = lambda t, u, v: ((-p_0 - 4 * mu * v / u - 2 * sigma / u) - (3 / 2 * v ** 2 * rho)) / (rho * u)
    v_func = lambda t, u, v: v

    epsilon = u_0 * 0.01

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

    return RK_4

fig, axs = plt.subplots(3)

part_d_1 = problem_2_d(u_0_1, t_f_1, d_t_1)
axs[0].plot(part_d_1['t'], part_d_1['u'], color='g', label='Radius: 10m')
axs[0].legend()

part_d_2 = problem_2_d(u_0_2, t_f_2, d_t_2)
axs[1].plot(part_d_2['t'], part_d_2['u'], color='r', label='Radius: 1m',)
axs[1].legend()

part_d_3 = problem_2_d(u_0_3, t_f_3, d_t_3)
axs[2].plot(part_d_3['t'], part_d_3['u'], color='b', label='Radius: 0.001m')
axs[2].legend()

plt.xlabel("Time")
plt.ylabel("Radius")
plt.show()
