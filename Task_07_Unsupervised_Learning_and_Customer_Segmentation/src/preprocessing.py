import pandas as pd
from sklearn.preprocessing import StandardScaler


def select_features(df):
    """
    Select numerical features used for customer segmentation.
    """
    features = [
        "Age",
        "Annual Income (k$)",
        "Spending Score (1-100)"
    ]

    return df[features].copy()


def scale_features(features):
    """
    Standardize clustering features using StandardScaler.
    """
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    return scaled_features, scaler