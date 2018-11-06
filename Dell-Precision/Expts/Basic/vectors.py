import numpy as np

a = np.array([[1,2,6],[4,5,8],[8,3,5],[6,5,4]])
#Print first column
print(a[:,0])

#Print second row
print(a[1,:])

print [row[0] for row in a]


b = np.array([1, 2, 3])
b.shape = (3, 1)
print(b)

d = np.matmul(b.transpose(), b)
e = np.matmul(b,b.transpose())
f = b.dot(b.transpose())
print(d)
print(e)
print(f)

d
