# Salary Prediction using Decision Tree Regression

This project implements **Decision Tree Regression** to predict the salary of an employee based on their position level. By using a dataset containing position levels and their corresponding salaries, the project highlights how decision trees can capture complex relationships in data through non-linear regression. 

## Detailed Summary

The script starts by loading a dataset (`Position_Salaries.csv`) that contains employee position levels and their salaries. It trains a **Decision Tree Regressor** model using this data and makes predictions for unseen data points. The results are visualized to show how well the model fits the actual salary data.

The script performs the following steps:

1. **Data Loading and Preprocessing:**
   - Loads the dataset and separates it into independent variables (position levels) and the dependent variable (salary).
2. **Model Training:**
   - Trains a **Decision Tree Regression model** on the entire dataset. Decision trees are known for their ability to model non-linear relationships by dividing the data into regions and predicting values based on the mean of the observations in each region.
3. **Prediction:**
   - Predicts the salary for a position level of 6.5 using the trained Decision Tree model.
4. **Visualization:**
   - Visualizes the results by plotting the actual salary data points and the predicted values from the Decision Tree Regression model.
   - A high-resolution visualization is generated to capture the step-like nature of decision trees and how they fit the data.

## Key Concepts Covered

- **Decision Tree Regression:** A regression technique that splits the data into multiple decision branches to model non-linear relationships. Decision trees are non-parametric models, meaning they do not assume a specific form for the relationship between independent and dependent variables.
- **Prediction:** Uses the trained decision tree to predict a salary based on a specific position level (6.5).
- **Visualization:** Provides a visualization of the decision tree regression model, highlighting the discontinuous nature of the predictions, which is characteristic of decision trees.
- **High-Resolution Plot:** Generates a finer grid of position levels to show the step-like predictions made by decision trees.
