import numpy as np

def system1(uk):
    return uk


def grad_system1(u, N):
    eps = 1e-4
    obj_grad_u = np.zeros(N)
    for k in range(N):
        uplus  = u[k] + eps
        uminus = u[k] - eps
        obj_uplus  = system1(uplus)
        obj_uminus = system1(uminus)
        obj_grad_u[k] = (obj_uplus - obj_uminus) / (2*eps)

    return obj_grad_u


u0 =[10.0, 20.0, 30.0]
N = np.size(u0,0)

print(grad_system1(u0, N))

