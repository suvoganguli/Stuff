from scipy.optimize import leastsq
import numpy as np

def f2(coord,args):
    x,y,r = args
    # notice that we're returning a vector of dimension 3
    return ((coord[0]-x)**2) + ((coord[1] - y)**2) - (r**2)

x = np.array([0,   2,  0])
y = np.array([0,   0,  2])
r = np.array([.88, 1, .75])

# initial (bad) guess at (x,y) values
initial_guess = np.array([100,100])

res = leastsq(f2,initial_guess,args = [x,y,r])
print(res)