# Task 03 — Feature Engineering Mastery

## Overview

This project focuses on feature engineering and feature selection for house price prediction using the House Prices - Advanced Regression dataset.

The goal is to create meaningful features from existing housing data, select the most useful predictors, and evaluate whether the engineered features can help achieve the business target of an MAE below $18,000.

## Business Scenario

A real estate platform needs accurate house price estimates. The business scenario states that every 5% improvement in prediction accuracy can potentially generate $800K more in annual commissions.

The raw-feature baseline provides an MAE of approximately $17,785. The target is to keep the final MAE below $18,000.

## Techniques Used

### Feature Engineering
- Domain-driven feature creation
- Polynomial features
- Binning
- Target encoding

### Feature Selection
- Mutual Information
- Recursive Feature Elimination (RFE)
- L1 regularization

### Model Evaluation
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² score
- Random Forest feature importance

## Engineered Features

The project creates several domain-driven features:

- `TotalSF` — total basement, first-floor, and second-floor area
- `TotalBath` — combined full, half, basement full, and basement half bathrooms
- `HouseAge` — property age at the time of sale
- `RemodAge` — years since the last remodeling
- `TotalPorchSF` — combined porch/deck area

Polynomial features and age-based bins were also created to capture nonlinear relationships.

## Feature Selection Results

Three feature selection approaches were applied:

1. Mutual Information
2. Recursive Feature Elimination
3. L1 regularization

Mutual Information identified `TotalSF` as the highest-scoring feature among the evaluated features.

RFE selected 15 features, including engineered features such as `TotalSF`, `TotalBath`, `RemodAge`, and `TotalPorchSF`.

L1 regularization retained features with non-zero coefficients under the selected regularization strength.

## Model Results

| Metric | Baseline | Final Model |
|---|---:|---:|
| MAE | $17,784.57 | $17,949.01 |
| RMSE | $29,477.22 | $29,134.48 |
| R² | 0.8867 | 0.8893 |

The final model achieved an MAE below the $18,000 business target. Although MAE increased slightly compared with the baseline, RMSE and R² improved.

## Project Structure

```text
Task_03_Feature_Engineering_Mastery/
│
├── task_03_feature_engineering.ipynb
├── README.md
├── REPORT.md
├── requirements.txt
│
├── src/
│   ├── feature_engineering.py
│   ├── feature_selection.py
│   └── modeling.py
│
└── figures/