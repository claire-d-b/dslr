from math import e
from numpy import dot, log, zeros, array, clip, isnan

# Sigmoid function
def sigmoid(z):
    z = clip(z, -500, 500)  # Prevent extreme values
    return 1 / (1 + e ** -z)

# Manual logistic regression function
def train_model(scores, houses, learning_rate=0.01, epochs=1000):
    # Initialize parameters (weights and bias)
    m, n = scores.shape  # m: number of samples, n: number of features
    w = zeros(n)  # Weights initialized to 0
    b = 0  # Bias initialized to 0
    houses = array(houses)
    scores = array(scores)

    epsilon = 1e-7  # Small constant to prevent log(0)

    # Gradient descent loop
    for epoch in range(epochs):
        # Forward pass: Compute predictions
        z = dot(scores, w) + b  # Linear part: w.X + b
        y_pred = sigmoid(z)  # Sigmoid activation

        # Assuming m is the number of samples, houses is your true target vector, y_pred is your predicted probabilities
        y_pred = clip(y_pred, epsilon, 1 - epsilon) # Clip the predictions to a range to prevent log(0)

        # Compute cost (Binary Cross-Entropy Loss)
        cost = -(1/m) * sum(houses * log(y_pred) + (1 - houses) * log(1 - y_pred))

        # Backward pass: Compute gradients
        dw = (1/m) * dot(scores.T, (y_pred - houses))  # Gradient of weights
        db = (1/m) * sum(y_pred - houses)        # Gradient of bias

        # Update parameters
        w -= learning_rate * dw
        b -= learning_rate * db

        # Check for NaN
        if isnan(w).any() or isnan(b):
            print("NaN encountered during training at epoch:", epoch)
            break
        # Print cost every 100 epochs for monitoring
        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Cost: {cost}")

    return w, b


# Make predictions
def predict(scores, w, b):
    z = dot(scores, w) + b
    y_pred = sigmoid(z)
    return [1 if p > 0.5 else 0 for p in y_pred]

# Make predictions
def predict_real(scores, w, b):
    z = dot(scores, w) + b
    y_pred = sigmoid(z)
    return [p for p in y_pred]
