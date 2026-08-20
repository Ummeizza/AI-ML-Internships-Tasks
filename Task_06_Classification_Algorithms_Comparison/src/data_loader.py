import pandas as pd


def load_bank_marketing_data(filepath):
    """
    Load the Bank Marketing dataset.

    Parameters
    ----------
    filepath : str
        Path to the CSV dataset.

    Returns
    -------
    pandas.DataFrame
        Loaded dataset.
    """
    df = pd.read_csv(filepath, sep=";")

    return df