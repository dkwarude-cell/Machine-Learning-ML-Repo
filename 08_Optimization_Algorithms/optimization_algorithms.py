# Optimization Algorithms in Machine Learning 
# Central purpose: Used to train models efficiently by minimizing the Cost Function / Loss Function.

# 1. Gradient Descent (Vanilla/Batch)
# -> Logic: The classic algorithm that calculates the error for the ENTIRE dataset 
#    before updating the model's weights.
# -> Direction: It calculates the gradient (derivative) of the loss function with respect to parameters,
#    then takes a step proportional to the negative of the gradient. (Stepping down the 'valley').
# -> Pros: Stable error gradient, guaranteed convergence for convex functions.
# -> Cons: Very slow on large datasets because it has to process everything before 1 update step.


# 2. Stochastic Gradient Descent (SGD)
# -> Logic: Instead of computing the gradient for the whole dataset, SGD does it for 
#    EACH individual data point, updating the weights instantly.
# -> Pros: Much faster on massive datasets. Updates are frequent.
# -> Cons: The updates are 'noisy' (stochastic), meaning the loss function fluctuates heavily. 
#    Might bounce around the minimum instead of converging cleanly.
# Example: from sklearn.linear_model import SGDRegressor, SGDClassifier


# 3. Mini-Batch Gradient Descent (often just called SGD in libraries)
# -> The sweet spot. Updates weights after evaluating a "batch" (e.g., 32, 64, 128 items) of data.
# -> Combines stability of Batch GD with the speed of SGD.


# 4. Adam Optimizer (Adaptive Moment Estimation)
# -> Logic: Very popular, especially in Deep Learning. It computes adaptive learning rates for each parameter.
#    Instead of a single learning rate (alpha) over all weights, Adam stores an exponentially
#    decaying average of past squared gradients (like RMSprop) and past gradients (like Momentum).
# -> Pros: Generally requires less hyperparameter tuning and is highly efficient.

# Space for custom optimizer tests or implementations: 
