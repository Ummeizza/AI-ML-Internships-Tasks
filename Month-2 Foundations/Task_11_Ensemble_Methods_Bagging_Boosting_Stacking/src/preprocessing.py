import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


def engineer_features(df):
    data = df.copy()

    # Split cabin information
    data[["Deck", "CabinNum", "Side"]] = data["Cabin"].str.split(
        "/", expand=True
    )

    data["CabinNum"] = pd.to_numeric(
        data["CabinNum"],
        errors="coerce"
    )

    # Total spending
    spending_cols = [
        "RoomService",
        "FoodCourt",
        "ShoppingMall",
        "Spa",
        "VRDeck"
    ]

    data["TotalSpending"] = data[spending_cols].sum(axis=1)

    # Travel group information
    data["GroupId"] = data["PassengerId"].str.split("_").str[0]

    group_counts = data["GroupId"].value_counts()
    data["GroupSize"] = data["GroupId"].map(group_counts)

    # Remove identifiers
    data = data.drop(
        columns=[
            "PassengerId",
            "Name",
            "Cabin",
            "GroupId"
        ]
    )

    return data


def create_preprocessor(X):
    numeric_features = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    categorical_features = X.select_dtypes(
        include=["object", "bool"]
    ).columns.tolist()

    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(
            handle_unknown="ignore",
            sparse_output=False
        ))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features)
        ]
    )

    return preprocessor