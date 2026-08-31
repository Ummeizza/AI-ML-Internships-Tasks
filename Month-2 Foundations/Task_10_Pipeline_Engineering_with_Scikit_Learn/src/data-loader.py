"""
Data loading utilities for the Titanic pipeline.
"""

import pandas as pd


def load_titanic_data(file_path):
    """
    Load the Titanic dataset from a CSV file.

    Parameters
    ----------
    file_path : str
        Path to the Titanic CSV file.

    Returns
    -------
    pandas.DataFrame
        Loaded Titanic dataset.
    """
    return pd.read_csv(file_path)