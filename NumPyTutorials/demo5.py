import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 10, 1)
print x

y = x ** 2

plt.scatter(x, y, label="square", color='b')


plt.show()
