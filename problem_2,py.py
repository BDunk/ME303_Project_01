rho = 1
mu = 1
sigma = 1
u_0 = 1
v_0 = 1
p_0 = 1
w_func = lambda t, u, v : ((-p_0 - 4 * mu * v / u - 2 * sigma / u) - (3 / 2 * v ** 2 * rho)) / (rho * u)
v_func = lambda t, u, v : v

