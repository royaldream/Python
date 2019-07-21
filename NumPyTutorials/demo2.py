import numpy as np

print np.__version__
a = np.array([(1, 2, 3, 4, 5, 6), (6, 7, 8, 9, 10, 11)])
print a

s = range(10)
import sys

print sys.getsizeof(1) * len(s)
# print s

d = np.arange(10)
print d.itemsize * d.size

# Dimension of Array
# a = np.array([(1, 2, 3), (4, 5, 6)])
print"dimension of array :", a.ndim
print"size of array :", a.size
print"item size of array :", a.itemsize
print"data type of array :", a.dtype
print "shape of array :", a.shape

print "reshape of array : ", a.reshape(4, 3)
print(a[0, 4])
print a[0:2, 1]

b = np.linspace(1, 3, 10)
print(b)

print "max ", a.max()
print "min ", a.min()
print "sum ", a.sum()
print "sqrt", np.sqrt(a)
print "derivation", np.std(a)
print '', np.hstack(a)
print '', np.vstack(a)

import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
print x
y = np.tan(x)
print y
plt.plot(x, y)
plt.show()
