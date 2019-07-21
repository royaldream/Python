import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 10, 0.2)
print x

y_sqrt = np.sqrt(x)
y_square = x ** 2
y_quabe = x ** 3
plt.plot([], [], color="m", label='sqrt')
plt.plot([], [], color="c", label='square')
plt.plot([], [], color="r", label='qube')
plt.stackplot(x, y_sqrt, y_square, y_quabe, colors=['m', 'c', 'r'])
plt.xlabel('x')

plt.ylabel('y')
plt.title("Graph")
plt.legend()
plt.show()
