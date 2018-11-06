import numpy as np

def system3(uk, xk, T):
    xkp1 = [0, 0]
    xkp1[0] = xk[0] + T * xk[1]
    xkp1[1] = xk[1] + T * uk
    return xkp1


def olp_system3(u, x0, T, N):
    x = np.zeros([N,np.size(x0)])
    x[0] = x0
    for k in range(N - 1):
        x[k + 1] = system3(u[k], x[k], T)

    return x


def objective(u, x, N):
    cost = 0.0
    r = 1
    idx = 0
    for k in range(N):
        cost = cost + (r - x[k,idx]) ** 2 + u[k] ** 2
    return cost


def grad_system3(u, N, x0, T):
    eps = 1e-1
    obj_grad_u = np.zeros(N)
    for k in range(N):
        uplus = np.copy(u)
        uminus = np.copy(u)

        uplus[k] = uplus[k] + eps
        xplus = olp_system3(uplus, x0, T, N)
        obj_uplus = objective(uplus, xplus, N)

        uminus[k] = uminus[k] - eps
        xminus = olp_system3(uminus, x0, T, N)
        obj_uminus = objective(uminus, xminus, N)

        obj_grad_u[k] = (obj_uplus - obj_uminus) / (2 * eps)

    return obj_grad_u


u0 = np.array([0, 10, 20, 30, 80, 100], dtype='float')
N = np.size(u0, 0)
x0 = np.array([1.0, 2.0])
T = 0.1

print(grad_system3(u0, N, x0, T))

