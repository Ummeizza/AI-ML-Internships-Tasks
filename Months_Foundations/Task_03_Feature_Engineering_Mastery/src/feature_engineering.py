import pandas as pd


def create_features(df):
    """
    Create domain-driven features for house price prediction.
    """
    data = df.copy()

    data["TotalSF"] = (
        data["TotalBsmtSF"].fillna(0)
        + data["1stFlrSF"].fillna(0)
        + data["2ndFlrSF"].fillna(0)
    )

    data["TotalBath"] = (
        data["FullBath"].fillna(0)
        + 0.5 * data["HalfBath"].fillna(0)
        + data["BsmtFullBath"].fillna(0)
        + 0.5 * data["BsmtHalfBath"].fillna(0)
    )

    data["HouseAge"] = data["YrSold"] - data["YearBuilt"]

    data["RemodAge"] = data["YrSold"] - data["YearRemodAdd"]

    porch_columns = [
        "OpenPorchSF",
        "3SsnPorch",
        "EnclosedPorch",
        "ScreenPorch",
        "WoodDeckSF"
    ]

    data["TotalPorchSF"] = data[porch_columns].fillna(0).sum(axis=1)

    return data