import numpy as np

A = np.array([[1,1],[1,1]])
x = np.array([2,3])

b = A*x

c = np.matmul(A,x)

d = np.matmul(A,np.matmul(A,x))

print(b)
print(c)
print(d)

y = np.array([1, 2, 3, 4])
y.shape = (4,1)
print(y)

y = np.zeros((2, 3, 4))
y.shape = (3, 8)
print(y)