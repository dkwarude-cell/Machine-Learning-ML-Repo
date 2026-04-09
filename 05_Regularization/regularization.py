# Regularization in Machine Learning

# What is it? 
# A technique used to prevent models from overfitting the training data.
# It does this by adding a penalty term to the learning model's loss function to discourage complex models.
# Goal is to make predictions on test data better without losing training set performance.

# Why is it required?
# Helps address the Bias-Variance tradeoff when the model suffers from high variance (overfitting).
# Makes models more robust against noise.

# Types of Regularization:
# 1. Lasso Regression (L1 Penalty)
# Adds the absolute value of magnitude of coefficient as penalty term.
# Note: Useful for feature selection because it can shrink coefficients down strictly to zero.
# Example: from sklearn.linear_model import Lasso

# 2. Ridge Regression (L2 Penalty)
# Adds the squared magnitude of coefficient as penalty term.
# Note: Punishes large weights but doesn't set them exactly to zero. Good for multi-collinearity.
# Example: from sklearn.linear_model import Ridge

# 3. Elastic Net Regression
# A combination of both L1 and L2 penalties. You have a mixing hyperparameter to choose the ratio.
# Example: from sklearn.linear_model import ElasticNet

# Implementation space below:
