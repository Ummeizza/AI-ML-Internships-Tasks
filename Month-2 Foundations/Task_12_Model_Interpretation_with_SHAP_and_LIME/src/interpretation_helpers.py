import numpy as np
import pandas as pd


def calculate_shap_importance(shap_values, feature_names):
    """
    Calculate mean absolute SHAP importance for each feature.
    """
    mean_abs_shap = np.abs(shap_values).mean(axis=0)

    return (
        pd.DataFrame({
            "Feature": feature_names,
            "Mean_Absolute_SHAP": mean_abs_shap
        })
        .sort_values(
            by="Mean_Absolute_SHAP",
            ascending=False
        )
        .reset_index(drop=True)
    )


def get_local_shap_contributions(
    shap_values,
    feature_names,
    sample_index=0
):
    """
    Return local SHAP contributions for one observation.
    """
    local_df = pd.DataFrame({
        "Feature": feature_names,
        "SHAP_Value": shap_values[sample_index]
    })

    local_df["Absolute_SHAP"] = np.abs(
        local_df["SHAP_Value"]
    )

    return local_df.sort_values(
        by="Absolute_SHAP",
        ascending=False
    ).reset_index(drop=True)


def calculate_group_metrics(
    y_true,
    y_pred,
    group_values
):
    """
    Calculate basic prediction metrics for each group.
    """
    from sklearn.metrics import (
        accuracy_score,
        precision_score,
        recall_score,
        f1_score
    )

    results = []

    for group in sorted(group_values.unique()):
        mask = group_values == group

        results.append({
            "Group": group,
            "Samples": int(mask.sum()),
            "Accuracy": accuracy_score(
                y_true[mask],
                y_pred[mask]
            ),
            "Precision": precision_score(
                y_true[mask],
                y_pred[mask],
                zero_division=0
            ),
            "Recall": recall_score(
                y_true[mask],
                y_pred[mask],
                zero_division=0
            ),
            "F1_Score": f1_score(
                y_true[mask],
                y_pred[mask],
                zero_division=0
            ),
            "Positive_Prediction_Rate": y_pred[mask].mean()
        })

    return pd.DataFrame(results)