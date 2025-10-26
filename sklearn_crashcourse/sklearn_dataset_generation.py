from matplotlib.pyplot import figure
from sklearn.datasets import make_blobs, make_circles
import matplotlib.pyplot as plt

X, y = make_blobs(n_samples=1000, centers=5)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()


figure()
X, y = make_circles(n_samples=1000, factor=0.5, noise=0.05)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()