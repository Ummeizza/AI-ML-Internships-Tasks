# Task 11 — Ensemble Methods: Bagging, Boosting and Stacking

## Objective

This project implements and compares ensemble learning techniques on the Spaceship Titanic dataset.

The main objective is to determine whether combining diverse machine learning models can improve predictive performance over a simple baseline model.

## Dataset

**Dataset:** Spaceship Titanic

**Target Variable:** `Transported`

**Records:** 8,693

## Methods Implemented

### Baseline
- Logistic Regression

### Bagging
- Random Forest
- BaggingClassifier

### Boosting
- XGBoost
- LightGBM
- CatBoost

### Ensemble
- Soft Voting
- Stacking

## Feature Engineering

The following features were created:

- `Deck`
- `CabinNum`
- `Side`
- `TotalSpending`
- `GroupSize`

Identifier fields such as `PassengerId` and `Name` were removed.

## Preprocessing

- Median imputation for numerical features
- Most-frequent imputation for categorical features
- StandardScaler for numerical features
- OneHotEncoder for categorical features
- Scikit-Learn Pipeline and ColumnTransformer

## Results

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 78.72% | 78.30% | 79.91% | 79.10% |
| CatBoost | 80.33% | 79.47% | 82.19% | 80.81% |
| Soft Voting | **81.31%** | **81.70%** | 81.05% | **81.38%** |
| Stacking | 80.56% | 79.63% | **82.53%** | 81.05% |

## Key Findings

Soft Voting achieved the best overall performance with 81.31% accuracy.

Stacking achieved the highest recall at 82.53%, but did not outperform Soft Voting in overall accuracy.

Prediction diversity analysis showed that the base models made different predictions on some test samples, supporting the use of ensemble learning.

## Project Structure

```text
Task_11_Ensemble_Methods_Bagging_Boosting_Stacking/
│
├── data/
├── figures/
├── src/
├── Task_11.ipynb
├── REPORT.md
├── README.md
├── requirements.txt
└── Dockerfile