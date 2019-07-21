import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

dataset = pd.read_csv("assets/iris.data", delimiter=',',
                      names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
# 1. sepal length in cm
#    2. sepal width in cm
#    3. petal length in cm
#    4. petal width
# print dataset
# print dataset.size

train_dataset = dataset.head(120)
test_dataset = dataset.tail(30)

X_train = train_dataset.sepal_length
Y_train = train_dataset.sepal_width

X_test = test_dataset.sepal_length
Y_test = test_dataset.sepal_width

plt.scatter(X_train, Y_train)
plt.show()
# print X_train
