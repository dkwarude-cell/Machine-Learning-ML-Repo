# Feature Engineering & Data Preprocessing

## Core Concepts
- **Handling Missing Data:** Deletion (listwise/pairwise), Imputation (mean, median, mode), Model-based imputation (KNN, iterative).
- **Categorical Encoding:** One-Hot Encoding, Label Encoding, Target Encoding, Frequency Encoding, Embedding layers.
- **Feature Scaling:** Standardization (Z-score normalization), Min-Max Scaling, Robust Scaling (to handle outliers).
- **Handling Outliers:** Z-score method, IQR method, Isolation Forest, capping/clipping.
- **Feature Selection:** Filter methods (correlation, Chi-square), Wrapper methods (forward/backward selection), Embedded methods (Lasso/L1 penalty).
- **Feature Extraction:** Creating new features from datetime (day of week, month), text (TF-IDF, word embeddings), interactions between variables.

## Common Questions
1. Why is feature scaling important for PCA and KNN, but not for Decision Trees?
2. What is the "dummy variable trap" in One-Hot Encoding?
3. How would you handle a categorical variable with hundreds of unique levels (high cardinality)?
