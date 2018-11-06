import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def rosenbrock_f(a, b):
    """Return the Rosenbrock function, Jacobian & Hessian.

    Parameters
    ----------
    a, b : float
        Parameters defining the surface.  Typical values are a=1, b=100.

    Notes
    -----
    The Rosenbrock function has a minimum of 0 at ``(a, a**2)``.

    """
    def f(x, y):
        return (a - x)**2 + b * (y - x**2) ** 2

    def J(x, y):
        return np.array([-2 * (a - x) - 4 * b * x * (y - x**2),
                         2 * b * (y - x ** 2)])

    def H(x, y):
        return np.array([[2, -4 * b * x],
                         [-4 * b * x, 2 * b]])

    return f, J, H


rosenbrock, rosenbrock_J, rosenbrock_H = rosenbrock_f(a=1, b=100)

# x, y = np.ogrid[-2:2:0.05, -0.5:3:0.05]
# z = rosenbrock(x, y).T


x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(x, y)

Z = rosenbrock(X,Y)

fig = plt.figure()
ax = fig.gca(projection='3d')

# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=True)
surf = ax.plot_surface(X, Y, Z)

plt.show()

