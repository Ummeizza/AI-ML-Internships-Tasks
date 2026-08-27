# Task 09 — Hyperparameter Tuning and AutoML

## Project Objective

The objective of this task is to build a systematic machine learning model tuning and evaluation workflow for Wine Quality classification.

The task focuses on reducing manual hyperparameter tuning by applying GridSearchCV, RandomizedSearchCV, Optuna, and TPOT AutoML. Different approaches are compared using consistent evaluation metrics, with the target of achieving 85%+ classification accuracy.

---

## Business Problem

The ML team at a SaaS company currently spends significant time manually tuning machine learning models. The existing model achieves approximately 78% accuracy, while the desired target is 85%+.

This project investigates automated and systematic hyperparameter optimization techniques to identify a better-performing model while maintaining a reproducible and leakage-free workflow.

---

## Dataset

**Dataset:** Wine Quality (UCI/Kaggle)

The dataset contains physicochemical measurements of wine samples and a quality score.

### Features

- fixed acidity
- volatile acidity
- citric acid
- residual sugar
- chlorides
- free sulfur dioxide
- total sulfur dioxide
- density
- pH
- sulphates
- alcohol

### Target Variable

**Target:** `quality`

The target represents the quality score of the wine.

---

## Data Cleaning

The dataset was inspected for data quality issues before model development.

The following checks were performed:

- Dataset shape and structure inspection
- Missing-value inspection
- Duplicate-row analysis
- Target distribution analysis
- Feature data-type inspection

A total of **240 duplicate rows (15.01%)** were identified.

The duplicate rows were analyzed rather than automatically removed because the task investigation showed that duplicates were concentrated mainly in the common quality classes. Removing them could alter the original data distribution and potentially affect model performance.

---

## Data Preprocessing

The following preprocessing steps were performed:

1. Features and target variable were separated.
2. The dataset was divided into training and testing sets.
3. Feature scaling was applied to the input features.
4. The test set was kept separate for final evaluation.
5. Hyperparameter tuning was performed using cross-validation on the training data.

The training set contained **1,279 observations**, while the testing set contained **320 observations**.

---

## Models and Tuning Methods

The following approaches were evaluated:

### Baseline Random Forest

A Random Forest classifier was used as the baseline model.

**Test Accuracy:** 68.00%

### GridSearchCV

GridSearchCV was used to perform an exhaustive search over a predefined hyperparameter grid.

**Best Cross-Validation Accuracy:** 68.80%

**Test Accuracy:** 66.87%

### RandomizedSearchCV

RandomizedSearchCV was used to explore a randomly selected subset of the hyperparameter search space.

Best parameters:

```text
n_estimators = 413
max_depth = 20
max_features = sqrt
min_samples_leaf = 1
min_samples_split = 5