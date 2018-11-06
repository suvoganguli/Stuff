from scipy.optimize import minimize
import numpy as np


def f(x):
    return np.square(x) + 1


# def cons(x):
#      a = 3
#      return -x + a


x0 = -10

# sol = minimize(f,x0)
# print(sol)

cons = [{'type': 'ineq', 'fun': lambda x:  x - 3},
        {'type': 'ineq', 'fun': lambda x: -x + 2}]

bnds = ((-1,0.5),)
solc = minimize(f,x0,constraints=cons,bounds=bnds)
print(solc)

