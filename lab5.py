import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Generate data
data = np.random.rand(100)
labels = ["Class1" if x <= 0.5 else "Class2" for x in data[:50]]

train_data = data[:50]
train_labels = labels
test_data = data[50:]

def knn(train_data, train_labels, test_point, k):
    distances = [(abs(test_point - train_data[i]), train_labels[i]) 
                 for i in range(len(train_data))]
    distances.sort()
    k_labels = [label for _, label in distances[:k]]
    return Counter(k_labels).most_common(1)[0][0]

k_values = [1, 3, 5, 20]

for k in k_values:
    print(f"\nResults for k = {k}")
    classified = [knn(train_data, train_labels, x, k) for x in test_data]

    for i, label in enumerate(classified):
        print(f"x{i+51}: {test_data[i]:.4f} -> {label}")

    # Visualization
    class1 = [test_data[i] for i in range(len(test_data)) if classified[i] == "Class1"]
    class2 = [test_data[i] for i in range(len(test_data)) if classified[i] == "Class2"]

    plt.figure()
    plt.scatter(train_data, [0]*len(train_data),
                c=["blue" if l=="Class1" else "red" for l in train_labels],
                label="Train")

    plt.scatter(class1, [1]*len(class1), c="blue", marker="x", label="Class1 Test")
    plt.scatter(class2, [1]*len(class2), c="red", marker="x", label="Class2 Test")

    plt.title(f"k-NN (k={k})")
    plt.legend()
    plt.show()