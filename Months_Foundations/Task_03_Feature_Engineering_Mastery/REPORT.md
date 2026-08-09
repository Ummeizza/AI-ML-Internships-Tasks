# Task 03 — Feature Engineering Mastery Report

## 1. Introduction

This project focuses on improving house price prediction through feature engineering and feature selection. The House Prices - Advanced Regression dataset was used for the analysis.

The main objective was to create meaningful features from existing variables, identify the most useful predictors, and evaluate the resulting model against a baseline.

## 2. Business Objective

The real estate platform requires accurate price estimates. The business scenario states that every 5% improvement in prediction accuracy can potentially generate $800K more in annual commissions.

The target was to achieve an MAE below $18,000.

## 3. Data Processing

The dataset was loaded and inspected for data types, missing values, and relevant housing attributes. Missing numerical values were handled using appropriate imputation, while categorical variables were processed before being used for modeling.

The data was divided into training and testing sets before target encoding to avoid data leakage.

## 4. Feature Engineering

Several domain-driven features were created based on housing characteristics.

### TotalSF

`TotalSF` combines basement, first-floor, and second-floor living areas.

This provides a broader measure of the total usable floor area of a property.

### TotalBath

`TotalBath` combines full and half bathrooms, including basement bathrooms, using half-bathrooms as 0.5.

### HouseAge

`HouseAge` represents the age of a property at the time it was sold.

### RemodAge

`RemodAge` represents the number of years since the property was last remodeled.

### TotalPorchSF

`TotalPorchSF` combines the available porch and deck area variables.

These features were created to provide the model with more meaningful representations of property characteristics.

## 5. Polynomial Features

Polynomial features were generated from selected numerical variables to capture possible nonlinear relationships and interactions.

Four original features produced 14 polynomial and interaction features.

The selected features were:

- TotalSF
- TotalBath
- HouseAge
- RemodAge

## 6. Binning

The `HouseAge` feature was divided into four categories:

- New
- Mid-Age
- Old
- Very Old

This converts a continuous age variable into meaningful groups that can represent different property-age patterns.

## 7. Target Encoding

`Neighborhood` was target encoded using the mean `SalePrice` for each category.

To prevent target leakage, the encoding mapping was calculated using only the training data and then applied to the test data.

Unseen categories were handled using the training-set global mean.

## 8. Feature Selection

Three feature selection techniques were applied.

### Mutual Information

Mutual Information was used to measure the amount of information each numerical feature provided about `SalePrice`.

The highest-scoring feature was:

- `TotalSF` — 0.6372

Other highly informative features included `OverallQual`, `Neighborhood_TargetEncoded`, and `GrLivArea`.

### Recursive Feature Elimination

RFE with a Random Forest estimator was used to select 15 features.

The selected features included:

- LotFrontage
- LotArea
- OverallQual
- YearBuilt
- YearRemodAdd
- BsmtFinSF1
- BsmtUnfSF
- 2ndFlrSF
- GrLivArea
- GarageArea
- TotalSF
- TotalBath
- RemodAge
- TotalPorchSF
- Neighborhood_TargetEncoded

### L1 Regularization

L1 regularization was applied after standardizing the numerical features. Features with non-zero coefficients were retained.

The selected feature set was then examined alongside the results from Mutual Information and RFE.

## 9. Feature Importance

Random Forest feature importance was used to provide an additional model-based interpretation of the selected features.

`TotalSF` was the most important feature, followed by `OverallQual` and `Neighborhood_TargetEncoded`.

This supports the usefulness of the engineered total-area feature in house price prediction.

## 10. Model Evaluation

A Random Forest regression model was trained using the RFE-selected features.

The results were compared with the baseline model.

| Metric | Baseline | Final Model |
|---|---:|---:|
| MAE | $17,784.57 | $17,949.01 |
| RMSE | $29,477.22 | $29,134.48 |
| R² | 0.8867 | 0.8893 |

### Interpretation

The final model achieved an MAE of $17,949.01, which is below the business target of $18,000.

The MAE increased slightly compared with the baseline. However, RMSE improved from $29,477.22 to $29,134.48 and R² increased from 0.8867 to 0.8893.

Therefore, the final model met the business requirement while showing improvement in RMSE and R².

## 11. Business Impact

The model achieved the required MAE threshold of below $18,000. More accurate price estimates can help the real estate platform provide better estimates to customers and support improved commission opportunities.

The $800K figure represents the potential business impact stated in the scenario for a 5% improvement in prediction accuracy; it is not claimed as an actual measured revenue increase from this model.

## 12. Limitations

The final model's MAE was slightly higher than the baseline, so the feature engineering did not improve every evaluation metric.

The model could potentially be improved through:

- Hyperparameter tuning
- Additional domain-specific features
- Alternative ensemble models
- More systematic feature selection
- Further treatment of outliers

## 13. Conclusion

This task demonstrated an end-to-end feature engineering workflow for house price prediction.

Domain-driven features, polynomial features, binning, target encoding, Mutual Information, RFE, and L1 regularization were applied.

The final model achieved an MAE of $17,949.01, meeting the business target of below $18,000. RMSE and R² also improved compared with the baseline, demonstrating that the engineered features provided useful predictive information.