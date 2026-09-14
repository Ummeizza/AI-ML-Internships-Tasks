# REPORT.md

# Task 13 — Time Series Forecasting Report

## 1. Introduction

This task focused on developing a time series forecasting solution for grocery sales prediction.

The business requirement was to forecast sales for the next 16 days so that a grocery chain could make better inventory ordering decisions. The project explored both traditional statistical forecasting methods and machine learning-based forecasting.

---

## 2. Business Problem

The grocery chain operates multiple stores and needs accurate demand estimates for inventory planning.

Two major risks are associated with inaccurate forecasts:

- Overforecasting can result in excess inventory and increased spoilage.
- Underforecasting can result in stockouts and lost sales.

The forecasting system should therefore provide reliable estimates of upcoming demand while minimizing prediction errors.

---

## 3. Dataset and Data Preparation

The Store Sales - Time Series Forecasting dataset was used.

The dataset contained sales records with information about dates, stores, product families, sales values, and promotions.

The following preprocessing steps were performed:

- Dataset structure was inspected.
- Missing values were identified.
- Date values were converted into datetime format.
- Invalid date values were detected and removed.
- Duplicate records were checked.
- Data was sorted chronologically.
- Sales were aggregated into total daily sales for the forecasting experiment.

The final modeling series used daily aggregated sales indexed by date.

---

## 4. Exploratory Time Series Analysis

The aggregated daily sales series was visualized to understand its overall behavior.

Rolling statistics were also calculated to examine changes in the level and variability of sales over time.

Time series decomposition was performed using a weekly period to investigate:

- Trend
- Seasonal behavior
- Residual variation

The analysis showed that sales contained temporal patterns that could be useful for forecasting.

---

## 5. Stationarity Testing

The Augmented Dickey-Fuller (ADF) test was applied to the aggregated daily sales series.

The test produced:

- **ADF Statistic:** approximately `-2.8075`
- **p-value:** approximately `0.0572`

Since the p-value was slightly above the 0.05 significance level, the series was treated as non-stationary.

This supported the use of first-order differencing for the ARIMA model.

---

## 6. Train/Test Strategy

A chronological train/test split was used.

The final **16 days** of the time series were reserved as the test period because the business requirement was to produce a 16-day forecast.

The earlier observations were used for model training.

This approach preserves the natural order of the time series and avoids using future observations to train the model.

---

## 7. Baseline Model

A simple last-value forecasting method was implemented as a baseline.

The baseline produced:

- **MAE:** approximately `127,092.76`
- **RMSE:** approximately `196,385.41`

This baseline provided a reference point for evaluating the more advanced forecasting methods.

---

## 8. ARIMA Model

An ARIMA model with configuration `(1,1,1)` was implemented.

The differencing component was selected because the ADF test indicated non-stationary behavior in the sales series.

The ARIMA model was trained using the historical training observations and used to generate predictions for the 16-day test horizon.

ARIMA provided a useful statistical benchmark, although its error was higher than the better-performing approaches in this experiment.

---

## 9. Prophet Model

Prophet was used as another forecasting approach.

The model configuration included:

- Weekly seasonality enabled
- Yearly seasonality enabled
- Daily seasonality disabled

The historical sales data was converted into Prophet's required `ds` and `y` format before training.

The model was then used to generate predictions for the 16-day test period.

Prophet performed better than the baseline and ARIMA models according to the final MAE comparison.

---

## 10. XGBoost Forecasting

XGBoost was used to model sales using supervised machine learning.

Historical sales values were converted into lag-based features.

The features included:

- `lag_1`
- `lag_7`
- `lag_14`
- `lag_28`
- `rolling_mean_7`
- `rolling_mean_14`
- `rolling_mean_28`
- `day_of_week`
- `month`
- `day`

Rolling features were calculated using shifted historical sales so that current sales were not directly used to construct their own features.

