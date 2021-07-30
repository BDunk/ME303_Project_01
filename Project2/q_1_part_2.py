import math
import os

import numpy as np
from matplotlib import pyplot as plt

# https://www.sciencedirect.com/science/article/abs/pii/S0260877405001330#:~:text=Conclusions,to%2088.2%25%20(mass).
alpha = 0.6
d_t = 10 ** -4
d_r = 10 ** -5
T_surrounding = 100
T_egg_initial = 25

record_every_n_steps = 10**4
def eggCookingValues(R):
    values_for_plot = [[], []]
    T_values_old = []
    t_index = 0
    n = 0
    while True:
        t = d_t * t_index
        T_values = []
        for r_index in range(math.ceil(R / d_r) + 1):
            r = r_index * d_r
            F = alpha * d_t / d_r ** 2
            if math.isclose(r, R):
                T = T_surrounding
            elif math.isclose(t, 0):
                # this is true for r=R and t=0, but previous condition teakes precendence
                T = T_egg_initial
            elif math.isclose(r, 0):
                T = (T_values_old[r_index] + F * 2 * T_values_old[r_index+1])/(1+2*F)
            else:
                T = (T_values_old[r_index] + F * (T_values_old[r_index + 1]+T_values_old[r_index - 1])) / (1 + 2 * F)
            T_values.append(T)
        if n==record_every_n_steps:
            # this prevents gigabyte sized .csv
            n=0
            values_for_plot[0].append(t)
            values_for_plot[1].append(T_values[0])
            print(round(t, 3), T_values[0], T_values[int(R / d_r / 4)], T_values[int(R / d_r / 2)],
                  T_values[int(3 * R / d_r / 4)], T_values[int(R / d_r)])
            if T_values[0] > 80:
                # this code used to be outside of the other if statement
                # it was moved here so that usually only one condition has to be checked
                # side benefit is that we are only plotting on a seconds scale, so we get
                # the lowest whole num of seconds
                return np.array(values_for_plot)
        T_values_old = T_values
        t_index+=1
        n+=1


# the assumption is made that there is no difference between the spherical eggs aside from the radius
# https://brinsea.co.uk/latest/resource-centre/egg-sizes/
# ((0.035 + 0.027) / 2) / 2
quail_radius = 0.0155
# ((0.062 + 0.043) / 2) / 2
chicken_radius = 0.0263
# https://www.britannica.com/animal/ostrich
# ((0.150 + 0.125) / 2) / 2
ostrich_radius = 0.0688

quail_values = np.genfromtxt('quail.csv', delimiter=',', dtype=None, names=True) if os.path.isfile('quail.csv') else eggCookingValues(quail_radius),
if not os.path.isfile('quail.csv'):
    np.savetxt("quail.csv", quail_values[0], delimiter=",")
chicken_values = np.genfromtxt('chicken.csv', delimiter=',', dtype=None, names=True) if os.path.isfile('chicken.csv') else eggCookingValues(chicken_radius),
if not os.path.isfile('chicken.csv'):
    np.savetxt("chicken.csv", chicken_values[0], delimiter=",")
ostrich_values = np.genfromtxt('ostrich.csv', delimiter=',', dtype=None, names=True) if os.path.isfile('ostrich.csv') else eggCookingValues(ostrich_radius),
if not os.path.isfile('ostrich.csv'):
    np.savetxt("ostrich.csv", ostrich_values[0], delimiter=",")

fig, ax = plt.subplots()
#ax.plot(quail_values['t'], quail_radius['T_at_0'], label='temp_at_center')

plt.show()
