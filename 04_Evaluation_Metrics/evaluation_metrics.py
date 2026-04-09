# Evaluation Metrics in Machine Learning

# 1. Classification Metrics
# Used for evaluating classification models where output is discrete (categories).

# Imports mapping to functions in scikit-learn
# Example: from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# -> Accuracy: Ratio of correctly predicted observations to total observations.
# -> Precision: Out of all the positive classes we have predicted correctly, how many are actually positive? (TP / (TP + FP))
# -> Recall (Sensitivity): Out of all the positive classes, how much we predicted correctly. (TP / (TP + FN))
# -> F1 Score: Harmonic mean of precision and recall. Best if precision and recall are both important.
# -> Logarithmic Loss (Log Loss): Measures the performance of a classification model where the prediction input is a probability value between 0 and 1.

# 2. Confusion Matrix (Lagbhag related to AUC/ROC)
# A table that shows actual vs. predicted values.
# Elements:
# -> True Positives (TP): We predict positive, and it's actually positive.
# -> True Negatives (TN): We predict negative, and it's actually negative.
# -> False Positives (FP): We predict positive, but it's actually negative. (Type 1 error)
# -> False Negatives (FN): We predict negative, but it's actually positive. (Type 2 error)
# Note: "5 & 6 lagbhag same hi hai, but phir bhi kuchh difference hai, just go through it."

# 3. Area Under Curve (AUC) and ROC Curve
# The ROC curve is a plot of True Positive Rate (TPR) against False Positive Rate (FPR) at various threshold settings.
# -> TPR (True Positive Rate) = Recall = TP / (TP + FN)
# -> TNR (True Negative Rate) = Specificity = TN / (TN + FP)
# -> FPR (False Positive Rate) = 1 - Specificity = FP / (FP + TN)
# -> FNR (False Negative Rate) = 1 - Sensitivity = FN / (FN + TP)
# AUC provides an aggregate measure of performance across all possible classification thresholds.

# 4. Regression Metrics
# Used for evaluating regression models where output is continuous.

# Imports: from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score (also numpy for RMSE)

# -> Mean Absolute Error (MAE): Average of the absolute difference between predicted and actual values.
# -> Mean Squared Error (MSE): Average of the squared difference between predicted and actual values. Penalizes larger errors.
# -> Root Mean Squared Error (RMSE): Square root of MSE. Keeps the unit metric same as the target.
# -> R² (R-squared / Coefficient of Determination): Represents the proportion of variance for a dependent variable that's explained by an independent variable(s).

# Note: Start your implementations and examples here 
