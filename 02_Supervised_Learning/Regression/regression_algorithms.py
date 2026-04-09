# Supervised Learning Algorithms - Regression
# Used when the target output is continuous.

# 1. Imports
# Import libraries like sklearn, pandas, numpy, and matplotlib or seaborn for later plotting.
# Include datasets or create dummy ones for regression testing.

# 2. Linear Regression (*)
# Single independent and single dependent variable.
# Logic: Find best-fit line by minimizing sum of squares 
# Implementation: from sklearn.linear_model import LinearRegression

# 3. Multiple Linear Regression (*)
# Multiple independent variables and single dependent variable.
# Logic: Same as simple linear just extended to multidimensional spaces.
# Implementation: from sklearn.linear_model import LinearRegression

# 4. Polynomial Regression (*)
# Logic: Model relationship as an nth degree polynomial.
# Implementation: Use PolynomialFeatures combined with LinearRegression.
# e.g., from sklearn.preprocessing import PolynomialFeatures

# 5. Ridge Regression
# Note: Has L2 penalty added to the loss function. Good for multicollinearity.
# Implementation: from sklearn.linear_model import Ridge

# 6. Lasso Regression
# Note: Has L1 penalty, leads to feature selection by shrinking coeffs to 0. 
# Implementation: from sklearn.linear_model import Lasso

# Implementation space below:
