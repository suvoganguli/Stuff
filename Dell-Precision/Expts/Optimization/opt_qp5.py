# Import the necessary packages
import numpy
from cvxopt import matrix
from cvxopt import solvers
from scipy.optimize import minimize

fun = lambda x: (x[0] - 1)**2 + (x[1] - 2.5)**2# Construct the QP, invoke solver

cons = ({'type': 'ineq', 'fun': lambda x:  x[0] - 2 * x[1] + 2},
        {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
        {'type': 'ineq', 'fun': lambda x: -x[0] + 2 * x[1] + 2})


bnds = ((0, None), (0, None))

res = minimize(fun, (2, 0), method='SLSQP', bounds=bnds,
               constraints=cons)

res

# minimize f(x) subject to
#
# g_i(x) >= 0,  i = 1,...,m
# h_j(x)  = 0,  j = 1,...,p

