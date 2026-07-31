import numpy as np

def replace_missing_values(df):
    df.replace("?", np.nan, inplace=True)
    return df

def remove_duplicates(df):
    return df.drop_duplicates()