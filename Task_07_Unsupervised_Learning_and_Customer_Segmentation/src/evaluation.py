from sklearn.metrics import silhouette_score


def calculate_silhouette_score(X, labels, ignore_noise=False):
    """
    Calculate the Silhouette Score.

    For DBSCAN, noise points (-1) can optionally be excluded.
    """

    if ignore_noise:
        mask = labels != -1
        X = X[mask]
        labels = labels[mask]

    unique_labels = set(labels)

    if len(unique_labels) < 2:
        return None

    return silhouette_score(X, labels)