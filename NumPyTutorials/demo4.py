import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 1, 0.1)
print x

print "square of x"
y = x ** 2
print y
plt.plot(x, y)
# plt.legend()
plt.show()

print "qube of x"
y = x ** 3
print y
plt.plot(x, y)
plt.show()

print "sqrt of x"
y = np.sqrt(x)
print y
plt.xlabel("x")
plt.ylabel("sqrt")
plt.legend()
plt.plot(x, y)
plt.show()


