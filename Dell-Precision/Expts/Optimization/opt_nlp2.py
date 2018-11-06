from scipy.optimize import minimize
import numpy as np


def f(x):
    return np.square(x)*np.sin(x)


cons = {'type': 'ineq',
        'fun': lambda x: -x + 3,
        'jac': lambda x: -1}

#x0 = np.array([-3])
#x0 = np.array([2])
x0 = np.array([2.5])

sol = minimize(f, x0, method = 'SLSQP', constraints=cons)
#sol = minimize(f, x0, constraints=cons)
print(sol)