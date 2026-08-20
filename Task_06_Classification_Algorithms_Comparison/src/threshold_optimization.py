import numpy as np
from sklearn.metrics import confusion_matrix


def calculate_business_cost(
    y_true,
    probabilities,
    threshold,
    false_positive_cost=5,
    false_negative_cost=500
):
    """
    Calculate business cost for a classification threshold.
    """

    predictions = (
        probabilities >= threshold
    ).astype(int)

    tn, fp, fn, tp = confusion_matrix(
        y_true,
        predictions
    ).ravel()

    business_cost = (
        fp * false_positive_cost
        + fn * false_negative_cost
    )

    return {
        "Threshold": threshold,
        "True Negatives": tn,
        "False Positives": fp,
        "False Negatives": fn,
        "True Positives": tp,
        "Business Cost": business_cost
    }


def find_optimal_threshold(
    y_true,
    probabilities,
    thresholds=None,
    false_positive_cost=5,
    false_negative_cost=500
):
    """
    Find the threshold with the lowest estimated business cost.
    """

    if thresholds is None:
        thresholds = np.arange(0.05, 0.96, 0.05)

    results = []

    for threshold in thresholds:
        results.append(
            calculate_business_cost(
                y_true,
                probabilities,
                threshold,
                false_positive_cost,
                false_negative_cost
            )
        )

    best_result = min(
        results,
        key=lambda x: x["Business Cost"]
    )

    return best_result, results