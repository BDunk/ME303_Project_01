import sys
import time
from matplotlib import pyplot as plt
from methods import rk_4

u_0 = 100
rho = 1000
mu = 10 ** -3
sigma = 72 * 10 ** -3
v_0 = 0
p_0 = 1.01*10**5

# times
d_t = 10 ** -6
t_0 = 0
t_f = 1

# functions
w_func = lambda t, u, v: ((-p_0 - 4 * mu * v / u - 2 * sigma / u) - (3 / 2 * v ** 2 * rho)) / (rho * u)
v_func = lambda t, u, v: v

epsilon = 10 ** 0

value_1_i = {'u': u_0, 'v': v_0, 't': t_0}
value_5_i = {'u': u_0, 'v': v_0, 't': t_0}
value_25_i = {'u': u_0, 'v': v_0, 't': t_0}
value_125_i = {'u': u_0, 'v': v_0, 't': t_0}
value_625_i = {'u': u_0, 'v': v_0, 't': t_0}

sum_1_error = 0
sum_5_error = 0
sum_25_error = 0
sum_125_error = 0
# this should probably be recursive since all I was doing was copying the same code and dividing by 10
for aa in range(round((t_f - t_0) / d_t)):
    print(aa)

    sum_1_error += (value_625_i['u'] - value_1_i['u']) ** 2
    sum_5_error += (value_625_i['u'] - value_5_i['u']) ** 2
    sum_25_error += (value_625_i['u'] - value_25_i['u']) ** 2
    sum_125_error += (value_625_i['u'] - value_125_i['u']) ** 2

    if value_1_i['u'] < epsilon:
        value_1_i['v'] = - value_1_i['v']

    value_1_i['t'], value_1_i['u'], value_1_i['v'] = rk_4(value_1_i['t'], value_1_i['u'], value_1_i['v'], d_t, v_func,
                                                          w_func)

    for bb in range(5):
        if value_5_i['u'] < epsilon:
            value_5_i['v'] = - value_5_i['v']

        value_5_i['t'], value_5_i['u'], value_5_i['v'] = rk_4(value_5_i['t'], value_5_i['u'], value_5_i['v'], d_t/5,
                                                              v_func,
                                                              w_func)
        for cc in range(5):
            if value_25_i['u'] < epsilon:
                value_25_i['v'] = - value_25_i['v']

            value_25_i['t'], value_25_i['u'], value_25_i['v'] = rk_4(value_25_i['t'], value_25_i['u'], value_25_i['v'],
                                                                  d_t / 25,
                                                                  v_func,
                                                                  w_func)
            for dd in range(5):
                if value_125_i['u'] < epsilon:
                    value_125_i['v'] = - value_125_i['v']

                value_125_i['t'], value_125_i['u'], value_125_i['v'] = rk_4(value_125_i['t'], value_125_i['u'],
                                                                         value_125_i['v'],
                                                                         d_t / 125,
                                                                         v_func,
                                                                         w_func)
                for ee in range(5):
                    if value_625_i['u'] < epsilon:
                        value_625_i['v'] = - value_625_i['v']

                    value_625_i['t'], value_625_i['u'], value_625_i['v'] = rk_4(value_625_i['t'], value_625_i['u'],
                                                                                value_625_i['v'],
                                                                                d_t / 625,
                                                                                v_func,
                                                                                w_func)

num_steps = round((t_f - t_0) / d_t)
print(f"1 * 10 ** -6 : {(sum_1_error/num_steps)**0.5}")
print(f"5 * 10 ** -6 : {(sum_5_error/num_steps)**0.5}")
print(f"25 * 10 ** -6 : {(sum_25_error/num_steps)**0.5}")
print(f"125 * 10 ** -6 : {(sum_125_error/num_steps)**0.5}")

