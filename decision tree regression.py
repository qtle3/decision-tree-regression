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
