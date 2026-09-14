# Task 13 — Time Series Forecasting

## Overview

This task focuses on building a complete time series forecasting workflow for grocery sales prediction.

The project uses historical grocery sales data to forecast sales for the next 16 days. Different statistical and machine learning approaches were explored and compared, including a simple baseline, ARIMA, Prophet, and XGBoost.

The main objective was to understand time series behavior, handle temporal data correctly, evaluate forecasting models, and select a suitable model for future demand prediction.

---

## Business Scenario

A grocery chain operates 54 stores and needs accurate 16-day sales forecasts to support inventory ordering decisions.

Forecasting errors can have direct business consequences:

- Overforecasting can lead to excess inventory and food spoilage.
- Underforecasting can cause stockouts and lost sales.

Therefore, a reliable forecasting system can help the business make better inventory decisions and balance product availability with waste reduction.

---

## Dataset

The project uses the **Store Sales - Time Series Forecasting** dataset.

The original dataset contains the following main fields:

- `id` — Record identifier
- `date` — Sales date
- `store_nbr` — Store number
- `family` — Product family
- `sales` — Sales amount
- `onpromotion` — Promotion information

The dataset was cleaned and validated before modeling.

A corrupted date value was detected during date conversion and was handled using error-coercion and row removal rather than guessing the correct date.

For the main forecasting experiment, sales were aggregated into total daily sales.

---

## Objectives

The main objectives of this task were to:

- Clean and validate time series data.
- Convert and organize date information correctly.
- Aggregate sales into a daily time series.
- Analyze trends and rolling statistics.
- Test stationarity using the Augmented Dickey-Fuller (ADF) test.
- Perform time series decomposition.
- Build an ARIMA forecasting model.
- Set up Prophet for forecasting.
- Create lag and rolling-window features.
- Train an XGBoost regression model.
- Use TimeSeriesSplit for chronological validation.
- Compare forecasting models using MAE and RMSE.
- Select the best-performing model.
- Generate a final 16-day sales forecast.
- Discuss business implications and limitations.

---

## Workflow

The forecasting workflow followed these major stages:

1. Dataset loading
2. Initial data inspection
3. Date cleaning and validation
4. Missing-value analysis
5. Daily sales aggregation
6. Time series visualization
7. Rolling statistics analysis
8. Stationarity testing
9. Time series decomposition
10. Train/test splitting
11. Baseline forecasting
12. ARIMA modeling
13. Prophet forecasting
14. Lag-feature engineering
15. XGBoost modeling
16. TimeSeriesSplit validation
17. Model comparison
18. Final model selection
19. 16-day forecasting
20. Business interpretation and limitations

---

## Stationarity Analysis

The Augmented Dickey-Fuller test was applied to the aggregated daily sales series.

The test produced a p-value of approximately **0.0572**, which is slightly above the 0.05 significance level.

Therefore, the series was treated as non-stationary for the ARIMA model, and first-order differencing was used through the ARIMA configuration.

---

## Models Evaluated

### 1. Baseline

A simple last-value forecasting approach was used as a reference point.

This provides a basic benchmark against which the more advanced models can be compared.

### 2. ARIMA

An ARIMA model with configuration `(1, 1, 1)` was implemented.

The first-order differencing component was selected because the aggregated sales series was considered non-stationary according to the ADF test.

### 3. Prophet

Prophet was configured with:

- Weekly seasonality
- Yearly seasonality
- Daily seasonality disabled

The model was trained using the historical daily sales series and used to generate predictions for the 16-day test period.

### 4. XGBoost

XGBoost was trained using historical and calendar-based features, including:

- Lag 1
- Lag 7
- Lag 14
- Lag 28
- 7-day rolling mean
- 14-day rolling mean
- 28-day rolling mean
- Day of week
- Month
- Day of month

This approach allows the machine learning model to learn patterns from previous sales observations and calendar information.

---

## Validation

TimeSeriesSplit was used instead of random cross-validation because time series data must preserve chronological order.

Five chronological folds were used to evaluate the XGBoost approach.

This prevents future observations from being randomly mixed with past observations during validation.

---

## Evaluation Metrics

The main evaluation metrics were:

### Mean Absolute Error (MAE)

MAE measures the average absolute difference between actual and predicted sales.

Lower MAE indicates better forecasting performance.

### Root Mean Squared Error (RMSE)

RMSE gives more weight to larger prediction errors.

Lower RMSE indicates better performance.

---

## Model Comparison

The evaluated models were compared using MAE and RMSE.

Based on the final test-period comparison, **XGBoost achieved the lowest MAE** among the evaluated models.

The overall ranking by MAE was:

1. XGBoost
2. Prophet
3. Baseline
4. ARIMA

Therefore, XGBoost was selected as the final model for the 16-day forecasting task.

---

## Final Forecast

The selected XGBoost model was used to produce the final 16-day sales forecast.

The forecast can support inventory planning by providing an estimate of expected demand over the upcoming period.

---

## Visualizations

The notebook includes visualizations for:

- Overall daily sales
- Rolling statistics
- Time series decomposition
- ARIMA forecast
- Prophet forecast
- Model comparison
- Final XGBoost forecast

---

## Project Structure

```text
Task_13_Time_Series_Forecasting/
│
├── Task_13_Time_Series_Forecasting.ipynb
├── README.md
├── REPORT.md
├── requirements.txt
├── .gitignore
│
├── src/
│   └── time_series_utils.py
│
├── configs/
│   └── config.yaml
│
└── figures/
    ├── overall_sales.png
    ├── rolling_statistics.png
    ├── decomposition.png
    ├── arima_forecast.png
    ├── prophet_forecast.png
    ├── model_comparison_mae.png
    └── final_xgboost_forecast.png