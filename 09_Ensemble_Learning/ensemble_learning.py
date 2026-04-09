# Ensemble Learning
# What is it? Combining multiple base models (weak learners) to produce one optimal predictive model (strong learner).

# 1. Bagging (Bootstrap Aggregating)
# -> Logic: Creates multiple subsets of the training data using replacement. 
#    Trains models in parallel on these subsets and aggregates their predictions (majority vote for Classif, average for Reg).
# -> Helps: Reduce Variance (prevents overfitting).
# -> Example: from sklearn.ensemble import BaggingClassifier


# 2. Random Forest
# -> Logic: The most famous Bagging algorithm. It uses Decision Trees as weak learners.
#    Not only does it sample data with replacement, it also selects a random subset of features
#    for every split. This ensures trees are uncorrelated.
# -> Example: from sklearn.ensemble import RandomForestClassifier


# 3. Boosting
# -> Logic: Models are trained sequentially. Each subsequent model tries to correct the errors 
#    made by the previous model by assigning higher weights to misclassified points.
# -> Helps: Reduce Bias (builds highly accurate models if no noise is present).


# 4. Gradient Boosting
# -> Logic: A specific Boosting strategy where each new model is built to predict the "residuals/errors" 
#    of the prior model, basically running gradient descent on the errors.
# -> Example: from sklearn.ensemble import GradientBoostingClassifier


# 5. AdaBoost (Adaptive Boosting)
# -> Logic: It assigns "weights" to individual samples. If a sample is classified incorrectly, 
#    its weight is increased so the next tree focuses more on it. Works sequentially.
# -> Example: from sklearn.ensemble import AdaBoostClassifier


# 6. Stacking
# -> Logic: Multiple diverse base models (e.g. SVM, KNN, Random Forest) are trained first.
#    Then, their PREDICTIONS are used as input features to a final "Meta-Model" (e.g. Logistic Regression)
#    which learns how best to combine the initial predictions.
# -> Example: from sklearn.ensemble import StackingClassifier

# Implementation sections for these: 
