import numpy as np
import pandas as pd
from sklearn.feature_selection import mutual_info_regression, RFE
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler


def mutual_information_selection(X, y):
    """Rank numerical features using mutual information."""
    data = X.select_dtypes(include=np.number).copy()
    data = data.fillna(data.median())

    scores = mutual_info_regression(
        data,
        y,
        random_state=42
    )

    return pd.DataFrame({
        "Feature": data.columns,
        "Mutual_Information": scores
    }).sort_values(
        "Mutual_Information",
        ascending=False
    )


def rfe_selection(X, y, n_features=15):
    """Select important features using Recursive Feature Elimination."""
    data = X.select_dtypes(include=np.number).copy()
    data = data.fillna(data.median())

    estimator = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

    rfe = RFE(
        estimator=estimator,
        n_features_to_select=n_features,
        step=1
    )

    rfe.fit(data, y)

    results = pd.DataFrame({
        "Feature": data.columns,
        "Selected": rfe.support_,
        "Ranking": rfe.ranking_
    })

    selected_features = data.columns[rfe.support_].tolist()

    return results, selected_features


def l1_selection(X, y, alpha=0.01):
    """Select features using L1 regularization."""
    data = X.select_dtypes(include=np.number).copy()
    data = data.fillna(data.median())

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    model = Lasso(
        alpha=alpha,
        max_iter=10000,
        random_state=42
    )

    model.fit(scaled_data, y)

    results = pd.DataFrame({
        "Feature": data.columns,
        "Coefficient": model.coef_
    })

    results["Absolute_Coefficient"] = (
        results["Coefficient"].abs()
    )

    selected_features = results[
        results["Coefficient"] != 0
    ]["Feature"].tolist()

    return results.sort_values(
        "Absolute_Coefficient",
        ascending=False
    ), selected_features