# Model Evaluation & Metrics

## Core Concepts
- **Classification Metrics:**
  - Accuracy, Precision, Recall (Sensitivity), Specificity, F1-Score.
  - Confusion Matrix.
  - ROC Curve (Receiver Operating Characteristic) and AUC (Area Under Curve).
  - PR Curve (Precision-Recall Curve) - when to use over ROC-AUC.
- **Regression Metrics:**
  - Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE).
  - R-squared ($R^2$) and Adjusted R-squared.
  - Mean Absolute Percentage Error (MAPE).
- **Validation Strategies:**
  - Train/Validation/Test Split.
  - K-Fold Cross Validation, Stratified K-Fold.
  - Leave-One-Out Cross Validation (LOOCV).
  - Time-series split (forward chaining).

## Common Questions
1. If you are predicting whether a patient has cancer, is it more important to have high precision or high recall?
2. What are the limitations of Accuracy as a metric?
3. What does an AUC of 0.5 indicate? What about 1.0?
