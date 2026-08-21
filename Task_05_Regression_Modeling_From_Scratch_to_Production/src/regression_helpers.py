import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_model(y_true, y_pred):
    """
    Calculate MAE, RMSE, and R² for a regression model.
    """

    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)

    return {
        "MAE": mae,
        "RMSE": rmse,
        "R²": r2
    }


def calculate_residuals(y_true, y_pred):
    """
    Calculate residuals as Actual - Predicted.
    """

    return np.array(y_true) - np.array(y_pred)


def prediction_interval(predictions, residual_std, z_score=1.96):
    """
    Calculate an approximate prediction interval.
    """

    margin = z_score * residual_std

    lower_bound = predictions - margin
    upper_bound = predictions + margin

    return lower_bound, upper_bound


print("regression_helpers.py created successfully.")