import pandas as pd
from sklearn.model_selection import train_test_split


def clean_data(df):
    """
    Clean the Bank Marketing dataset.

    Removes duplicate records and converts the target variable
    from yes/no labels to binary values.
    """

    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Convert target to binary
    df["y"] = df["y"].map({"no": 0, "yes": 1})

    return df


def split_features_target(df):
    """
    Separate features and target variable.
    """

    X = df.drop(columns=["y"])
    y = df["y"]

    return X, y


def create_train_test_split(X, y, test_size=0.2, random_state=42):
    """
    Create a stratified train-test split.
    """

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )