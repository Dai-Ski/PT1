from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
iris = load_iris()
pca = PCA(n_components=2)
res = pca.fit_transform(iris.data)
colors = ['r', 'g', 'b']
for i, name in enumerate(iris.target_names):
    plt.scatter(res[iris.target == i, 0], res[iris.target == i, 1], 
                label=name, color=colors[i])
plt.legend()
plt.grid()
plt.show()
