"""
For all of these functions:
It returns a tuple with the next values of:
u
v
t

It takes:
u_i: the previous value of u
v_i: the previous value of v
t_i: the previous value of t
d_t: the difference between t_i and t_i_plus_1
v: a lambda function that takes t,u,v
w: a lambda function that takes t,u,v

"""
def forward_euler(t_i, u_i, v_i, d_t, v, w):

    k_0 = d_t * v(t_i, u_i, v_i)
    l_0 = d_t * w(t_i, u_i, v_i)

    t_i_plus_1 = t_i + d_t
    u_i_plus_1 = u_i + k_0
    v_i_plus_1 = v_i + l_0
    return t_i_plus_1, u_i_plus_1, v_i_plus_1

def rk_2(t_i, u_i, v_i, d_t, v, w):
    k_0 = d_t * v(t_i, u_i, v_i)
    l_0 = d_t * w(t_i, u_i, v_i)

    k_1 = d_t * v(t_i + d_t, u_i + k_0, v_i + l_0)
    l_1 = d_t * w(t_i + d_t, u_i + k_0, v_i + l_0)

    t_i_plus_1 = t_i + d_t
    u_i_plus_1 = u_i + (k_0+k_1) / 2
    v_i_plus_1 = v_i + (l_0+l_1) / 2
    return t_i_plus_1, u_i_plus_1, v_i_plus_1


def rk_4(t_i, u_i, v_i, d_t, v, w):

    k_0 = d_t * v(t_i, u_i, v_i)
    l_0 = d_t * w(t_i, u_i, v_i)

    k_1 = d_t * v(t_i + d_t / 2, u_i + k_0 / 2, v_i + l_0 / 2)
    l_1 = d_t * w(t_i + d_t / 2, u_i + k_0 / 2, v_i + l_0 / 2)

    k_2 = d_t * v(t_i + d_t / 2, u_i + k_1 / 2, v_i + l_1 / 2)
    l_2 = d_t * w(t_i + d_t / 2, u_i + k_1 / 2, v_i + l_1 / 2)

    k_3 = d_t * v(t_i + d_t, u_i + k_2, v_i + l_2)
    l_3 = d_t * w(t_i + d_t, u_i + k_2, v_i + l_2)

    t_i_plus_1 = t_i + d_t
    u_i_plus_1 = u_i + (k_0 + 2 * k_1 + 2 * k_2 + k_3) / 6
    v_i_plus_1 = v_i + (l_0 + 2 * l_1 + 2 * l_2 + l_3) / 6

    return t_i_plus_1, u_i_plus_1, v_i_plus_1
