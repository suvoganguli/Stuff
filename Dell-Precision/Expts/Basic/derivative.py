
def system1(uk):
    return uk


def system2(uk, xk, T):
    xkp1 = xk + T * uk
    return xkp1


def system3(uk, xk, T):
    xkp1 = [0, 0]
    xkp1[0] = xk[0] + T * xk[1]
    xkp1[1] = xk[1] + T * uk
    return xkp1[0]


def grad_system1(u):
    eps = 1e-4
    uplus  = u + eps
    uminus = u - eps
    obj_uplus  = system1(uplus)
    obj_uminus = system1(uminus)
    obj_grad_u = (obj_uplus - obj_uminus) / (2*eps)
    return obj_grad_u


def grad_system2(u, x, T):
    eps = 1e-4
    uplus  = u + eps
    uminus = u - eps
    obj_uplus  = system2(uplus, x, T)
    obj_uminus = system2(uminus, x, T)
    obj_grad_u = (obj_uplus - obj_uminus) / (2*eps)
    return obj_grad_u


def grad_system3(u, x, T):
    eps = 1e-4
    uplus  = u + eps
    uminus = u - eps
    obj_uplus  = system3(uplus, x, T)
    obj_uminus = system3(uminus, x, T)
    obj_grad_u = (obj_uplus - obj_uminus) / (2*eps)
    return obj_grad_u


def grad_grad_system3(u, x, T):
    eps = 1e-4
    uplus  = u + eps
    uminus = u - eps
    obj_uplus  = grad_system3(uplus, x, T)
    obj_uminus = grad_system3(uminus, x, T)
    obj_grad_u = (obj_uplus - obj_uminus) / (2*eps)
    return obj_grad_u


u0 = 10.0
print(grad_system1(u0))

x0 = 1.0
T = 0.1
print(grad_system2(u0, x0, T))

x0 = [2.0, 3.0]
T = 0.1
print(grad_system3(u0, x0, T))

x0 = [2.0, 3.0]
T = 0.1
print(grad_grad_system3(u0, x0, T))