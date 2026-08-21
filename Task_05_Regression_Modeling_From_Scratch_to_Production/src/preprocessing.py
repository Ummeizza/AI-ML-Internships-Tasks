import numpy as np
from sklearn.model_selection import train_test_split


def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split features and target into training and testing sets.
    """
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state
    )


def check_missing_values(X):
    """
    Check the total number of missing values in the dataset.
    """
    return np.sum(np.isnan(X))


print("preprocessing.py created successfully.")