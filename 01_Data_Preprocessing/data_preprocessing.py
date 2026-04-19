# Data Preprocessing steps

# 1. Import necessary libraries
# We will need pandas for data manipulation, and components from sklearn.

# 2. Load the dataset
# Read your dataset (e.g., CSV file) using pandas.

# 3. Handling missing data
# Check for null values.
# Options: Drop the rows/columns with missing values or impute them (mean, median, mode).

# 4. Handling outliers
# Identify outliers (using Boxplot, Z-score, or IQR).
# Action: Cap/trim them or remove the rows.

# 5. Feature scaling (Normalization & Standardization)
# Normalization: Scale features to a range usually [0, 1] (MinMaxScaler).
# Standardization: Scale to mean 0 and standard deviation 1 (StandardScaler).

# 6. Feature Selection
# Drop irrelevant columns or use techniques like SelectKBest to keep the most important features.

# 7. Feature Extraction / Dimensionality Reduction
# Use techniques like PCA to reduce the number of features if there are too many, 
# while retaining the variance.

# 8. Train/Test split
# Split the dataset into training and testing sets (e.g., 80% train, 20% test).
# Use train_test_split from sklearn.model_selection.

# Note: Add the actual implementation below.
# 1. Import necessary libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.decomposition import PCA

import os

# 2. Load the dataset
# df = pd.read_csv("your_dataset.csv")
file_path = os.path.join(os.path.dirname(__file__), "your_dataset.csv")
df = pd.read_csv(file_path)

# Display basic info
print(df.head())
print(df.info())

# 3. Handling missing data
# Separate features and target (assuming 'target' column exists)
X = df.drop('target', axis=1)
y = df['target']

# Impute missing values (mean strategy)
imputer = SimpleImputer(strategy='mean')
X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# 4. Handling outliers (using IQR method)
Q1 = X_imputed.quantile(0.25)
Q3 = X_imputed.quantile(0.75)
IQR = Q3 - Q1

# Filter out outliers
X_no_outliers = X_imputed[~((X_imputed < (Q1 - 1.5 * IQR)) | 
                           (X_imputed > (Q3 + 1.5 * IQR))).any(axis=1)]

# Align target variable
y = y[X_no_outliers.index]

# 5. Feature Scaling
# Choose ONE depending on use case

# (A) Standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_no_outliers)

# (B) OR Normalization
# scaler = MinMaxScaler()
# X_scaled = scaler.fit_transform(X_no_outliers)

# Convert back to DataFrame
X_scaled = pd.DataFrame(X_scaled, columns=X_no_outliers.columns)

# 6. Feature Selection
selector = SelectKBest(score_func=f_regression, k=5)  # select top 5 features
X_selected = selector.fit_transform(X_scaled, y)

# Get selected feature names
selected_features = X_scaled.columns[selector.get_support()]
X_selected = pd.DataFrame(X_selected, columns=selected_features)

print("Selected Features:", selected_features)

# 7. Dimensionality Reduction (PCA)
pca = PCA(n_components=2)  # reduce to 2 components
X_pca = pca.fit_transform(X_selected)

X_pca = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])

print("Explained Variance Ratio:", pca.explained_variance_ratio_)

# 8. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_pca, y, test_size=0.2, random_state=42
)

print("Training set size:", X_train.shape)
print("Testing set size:", X_test.shape)