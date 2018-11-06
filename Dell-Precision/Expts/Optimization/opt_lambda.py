import numpy as np

y = np.array([1,2])
a = 10

f = lambda x: x[0] + a

print(f)
print(f(y))