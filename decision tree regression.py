# Decision Tree Regression

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import and load dataset
dataset = pd.read_csv("Position_Salaries")
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
