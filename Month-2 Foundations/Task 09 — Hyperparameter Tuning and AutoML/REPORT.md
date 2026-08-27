# Task 09 — Hyperparameter Tuning and AutoML

## 1. Overview

This task focused on developing a systematic hyperparameter tuning and AutoML workflow for Wine Quality classification. The main objective was to reduce manual model tuning and evaluate different automated optimization techniques to improve model performance.

The approaches evaluated in this task were GridSearchCV, RandomizedSearchCV, Optuna, TPOT AutoML, and an additional SMOTE-based class-balancing experiment.

---

## 2. Business Objective

The business scenario involved an ML team spending significant time manually tuning models. The existing target was to improve model performance toward an accuracy of 85% or higher.

The task therefore focused on systematic and automated hyperparameter optimization while maintaining a reproducible and leakage-free workflow.

---

## 3. Dataset

**Dataset:** Wine Quality (UCI/Kaggle)

The dataset contains physicochemical measurements of wine samples.

### Input Features

- Fixed acidity
- Volatile acidity
- Citric acid
- Residual sugar
- Chlorides
- Free sulfur dioxide
- Total sulfur dioxide
- Density
- pH
- Sulphates
- Alcohol

### Target Variable

The target variable is `quality`, representing the quality score of each wine sample.

---

## 4. Data Exploration and Cleaning

The dataset was inspected for structure, data types, missing values, duplicate records, and target-class distribution.

A total of **240 duplicate rows**, representing approximately **15.01%** of the dataset, were identified.

Instead of automatically removing duplicates, their distribution was analyzed because removing them could change the original data distribution and affect model behavior.

The target distribution was also examined. Quality scores **5 and 6** represented the majority of observations, while classes such as 3, 4, and 8 contained substantially fewer samples.

---

## 5. Data Preprocessing

The target variable was separated from the input features.

The dataset was divided into training and testing sets using stratified splitting.

### Dataset Split

- Training set: **1,279 samples**
- Testing set: **320 samples**
- Number of input features: **11**

Feature scaling was then applied to the training and testing data.

The test set was kept separate and was not used during hyperparameter optimization.

---

## 6. Baseline Model

A Random Forest classifier was used as the baseline model to establish a reference performance before tuning.

### Baseline Result

| Metric | Score |
|---|---:|
| Accuracy | **68.00%** |

This baseline was used to compare the effectiveness of the subsequent optimization methods.

---

## 7. GridSearchCV

GridSearchCV was used for exhaustive hyperparameter search.

A total of **48 parameter combinations** were evaluated using **5-fold cross-validation**, resulting in 240 model fits.

### Best Parameters

```text
max_depth = None
max_features = sqrt
min_samples_leaf = 2
min_samples_split = 2
n_estimators = 200