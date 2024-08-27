# Decision Tree Regression

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import datatree regression libraries
from sklearn.tree import DecisionTreeRegressor


# import and load dataset
dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# Training Decision Tree Regression Model on the whole dataset
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)

# predicting a new result
regressor.predict([[6.5]])

# Visualising the Polynomial Regression Results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color="red")
plt.plot(X_grid, regressor.predict(X_grid), color="blue")
plt.title("Truth or Bluff (Decision Tree Regression)")
plt.xlabel("Position level")
plt.ylabel("Salary")
plt.show()
