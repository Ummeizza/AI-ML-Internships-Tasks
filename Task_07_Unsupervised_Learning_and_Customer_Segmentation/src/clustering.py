from sklearn.cluster import (
    KMeans,
    DBSCAN,
    AgglomerativeClustering
)


def apply_kmeans(X, n_clusters=6, random_state=42):
    """
    Apply K-Means clustering.
    """
    model = KMeans(
        n_clusters=n_clusters,
        random_state=random_state,
        n_init=10
    )

    labels = model.fit_predict(X)

    return model, labels


def apply_dbscan(X, eps=0.4, min_samples=5):
    """
    Apply DBSCAN clustering.
    """
    model = DBSCAN(
        eps=eps,
        min_samples=min_samples
    )

    labels = model.fit_predict(X)

    return model, labels


def apply_hierarchical(X, n_clusters=6):
    """
    Apply Agglomerative Hierarchical Clustering.
    """
    model = AgglomerativeClustering(
        n_clusters=n_clusters,
        linkage="ward"
    )

    labels = model.fit_predict(X)

    return model, labels