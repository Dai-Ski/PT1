from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
data = load_breast_cancer()
clf = DecisionTreeClassifier(random_state=42).fit(data.data, data.target)
print(clf.predict([data.data[0]])) 
plt.figure(figsize=(12,8))
plot_tree(clf, filled=True, feature_names=data.feature_names)
plt.show()