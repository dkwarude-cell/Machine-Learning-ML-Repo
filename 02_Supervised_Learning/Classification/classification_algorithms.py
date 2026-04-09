# Supervised Learning Algorithms - Classification
# Used when the output data is categorical (e.g., Yes/No, Spam/Not Spam, Multi-class labels).

# 1. Imports
# Need sklearn classifiers like LogisticRegression, SVC, etc.

# 2. Logistic Regression (*)
# Logic: Sigmoid function curve fitting to classify inputs to 0 or 1.
# Usually meant for binary classification.
# Implementation: from sklearn.linear_model import LogisticRegression

# 3. K-Nearest Neighbors (KNN) (*)
# Logic: Lazy learning algorithm. Classifies based on 'K' nearest data points in the space.
# Uses distances like Euclidean, Manhattan.
# Implementation: from sklearn.neighbors import KNeighborsClassifier

# 4. Support Vector Machine (SVM) (*)
# Logic: Finds best separating hyperplane with maximum margin between classes.
# Kernel trick for non-linear data.
# Implementation: from sklearn.svm import SVC (or SVClassifier)

# 5. Decision Tree
# Logic: Tree-based mechanism breaking data by feature thresholds (gini/entropy).
# Easy to interpret but prone to overfitting.
# Implementation: from sklearn.tree import DecisionTreeClassifier

# 6. Random Forest (*)
# Logic: Ensemble method. Builds many decision trees and votes. Reduces overfitting.
# Implementation: from sklearn.ensemble import RandomForestClassifier

# 7. Naive Bayes
# Logic: Probabilistic classifier based on Bayes' Theorem with independence assumption.
# Good for text classification.
# Implementation: from sklearn.naive_bayes import GaussianNB/MultinomialNB

# 8. Gradient Boosting
# Logic: Sequential ensemble modeling where new models correct errors of older ones.
# Implementation: from sklearn.ensemble import GradientBoostingClassifier

# 9. XGBoost (*)
# Logic: Highly optimized Gradient Boosting. Faster and usually performs better.
# Note: May need 'xgboost' separate pip installation.
# Implementation: import xgboost as xgb / from xgboost import XGBClassifier

# Start coding below:
