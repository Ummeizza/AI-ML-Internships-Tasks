from sklearn.ensemble import (
    RandomForestClassifier,
    BaggingClassifier,
    VotingClassifier,
    StackingClassifier
)

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier


def get_random_forest():
    return RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced",
        n_jobs=-1
    )


def get_bagging():
    return BaggingClassifier(
        estimator=DecisionTreeClassifier(
            max_depth=8,
            random_state=42
        ),
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )


def get_xgboost():
    return XGBClassifier(
        n_estimators=200,
        max_depth=5,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        eval_metric="logloss",
        n_jobs=-1
    )


def get_lightgbm():
    return LGBMClassifier(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=6,
        random_state=42,
        verbosity=-1,
        n_jobs=-1
    )


def get_catboost():
    return CatBoostClassifier(
        iterations=200,
        depth=6,
        learning_rate=0.05,
        random_seed=42,
        verbose=False
    )


def get_voting_model():
    return VotingClassifier(
        estimators=[
            ("rf", get_random_forest()),
            ("xgb", get_xgboost()),
            ("cat", get_catboost())
        ],
        voting="soft"
    )


def get_stacking_model():
    return StackingClassifier(
        estimators=[
            ("rf", get_random_forest()),
            ("xgb", get_xgboost()),
            ("cat", get_catboost())
        ],
        final_estimator=LogisticRegression(
            max_iter=1000,
            random_state=42
        ),
        cv=5,
        n_jobs=-1
    )