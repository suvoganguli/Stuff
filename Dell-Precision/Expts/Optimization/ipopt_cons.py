import ipopt
import numpy as np

class nlp(object):

    def __init__(self):
        pass

    def objective(self, x):
        return (x[0] - 1.0)**2 + (x[1] - 2.0)**2

    def gradient(self, x):
        return [2*(x[0]-1.0), 2*(x[1]-2.0)]

    def constraints(self, x):
        return x[0]

    def jacobian(self, x):
        return [1.0, 0.0]


lb = None  # np.ones([N,1])*(-3)
ub = None  # np.ones([N,1])*(3)
cl = [1.5]
cu = None

p = ipopt.problem(
    n=2,
    m=1,
    problem_obj=nlp(),
    lb=lb,
    ub=ub,
    cl=cl,
    cu=cu
)
p.addOption('print_level', 0)
p.addOption('max_iter', 20)

x0 = [0,0]
xstar, info = p.solve(x0)

print(xstar)




