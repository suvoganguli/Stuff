# Import the necessary packages
import numpy
from cvxopt import matrix
from cvxopt import solvers

# Define QP parameters (directly)
# min 0.5*x'*P*x + q'*x
#  x
# subject to Gx <= h
#            Ax = b
#
# https://courses.csail.mit.edu/6.867/wiki/images/a/a7/Qp-cvxopt.pdf

P = matrix([[1.0,0.0],[0.0,0.0]])
q = matrix([3.0,4.0])
G = matrix([[-1.0,0.0,-1.0,2.0,3.0],[0.0,-1.0,-3.0,5.0,4.0]])
h = matrix([0.0,0.0,-15.0,100.0,80.0])

# Define QP parameters (with NumPy)
P = matrix(numpy.diag([1,0]), tc='d')
q = matrix(numpy.array([3,4]), tc='d')
G = matrix(numpy.array([[-1,0],[0,-1],[-1,-3],[2,5],[3,4]]), tc='d')
h = matrix(numpy.array([0,0,-15,100,80]), tc='d')

# Construct the QP, invoke solver
sol = solvers.qp(P,q,G,h)

# Extract optimal value and solution
sol['x'] # [7.13e-07, 5.00e+00]
sol['primal objective'] # 20.0000061731

print(sol['x'])
print(sol['primal objective'])
