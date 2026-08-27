import pandas as pd


def load_data(file_path):
    """
    Load the Wine Quality dataset.

    Parameters
    ----------
    file_path : str
        Path to the dataset.

    Returns
    -------
    pandas.DataFrame
        Loaded dataset.
    """
    return pd.read_csv(file_path)


def inspect_data(df):
    """
    Return basic information about the dataset.
    """
    return {
        "shape": df.shape,
        "missing_values": df.isnull().sum(),
        "duplicates": df.duplicated().sum(),
        "dtypes": df.dtypes
    }