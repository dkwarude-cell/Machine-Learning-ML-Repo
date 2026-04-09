# Fundamental Concepts: Dataset Splits & Underfitting/Overfitting

# 1. Training vs Testing vs Validation
# -> Training Set: Data used to train the model so it can learn underlying patterns/weights.
# -> Validation Set: Used to tune the hyperparameters and evaluate the model iteratively during development.
#    (Think of it like a practice test before final exams).
# -> Testing Set: Completely unseen data to evaluate the final model score. Only used once! (Real Exam).
# Without a Validation set, tuning models to the Test set leaks test data into the model indirectly (Data Leakage).


# 2. Overfitting (High Variance)
# When the model performs excellently on Training data but horribly on Test data.
# It "memorizes" the noise in the training set instead of learning the generalized trend.
#
# -> Why it happens: Model is too complex compared to the amount of data available. 
#                    Training for too many epochs; deep decision trees; lacking regularization.
# -> Bias-Variance: High Variance, Low Bias. (Because changing training data changes the model completely).
# -> How to Reduce: 
#    - Get more data
#    - Feature selection (remove unnecessary dimensions)
#    - Apply Regularization (L1/L2)
#    - Cross Validation
#    - Pruning (for decision trees) or early stopping.


# 3. Underfitting (High Bias)
# When the model is too simple to capture the underlying trend. Performs poorly on both Train & Test data.
#
# -> Why it happens: Model is too simple; missing important features; stopped training too early.
# -> Bias-Variance: High Bias, Low Variance. (Because model stays same regardless of the training data changes—it assumes too much blindly).
# -> How to Reduce:
#    - Increase model complexity (e.g. from linear to polynomial)
#    - Add more relevant features / feature engineering
#    - Reduce regularizations if already applied.


# Space below for plotting Bias-Variance trade-off graphs or running examples:
