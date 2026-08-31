"""
Custom preprocessing utilities for the Titanic pipeline.
"""

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class FamilySizeTransformer(BaseEstimator, TransformerMixin):
    """
    Create a FamilySize feature using SibSp and Parch.

    FamilySize = SibSp + Parch + 1
    """

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        X["FamilySize"] = X["SibSp"] + X["Parch"] + 1

        return X