# Task 05 — Regression Modeling From Scratch to Production

## Overview

In this task, I worked on a house price prediction problem using the *California Housing dataset* from Scikit-learn. The main focus was to understand how different regression models perform and how model results can be evaluated from both a machine learning and business perspective.

## What I Worked On

* Loaded and explored the California Housing dataset.
* Checked the dataset for missing values and duplicates.
* Split the data into training and testing sets.
* Applied feature scaling where required.
* Created a baseline for comparison.
* Trained and compared:

  * Linear Regression
  * Ridge Regression
  * Tuned Ridge Regression
  * Polynomial Regression
* Evaluated models using *MAE, RMSE, and R²*.
* Generated predictions on unseen test data.
* Checked predictions against the defined business error threshold.
* Compared the overall performance of the models.

## Results

Polynomial Regression gave the best results among the tested models:

| Metric |   Result |
| ------ | -------: |
| MAE    | 0.467001 |
| RMSE   | 0.681397 |
| R²     | 0.645682 |

Compared with the baseline, the final modeling process improved MAE by *48.46%* and RMSE by *40.48%*.

For the business threshold analysis, *1,849 out of 4,128 predictions (44.79%)* were within the acceptable error range.

## What I Learned

This task helped me understand the complete regression workflow, including baseline comparison, regularization with Ridge, hyperparameter tuning, polynomial features, model evaluation, and interpreting results according to a real business requirement.

## Tools Used

Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Google Colab, and GitHub.
## Business Scenario
A PropTech app serves ~10,000 price predictions/day. Predictions within **±$30,000** of the actual value are considered acceptable.

## Project Structure
Task_05_Regression_Modeling_From_Scratch_to_Production/
├── notebooks/
│ └── Task_05_Regression_Modeling.ipynb # full analysis notebook
├── src/ # modular, reusable pipeline code
│ ├── init.py
│ ├── preprocessing.py # train/test split, missing-value checks
│ ├── model_utils.py # model/pipeline factory functions
│ ├── train_models.py # training functions per model type
│ ├── predict.py # prediction + error calculation
│ ├── evaluate.py # MAE/RMSE/R² evaluation, residuals
│ └── regression_helpers.py # shared metrics + prediction intervals
├── requirements.txt
├── REPORT.md
├── README.md
└── .gitignore