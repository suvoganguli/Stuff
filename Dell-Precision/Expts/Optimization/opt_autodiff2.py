#from __future__ import absolute_import
import autograd.numpy as np  # Thinly-wrapped numpy
from autograd import grad    # The only autograd function you may ever need
from autograd import elementwise_grad as egrad # for functions that vectorize over inputs


def tanh(x):                 # Define a function
    y = np.exp(-2.0 * x)
    return (1.0 - y) / (1.0 + y)


#x = np.linspace(-1, 1, 1) #np.array([1,2])
x2 = np.array([-1,0,1])
x3 = np.float_(x2)

#grad_tanh = grad(tanh)       # Obtain its gradient function

x0 = np.float_(1)
a = grad(tanh)(x0)               # Evaluate the gradient at x = 1.0
b = tanh(x3)
c = grad(tanh)(x3)
d = egrad(tanh)(x3)

# b = (tanh(1.0001) - tanh(0.9999)) / 0.0002  # Compare to finite differences

print(a)
print(b)
print(c)
print(d)
