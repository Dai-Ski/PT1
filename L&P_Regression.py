from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline
import numpy as np
import matplotlib.pyplot as plt
housing = fetch_california_housing(as_frame=True)
X, y = housing.data[['AveRooms']], housing.target
model = LinearRegression().fit(X, y)
plt.scatter(X, y, color='red', s=2, alpha=0.5)
plt.plot(X, model.predict(X), color='blue')
plt.title("Linear: AveRooms vs Price")
plt.show()

X_p = np.sort(5 * np.random.rand(100, 1), axis=0)
y_p = 0.5 * X_p**2 + X_p + 2 + np.random.randn(100, 1)
poly = make_pipeline(PolynomialFeatures(2), StandardScaler(), LinearRegression()).fit(X_p, y_p)
plt.scatter(X_p, y_p, color='green')
plt.plot(X_p, poly.predict(X_p), color='black')
plt.title("Polynomial: X vs Y")
plt.show()