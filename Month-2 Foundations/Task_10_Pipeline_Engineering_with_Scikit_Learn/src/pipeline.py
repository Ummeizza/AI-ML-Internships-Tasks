"""
Machine learning pipeline construction for Titanic survival prediction.
"""

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier

from preprocessing import FamilySizeTransformer


def create_pipeline(random_state=42):
    """
    Create the complete Titanic machine learning pipeline.

    Returns
    -------
    sklearn.pipeline.Pipeline
        Configured preprocessing and classification pipeline.
    """

    numeric_features = [
        "Pclass",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "FamilySize"
    ]

    categorical_features = [
        "Sex",
        "Embarked"
    ]

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, numeric_features),
            ("cat", categorical_pipeline, categorical_features)
        ]
    )

    pipeline = Pipeline(
        steps=[
            ("feature_engineering", FamilySizeTransformer()),
            ("preprocessing", preprocessor),
            (
                "model",
                RandomForestClassifier(
                    n_estimators=200,
                    random_state=random_state,
                    class_weight="balanced"
                )
            )
        ]
    )

    return pipeline