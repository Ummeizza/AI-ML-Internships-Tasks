# Report — Task 05: Regression Modeling From Scratch to Production

## 1. Business Problem
A PropTech startup needs a house price estimator serving ~10,000 predictions/day. Predictions within **±$30,000** of the actual value are acceptable; anything wider risks users losing trust in the app. Since the target variable (`MedHouseVal`) is expressed in units of $100,000, this threshold corresponds to **0.30 target units**.

## 2. Dataset
- **Source:** California Housing (scikit-learn built-in, `fetch_california_housing`)
- **Observations:** 20,640
- **Features:** 8 numeric predictors (e.g. `MedInc`, `HouseAge`, `AveRooms`, `Population`, `Latitude`, `Longitude`)
- **Target:** `MedHouseVal` — median house value in units of $100,000

## 3. Methodology
1. **Exploratory analysis** — dimensions, dtypes, missing values, duplicates, statistical summary, target distribution, feature–target relationships.
2. **Preprocessing** — feature/target split, train/test split, feature scaling (`StandardScaler`), leakage prevention verified (scaler fit only on training data).
3. **Baseline model** — mean-prediction baseline for comparison.
4. **Modeling** — Linear Regression, Ridge, Lasso, ElasticNet (each tuned via cross-validation for regularization strength), and Polynomial Regression (degree 2, expanding 8 features → 44).
5. **Evaluation** — MAE, RMSE, R² for every model, compared against baseline and against each other.
6. **Residual analysis** — residuals vs. predicted values, residual distribution, actual vs. predicted plots.
7. **Prediction intervals** — approximate 95% intervals from residual standard deviation.
8. **Business evaluation** — proportion of predictions within the ±$30,000 threshold.

## 4. Results

| Model | MAE | RMSE | R² |
|---|---|---|---|
| Baseline (mean) | 0.9061 | 1.1449 | -0.0002 |
| Linear Regression | 0.5332 | — | 0.5758 |
| Ridge (tuned) | ~0.53 | — | ~0.58 |
| Tuned ElasticNet | 0.5331 | 0.7451 | 0.5764 |
| **Polynomial Regression (final)** | **0.4670** | **0.6814** | **0.6457** |

**Final model: Polynomial Regression (degree 2).**
- MAE ≈ 0.467 → average prediction error ≈ **$46,700**
- R² ≈ 0.646 → explains ~64.6% of the variance in median house values
- Improvement over baseline: MAE −48.46%, RMSE −40.48%

## 5. Business Evaluation
Out of 4,128 test predictions:
- **1,849 (44.79%)** fell within the ±$30,000 acceptable threshold
- **2,279 (55.21%)** exceeded it

**Conclusion: the final model does not meet the business accuracy requirement.** While Polynomial Regression is clearly the best-performing model evaluated, more than half of individual predictions still fall outside the ±$30,000 tolerance the business needs.

## 6. Limitations
- Average prediction error (~$46,700) remains above the ±$30,000 target.
- Only 44.79% of individual predictions meet the business threshold.
- Residual analysis shows some large outlier errors and a long-tailed residual distribution.
- Polynomial expansion (8 → 44 features) increases model complexity and overfitting risk.
- Prediction intervals are approximate (residual-based) and can produce non-physical (negative) lower bounds.

## 7. Future Work
- Additional feature engineering (e.g. geospatial clustering on Latitude/Longitude, engineered ratios).
- Cross-validated search over polynomial degree and regularization jointly.
- Tree-based or ensemble regressors (Random Forest, Gradient Boosting) as a stronger candidate for the business accuracy requirement.

## 8. Reproducibility
- All modeling logic is modularized in `src/` (preprocessing, model utilities, training, prediction, evaluation).
- The notebook (`notebooks/Task_05_Regression_Modeling.ipynb`) generates and tests these modules directly, then organizes them into `src/`.
- Dataset loads directly from scikit-learn, so no external data files are required — the project runs from a clean clone with `pip install -r requirements.txt`.