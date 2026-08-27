from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def split_features_target(df, target_column="quality"):
    """
    Separate input features and target variable.
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]

    return X, y


def create_train_test_split(X, y, test_size=0.2, random_state=42):
    """
    Split the dataset into training and testing sets.
    """
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )


def scale_features(X_train, X_test):
    """
    Standardize training and testing features.
    """
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, scaler