The XGBoost model was trained using chronological training data and evaluated on the final test period.

---

## 11. Time Series Cross-Validation

`TimeSeriesSplit` with five splits was used for chronological cross-validation.

Random K-fold validation was avoided because randomly mixing observations could allow future information to influence earlier training periods.

TimeSeriesSplit provides a more appropriate validation strategy for temporal data because each validation period occurs after its corresponding training period.

---

## 12. Model Comparison

The models were compared using Mean Absolute Error and Root Mean Squared Error.

The final MAE comparison showed the following order:

| Model | Relative Performance |
|---|---|
| XGBoost | Best |
| Prophet | Second |
| Baseline | Third |
| ARIMA | Fourth |

XGBoost achieved the lowest MAE among the evaluated models.

Therefore, XGBoost was selected as the final forecasting model.

---

## 13. Final Forecast

The selected XGBoost model was used to generate the final 16-day sales forecast.

The forecast provides an estimate of upcoming demand and can be used as an input for inventory planning.

The final forecast was compared visually with the actual sales values from the test period.

---

## 14. Business Interpretation

The forecasting results demonstrate the potential value of historical sales information for inventory planning.

A more accurate forecast can help the grocery chain:

- Plan inventory quantities more effectively.
- Reduce unnecessary overstock.
- Reduce food spoilage.
- Lower the risk of stockouts.
- Improve product availability.
- Support data-driven ordering decisions.

However, forecasting accuracy alone does not completely determine business value. In a production environment, the cost of overforecasting and underforecasting should also be incorporated into decision-making.

---

## 15. Limitations

The project has several limitations.

### Aggregated Forecasting

Sales were aggregated into total daily sales. Therefore, the model does not provide separate predictions for individual stores or product families.

### External Variables

Factors such as weather, holidays, local events, and changing customer behavior were not explicitly included.

### Promotion Information

Promotion data was not used as a future forecasting feature because future promotion information may not always be available at prediction time.

### Model Configuration

The ARIMA model used a simple `(1,1,1)` configuration rather than extensive parameter tuning or a complete SARIMA search.

### Evaluation Window

The final model comparison was based on one 16-day test horizon, so performance may differ during other periods.

### Production Forecasting

A real production system would require continuous monitoring, periodic retraining, and validation as new sales data becomes available.

---

## 16. Future Improvements

Future versions of the project could include:

1. Store-level forecasting.
2. Product-family-level forecasting.
3. Known future promotions as input features.
4. Holiday and special-event features.
5. Weather and external demand indicators.
6. SARIMA and other seasonal forecasting models.
7. XGBoost hyperparameter tuning.
8. Recursive multi-step forecasting.
9. Business-cost-based evaluation.
10. Continuous model monitoring and retraining.

---

## 17. Key Skills Demonstrated

This task demonstrated practical experience with:

- Time series data preprocessing
- Datetime handling
- Time series aggregation
- Exploratory time series analysis
- Rolling statistics
- ADF stationarity testing
- Time series decomposition
- ARIMA
- Prophet
- Lag feature engineering
- Rolling-window features
- XGBoost regression
- TimeSeriesSplit
- MAE and RMSE
- Forecast comparison
- Business interpretation
- Forecasting limitations and improvement planning

---

## 18. Conclusion

The project successfully developed a complete time series forecasting workflow for grocery sales.

The data was cleaned, validated, aggregated, and analyzed before applying multiple forecasting approaches. A baseline model, ARIMA, Prophet, and XGBoost were evaluated using appropriate forecasting metrics.

TimeSeriesSplit was used to preserve chronological order during machine learning validation.

Among the evaluated models, XGBoost achieved the lowest MAE on the selected 16-day test period and was therefore selected as the final model.

The project demonstrates how time series analysis and machine learning can be combined to support demand forecasting and inventory planning. Although the current solution is a prototype, it provides a strong foundation for a more detailed production forecasting system.