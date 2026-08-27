from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier


def create_random_forest(random_state=42):
    """
    Create the baseline Random Forest classifier.
    """
    return RandomForestClassifier(
        random_state=random_state,
        n_jobs=-1
    )


def run_grid_search(model, param_grid, X_train, y_train, cv=5):
    """
    Run GridSearchCV.
    """
    search = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        cv=cv,
        scoring="accuracy",
        n_jobs=-1
    )

    search.fit(X_train, y_train)

    return search


def run_randomized_search(
    model,
    param_distributions,
    X_train,
    y_train,
    n_iter=30,
    cv=5,
    random_state=42
):
    """
    Run RandomizedSearchCV.
    """
    search = RandomizedSearchCV(
        estimator=model,
        param_distributions=param_distributions,
        n_iter=n_iter,
        cv=cv,
        scoring="accuracy",
        random_state=random_state,
        n_jobs=-1
    )

    search.fit(X_train, y_train)

    return search