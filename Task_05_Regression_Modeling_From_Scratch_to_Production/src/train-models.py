from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures


def train_linear_regression(X_train, y_train):
    """Train a Linear Regression model."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def train_ridge_regression(X_train, y_train, alpha=1.0):
    """Train a Ridge Regression model."""
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("ridge", Ridge(alpha=alpha))
    ])
    model.fit(X_train, y_train)
    return model


def train_lasso_regression(X_train, y_train, alpha=0.01):
    """Train a Lasso Regression model."""
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("lasso", Lasso(alpha=alpha))
    ])
    model.fit(X_train, y_train)
    return model


def train_elasticnet_regression(X_train, y_train, alpha=0.01, l1_ratio=0.5):
    """Train an ElasticNet Regression model."""
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("elasticnet", ElasticNet(alpha=alpha, l1_ratio=l1_ratio))
    ])
    model.fit(X_train, y_train)
    return model


def train_polynomial_regression(X_train, y_train, degree=2):
    """Train a Polynomial Regression model."""
    model = Pipeline([
        ("polynomial", PolynomialFeatures(degree=degree, include_bias=False)),
        ("scaler", StandardScaler()),
        ("linear", LinearRegression())
    ])
    model.fit(X_train, y_train)
    return model


print("train_models.py created successfully.")