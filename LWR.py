import numpy as np
import matplotlib.pyplot as plt
def kernel(x, xi, tau):
    return np.exp(-np.sum((x - xi)**2) / (2 * tau**2))

def lwr(x, X, y, tau):
    weights = np.array([kernel(x, xi, tau) for xi in X])
    W = np.diag(weights)
    theta = np.linalg.inv(X.T @ W @ X) @ (X.T @ W @ y)
    return x @ theta

X = np.linspace(0, 2*np.pi, 100)
y = np.sin(X) + 0.1 * np.random.randn(100)
X_bias = np.c_[np.ones(100), X] 
x_test = np.linspace(0, 2*np.pi, 200)
y_pred = [lwr(np.array([1, xi]), X_bias, y, 0.5) for xi in x_test]

plt.scatter(X, y, color='red')
plt.plot(x_test, y_pred, color='blue')
plt.show()