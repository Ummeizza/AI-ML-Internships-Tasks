import numpy as np
import pandas as pd


def calculate_prediction_disagreement(predictions):
    models = predictions.columns

    diversity_matrix = pd.DataFrame(
        index=models,
        columns=models,
        dtype=float
    )

    for model_a in models:
        for model_b in models:
            diversity_matrix.loc[model_a, model_b] = np.mean(
                predictions[model_a] != predictions[model_b]
            )

    return diversity_matrix