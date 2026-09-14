import numpy as np
import pandas as pd


def calculate_rmse(y_true, y_pred):
    return np.sqrt(np.mean((np.asarray(y_true) - np.asarray(y_pred)) ** 2))


def create_lag_features(
    series,
    lags=(1, 7, 14, 28),
    rolling_windows=(7, 14, 28)
):
    data = pd.DataFrame({"sales": series.copy()})

    for lag in lags:
        data[f"lag_{lag}"] = data["sales"].shift(lag)

    for window in rolling_windows:
        data[f"rolling_mean_{window}"] = (
            data["sales"]
            .shift(1)
            .rolling(window)
            .mean()
        )

    data["day_of_week"] = data.index.dayofweek
    data["month"] = data.index.month
    data["day"] = data.index.day

    return data.dropna()