from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit

data = load_iris()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

split = StratifiedShuffleSplit(n_splits=5, test_size=0.2)

for train_index, test_index in split.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

counts = np.bincount(y_train)
positions = np.arange(3)

plt.bar(positions, counts)
plt.xticks(positions, data.target_names )

plt.show()