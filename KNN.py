import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
data = np.random.rand(100)
x_train, x_test = data[:50], data[50:]
y_train = ["A" if x < 0.5 else "B" for x in x_train]

def predict(p, k):
    dist = sorted([(abs(p - x_train[i]), y_train[i]) for i in range(len(x_train))])
    top_k = [d[1] for d in dist[:k]]
    return Counter(top_k).most_common(1)[0][0]

for k in [1, 3]:
    res = [predict(p, k) for p in x_test]
    plt.figure()
    plt.scatter(x_train, [0]*50, c=["r" if y=="A" else "b" for y in y_train], label="Train")
    plt.scatter(x_test, [1]*50, c=["r" if y=="A" else "b" for y in res], marker='x', label="Test")
    plt.title(f"KNN k={k}")
    plt.show()
