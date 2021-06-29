from matplotlib import pyplot as plt
import numpy as np

start_time = 0
end_time = 10 ** -3
time_step = 10 ** -6
p_0=1.1*10**5
v_0 = 0
rho=10**3
r_0=0.002
lambda_squared = 3*p_0/(rho*r_0**2)

# analytical stuff (not implemented, just random numbers to make the plot work)
analytical = {'u': [r_0], 'v': [v_0], 't': [start_time]}
for ii in range(round((end_time-start_time)/time_step)):
    analytical['u'].append(r_0/3)
    analytical['v'].append(v_0/3)
    analytical['t'].append((ii+1)*(time_step))

plot = plt.plot(np.array(analytical['t']), np.array(analytical['u']), label = 'analytical')


#forward euler stuff
forward_euler = {'u': [r_0], 'v': [v_0], 't': [start_time]}

for ii in range(round((end_time-start_time)/time_step)):
    u_i = forward_euler['u'][ii]
    v_i = forward_euler['v'][ii]
    t_i = forward_euler['t'][ii]

    t_i_plus_1 = t_i + time_step
    w_i_plus_1 = -(3/2)*p_0/(rho*r_0)-lambda_squared*(u_i-r_0)
    v_i_plus_1 = v_i + time_step * w_i_plus_1
    u_i_plus_1 = u_i + time_step * v_i_plus_1
    forward_euler['u'].append(u_i_plus_1)
    forward_euler['v'].append(v_i_plus_1)
    forward_euler['t'].append(t_i_plus_1)

plot = plt.plot(np.array(forward_euler['t']), np.array(forward_euler['u']), label = 'forward_euler')

#RK2 stuff (not implemented, just random numbers to make the plot work)
rk_2 = {'u': [r_0], 'v': [v_0], 't': [start_time]}
for ii in range(round((end_time-start_time)/time_step)):
    rk_2['u'].append(r_0)
    rk_2['v'].append(v_0)
    rk_2['t'].append((ii+1)*(time_step))

plot = plt.plot(np.array(rk_2['t']), np.array(rk_2['u']), label = 'rk_2')

#RK4 stuff (not implemented, just random numbers to make the plot work)
rk_4 = {'u': [r_0], 'v': [v_0], 't': [start_time]}

for ii in range(round((end_time-start_time)/time_step)):
    rk_4['u'].append(r_0/2)
    rk_4['v'].append(v_0/2)
    rk_4['t'].append((ii+1)*(time_step))

plot = plt.plot(rk_4['t'], rk_4['u'], label = 'rk_4')

plt.legend()
plt.show()


