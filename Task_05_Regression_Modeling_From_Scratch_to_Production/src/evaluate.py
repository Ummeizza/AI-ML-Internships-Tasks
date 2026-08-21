from regression_helpers import evaluate_model, calculate_residuals


def evaluate_predictions(y_true, y_pred):
    """
    Evaluate predictions using MAE, RMSE, and R².
    """
    metrics = evaluate_model(y_true, y_pred)
    return metrics


def get_residuals(y_true, y_pred):
    """
    Calculate residuals for a regression model.
    """
    return calculate_residuals(y_true, y_pred)


def print_evaluation_results(model_name, y_true, y_pred):
    """
    Print regression evaluation results.
    """
    metrics = evaluate_model(y_true, y_pred)

    print(f"Model: {model_name}")
    print(f"MAE: {metrics['MAE']:.6f}")
    print(f"RMSE: {metrics['RMSE']:.6f}")
    print(f"R²: {metrics['R²']:.6f}")

    return metrics


print("evaluate.py created successfully.")