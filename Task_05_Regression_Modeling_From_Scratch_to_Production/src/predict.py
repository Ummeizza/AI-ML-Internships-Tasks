import numpy as np


def generate_predictions(model, X):
    """
    Generate predictions using a trained regression model.
    """
    predictions = model.predict(X)
    return np.asarray(predictions)


def calculate_prediction_error(y_true, y_pred):
    """
    Calculate prediction errors as Actual - Predicted.
    """
    return np.asarray(y_true) - np.asarray(y_pred)


print("predict.py created successfully.")