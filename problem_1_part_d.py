from matplotlib import pyplot as plt
import numpy as np

start_time = 0
end_time = 0.000347
time_step = 10 ** -9
p_0=1.1*10**5
v_0 = 0
rho=10**3
r_0=0.002
lambda_squared = 3*p_0/(rho*r_0**2)
constant_term = -(3/2)*p_0/(rho*r_0)

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
forward_euler = {'u': [r_0], 'v': [v_0], 't': [start_time]}

for ii in range(round((end_time-start_time)/time_step)):
    u_i = forward_euler['u'][ii]
    v_i = forward_euler['v'][ii]
    t_i = forward_euler['t'][ii]

    t_i_plus_1 = t_i + time_step
    w_i = constant_term-lambda_squared*(u_i-r_0)
    v_i_plus_1 = v_i + time_step * w_i
    u_i_plus_1 = u_i + time_step * v_i_plus_1
    forward_euler['u'].append(u_i_plus_1)
    forward_euler['v'].append(v_i_plus_1)
    forward_euler['t'].append(t_i_plus_1)

plot = plt.plot(np.array(forward_euler['t']), np.array(forward_euler['u']), label = 'forward_euler')

#RK2 stuff
# I don't know whether we need to be doing this method on both times, or only on the one?
# Like we only do the averaging on w, not on v, so is it one half RK2, one half forward euler
rk_2 = {'u': [r_0], 'v': [v_0], 't': [start_time]}
for ii in range(round((end_time-start_time)/time_step)):
    u_i = rk_2['u'][ii]
    v_i = rk_2['v'][ii]
    t_i = rk_2['t'][ii]
    t_i_plus_1 = t_i + time_step

    w_i = constant_term-lambda_squared*(u_i-r_0)

    v_i_plus_1_star = v_i + time_step * w_i

    u_i_plus_1_star = u_i + time_step * v_i_plus_1_star

    w_at_u_i_plus_1_star = constant_term-lambda_squared*(u_i_plus_1_star-r_0)

    w_avg = (w_i + w_at_u_i_plus_1_star)/2

    v = v_i + time_step * w_avg

    u = u_i + time_step * v


    rk_2['u'].append(u)
    rk_2['v'].append(v)
    rk_2['t'].append(t_i_plus_1)

plot = plt.plot(np.array(rk_2['t']), np.array(rk_2['u']), label = 'rk_2')

#RK4 stuff (not implemented, just random numbers to make the plot work)
rk_4 = {'u': [r_0], 'v': [v_0], 't': [start_time]}

for ii in range(round((end_time-start_time)/time_step)):
    u_i = rk_2['u'][ii]
    v_i = rk_2['v'][ii]
    t_i = rk_2['t'][ii]
    t_i_plus_1_half = t_i+(time_step/2)
    t_i_plus_1 = t_i + time_step

    w_at_u_i = constant_term-lambda_squared*(u_i-r_0)

    v_at_u_i = v_i + 1/2 * time_step * w_at_u_i

    u_i_plus_1_half_star = u_i + 1/2 * time_step * v_at_u_i

    w_i_plus_1_half_star = constant_term-lambda_squared*(u_i-r_0)

    v_i_plus_1_half_star = v_i+ 1/2 * time_step * w_i_plus_1_half_star

    u_i_plus_1_half_star_star = u_i + 1/2 * time_step * v_i_plus_1_half_star

    w_i_plus_1_half_star_star = constant_term-lambda_squared*(u_i-r_0)

    v_i_plus_1_half_star_star = v_i + 1/2 * time_step * w_i_plus_1_half_star_star

    u_i_plus_1_star = v_i_plus_1_half_star_star + time_step * v_i_plus_1_half_star_star

    w_i_plus_1_star = constant_term-lambda_squared*(u_i_plus_1_star-r_0)

    w_avg = w_at_u_i / 6 + w_i_plus_1_half_star / 3 + w_i_plus_1_half_star_star / 3 + w_i_plus_1_star / 6

    v = v_i + time_step * w_avg
    u = u_i + time_step * v



    rk_4['u'].append(u)
    rk_4['v'].append(v)
    rk_4['t'].append(t_i_plus_1)

plot = plt.plot(rk_4['t'], rk_4['u'], label = 'rk_4')

plt.legend()
plt.show()


