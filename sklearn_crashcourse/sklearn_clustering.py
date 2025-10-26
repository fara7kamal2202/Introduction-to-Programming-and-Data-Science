from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

X, _ = make_blobs(n_samples=5000, centers=5, random_state=5)
scalar = StandardScaler()
X_scaled = scalar.fit_transform(X)



kmeans = KMeans(n_clusters=5)
kmeans.fit(X_scaled)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=kmeans.labels_)
plt.show()