from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)


def evaluate_model(y_true, y_pred):
    """
    Calculate classification metrics.
    """
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0
        ),
        "recall": recall_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0
        ),
        "f1_score": f1_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0
        )
    }


def print_evaluation_results(y_true, y_pred):
    """
    Print evaluation metrics and classification report.
    """
    results = evaluate_model(y_true, y_pred)

    print("Accuracy:", round(results["accuracy"], 4))
    print("Precision:", round(results["precision"], 4))
    print("Recall:", round(results["recall"], 4))
    print("F1 Score:", round(results["f1_score"], 4))

    print("\nClassification Report")
    print(classification_report(
        y_true,
        y_pred,
        zero_division=0
    ))