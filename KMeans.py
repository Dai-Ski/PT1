from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
data = load_iris()
X_scaled = StandardScaler().fit_transform(data.data)
km = KMeans(n_clusters=3, random_state=42, n_init='auto').fit(X_scaled)
pca_res = PCA(2).fit_transform(X_scaled)
plt.scatter(pca_res[:,0], pca_res[:,1], c=km.labels_, cmap='Set1')
plt.show()