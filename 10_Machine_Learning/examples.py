# Scikit-learn Example
from sklearn.linear_model import LinearRegression
import numpy as np

# Data
X = np.array([[1], [2], [3]])
y = np.array([2, 4, 6])

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction
prediction = model.predict([[4]])
print("Prediction for 4:", prediction)