from scipy.optimize import minimize
import numpy as np


def f(x):
    Q = np.array([[1, 0], [0, 1]])
    out = np.matmul(x.T, np.matmul(Q, x))
    return out


consInEq = {'type': 'ineq',
            'fun': lambda x: -x[0] + 3
            }

x = np.array([1,1])
# x.shape = (2,1)
# print(x)
# print(f(x))

x0 = np.array([2,3])
#x0.shape = (2,1)

sol = minimize(f, x0, method = 'SLSQP', constraints=consInEq)
#sol = minimize(f, x0, constraints=consInEq)
#sol = minimize(f, x0)
print(sol)