from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)


def evaluate_classifier(y_true, y_pred, y_prob, positive_label="Yes"):
    """Calculate classification metrics."""
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(
            y_true, y_pred,
            pos_label=positive_label,
            zero_division=0
        ),
        "recall": recall_score(
            y_true, y_pred,
            pos_label=positive_label,
            zero_division=0
        ),
        "f1": f1_score(
            y_true, y_pred,
            pos_label=positive_label,
            zero_division=0
        ),
        "roc_auc": roc_auc_score(
            y_true,
            y_prob
        )
    }