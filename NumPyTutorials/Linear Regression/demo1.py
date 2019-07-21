import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.random.rand(100, 1)
y = 2 + (3 * x) + np.random.rand(100, 1)
print x
print y

plt.scatter(x, y, s=5, color="b")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

