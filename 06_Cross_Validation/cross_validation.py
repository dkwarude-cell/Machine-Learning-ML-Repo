# Cross Validation in Machine Learning

# What is it?
# A technique to evaluate a model's generalizability by training and testing models 
# on different data sets from the same overall dataset. 
# It helps to ensure that the model doesn't just memorize the training patterns.

# 1. Holdout Method
# Logic: Simply split data into Train, Validation, and Test sets based on a specific ratio (e.g., 70:20:10).
# Example: Use `train_test_split` from sklearn twice. First for train-temp, then temp into val-test.
# Good when dataset size is very large. Not the best for smaller datasets because some data is 
# never used for training or testing depending on the split.

# 2. K-Fold Cross Validation
# Logic: Divides the dataset into "K" equally sized partitions or "folds".
# - Train the model K times. 
# - Each time, use K-1 folds for training and 1 distinct fold for testing.
# - The final score is the average of performance across all K passes.
# Example: from sklearn.model_selection import KFold, cross_val_score
# Good for smaller datasets to maximize utility of limited data.

# Note: Start your implementations and examples here 
