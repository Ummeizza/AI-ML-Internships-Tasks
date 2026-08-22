import pandas as pd


def load_data(path):
    """Load the heart disease dataset."""
    return pd.read_csv(path)