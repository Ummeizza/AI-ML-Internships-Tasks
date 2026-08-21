from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures


def create_linear_model():
    """Create a Linear Regression model."""
    return LinearRegression()


def create_ridge_model(alpha=1.0):
    """Create a Ridge Regression model with scaling."""
    return Pipeline([
        ("scaler", StandardScaler()),
        ("ridge", Ridge(alpha=alpha))
    ])


def create_lasso_model(alpha=0.01):
    """Create a Lasso Regression model with scaling."""
    return Pipeline([
        ("scaler", StandardScaler()),
        ("lasso", Lasso(alpha=alpha))
    ])


def create_elasticnet_model(alpha=0.01, l1_ratio=0.5):
    """Create an ElasticNet Regression model with scaling."""
    return Pipeline([
        ("scaler", StandardScaler()),
        ("elasticnet", ElasticNet(alpha=alpha, l1_ratio=l1_ratio))
    ])


def create_polynomial_model(degree=2):
    """Create a Polynomial Regression model with scaling."""
    return Pipeline([
        ("polynomial", PolynomialFeatures(degree=degree, include_bias=False)),
        ("scaler", StandardScaler()),
        ("linear", LinearRegression())
    ])


print("model_utils.py created successfully.")