# Task 06 — Classification Algorithms Comparison

## Overview

This project focuses on building and comparing multiple classification models for a bank marketing campaign.

The objective is to identify customers who are most likely to subscribe to a term deposit while considering the different business costs of incorrect predictions.

The Bank Marketing dataset contains a highly imbalanced target variable, making accuracy alone an unreliable measure of model performance. Therefore, the project evaluates multiple classification algorithms, applies class-imbalance techniques, and performs business-oriented threshold optimization.

---

## Business Problem

The bank currently contacts customers using a largely random strategy.

- Cost of an unnecessary call: **$5**
- Estimated value of a missed subscriber: **$500**
- Current conversion rate: approximately **11%**

Because missing a potential subscriber is significantly more expensive than making an unnecessary call, the model should prioritize identifying the positive class while maintaining a reasonable number of false-positive calls.

---

## Dataset

**Dataset:** Bank Marketing Dataset  
**Source:** UCI / Kaggle

The dataset contains customer demographic information, contact details, previous campaign information, and economic indicators.

### Target Variable

`y`

- `0` — Customer did not subscribe
- `1` — Customer subscribed

After cleaning:

- Total observations: **41,176**
- Non-subscribers: **36,537**
- Subscribers: **4,639**
- Positive-class proportion: **11.27%**

The dataset therefore contains a substantial class imbalance.

---

## Project Objectives

The project aims to:

1. Clean and preprocess the Bank Marketing dataset.
2. Analyze the target-class imbalance.
3. Establish a simple baseline classifier.
4. Compare multiple classification algorithms.
5. Evaluate models using appropriate classification metrics.
6. Handle class imbalance using class weights and SMOTE.
7. Optimize the classification threshold according to business costs.
8. Analyze ROC and Precision-Recall curves.
9. Select a final model based on both statistical performance and business impact.

---

## Models Evaluated

The following classification algorithms were implemented:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)

A baseline model predicting the majority class was also established for comparison.

---

## Class Imbalance Handling

Two approaches were investigated:

### 1. Class Weighting

The `balanced` class-weight option was applied to supported classifiers. This increases the importance of minority-class observations during training without generating additional data.

### 2. SMOTE

SMOTE (Synthetic Minority Over-sampling Technique) was applied to the training data to generate synthetic minority-class observations.

The test set was kept unchanged to avoid data leakage and preserve a realistic evaluation distribution.

---

## Evaluation Metrics

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- PR-AUC

Because the dataset is highly imbalanced, particular attention was given to **Recall, F1 Score, PR-AUC, and ROC-AUC** rather than relying on accuracy alone.

---

## Key Results

The baseline classifier achieved approximately **88.73% accuracy**, but its recall and F1 score were both zero because it failed to identify any subscribers.

The standard classifiers performed substantially better.

The balanced Random Forest achieved:

- Accuracy: **86.27%**
- Precision: **44.73%**
- Recall: **92.78%**
- F1 Score: **60.36%**
- ROC-AUC: **0.9444**
- PR-AUC: **0.6399**

The SMOTE-based Random Forest achieved an F1 score of approximately **61.65%**, showing that synthetic oversampling can improve the balance between precision and recall.

---

## Business-Aware Threshold Optimization

Using the default probability threshold of 0.50 resulted in a higher estimated business cost.

The threshold was therefore optimized using:

**Business Cost = (False Positives × $5) + (False Negatives × $500)**

Among the tested thresholds, **0.25** produced the lowest estimated business cost.

At this threshold, the balanced Random Forest produced:

| Metric | Result |
|---|---:|
| Threshold | 0.25 |
| True Negatives | 5,375 |
| False Positives | 1,933 |
| False Negatives | 9 |
| True Positives | 919 |
| Recall | 99.03% |
| F1 Score | 48.62% |
| Estimated Business Cost | **$14,165** |

The optimized threshold prioritizes identifying potential subscribers because a missed subscriber has a substantially higher estimated cost than an unnecessary call.

---

## Visualizations

The project includes visualizations for:

- Model performance comparison
- ROC curve
- Precision-Recall curve
- Confusion matrix
- Classification performance analysis

These figures are stored in the `figures/` directory.

---

