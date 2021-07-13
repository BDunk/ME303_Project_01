from matplotlib import pyplot as plt
import numpy as np
from methods import forward_euler, rk_2, rk_4

start_time = 0
end_time = 0.000347
time_step = 10 ** -6
p_0=1.01*10**5
v_0 = 0
rho=10**3
r_0=0.002
lambda_squared = 3*p_0/(rho*r_0**2)
constant_term = -(3/2)*p_0/(rho*r_0)
w_func = lambda t, u, v : constant_term-lambda_squared*(u-r_0)
v_func = lambda t, u, v : v


# analytical stuff (not implemented, just random numbers to make the plot work)

analytical = {'u': [r_0], 't': [start_time]}
smallest = r_0
for ii in range(round((end_time-start_time)/time_step)):

    t_i = analytical['t'][ii]
    t_i_plus_1 = t_i + time_step
    u_i_plus_1 = ((1.5*r_0*np.cos(np.sqrt(lambda_squared)*t_i_plus_1)+v_0/np.sqrt(lambda_squared)*np.sin(np.sqrt(lambda_squared)*t_i_plus_1))/3+0.5*r_0)
    analytical['u'].append(u_i_plus_1)
    analytical['t'].append(t_i_plus_1)

plot = plt.plot(np.array(analytical['t']), np.array(analytical['u']), label = 'analytical')


#forward euler stuff
Euler = {'u': [r_0], 'v': [v_0], 't': [start_time], 'max_error':{'e': 0, 't': 0}}


for ii in range(round((end_time-start_time)/time_step)):
    t_i = Euler['t'][ii]
    u_i = Euler['u'][ii]
    v_i = Euler['v'][ii]

    e_i = np.abs(u_i - analytical['u'][ii])

    if e_i > Euler['max_error']['e']:
        Euler['max_error'] = {'e': e_i, 't': t_i}

    t_plus, u_plus, v_plus = forward_euler(t_i, u_i, v_i, time_step, v_func, w_func)


    Euler['t'].append(t_plus)
    Euler['u'].append(u_plus)
    Euler['v'].append(v_plus)

plot = plt.plot(np.array(Euler['t']), np.array(Euler['u']), label = 'forward_euler')

#RK2 stuff
RK_2 = {'u': [r_0], 'v': [v_0], 't': [start_time], 'max_error':{'e': 0, 't': 0}}
for ii in range(round((end_time-start_time)/time_step)):
    t_i = RK_2['t'][ii]
    u_i = RK_2['u'][ii]
    v_i = RK_2['v'][ii]

    e_i = np.abs(u_i - analytical['u'][ii])

    if e_i > RK_2['max_error']['e']:
        RK_2['max_error'] = {'e': e_i, 't': t_i}

    t_plus, u_plus, v_plus = rk_2(t_i, u_i, v_i, time_step, v_func, w_func)

    RK_2['t'].append(t_plus)
    RK_2['u'].append(u_plus)
    RK_2['v'].append(v_plus)

plot = plt.plot(np.array(RK_2['t']), np.array(RK_2['u']), label = 'rk_2')

# RK4 stuff
RK_4 = {'u': [r_0], 'v': [v_0], 't': [start_time], 'max_error':{'e': 0, 't': 0}}

for ii in range(round((end_time-start_time)/time_step)):
    u_i = RK_4['u'][ii]
    v_i = RK_4['v'][ii]
    t_i = RK_4['t'][ii]

    e_i = np.abs(u_i - analytical['u'][ii])

    if e_i > RK_4['max_error']['e']:
        RK_4['max_error'] = {'e': e_i, 't': t_i}

    t_plus, u_plus, v_plus = rk_4(t_i, u_i, v_i, time_step, v_func, w_func)

    RK_4['t'].append(t_plus)
    RK_4['u'].append(u_plus)
    RK_4['v'].append(v_plus)

plot = plt.plot(RK_4['t'], RK_4['u'], label = 'rk_4')

print(f"Errors (maximum error, time of maximium error):")
print(f"Euler - ({Euler['max_error']['e']}, {Euler['max_error']['t']}) ")
print(f"RK_2 - ({RK_2['max_error']['e']}, {RK_2['max_error']['t']}) ")
print(f"RK_4 - ({RK_4['max_error']['e']}, {RK_4['max_error']['t']}) ")

plt.legend()
plt.show()




