# Task 06 Report — Classification Algorithms Comparison

## 1. Executive Summary

This task focused on developing a classification solution for a bank marketing campaign. The objective was to identify customers who were more likely to subscribe to a term deposit while considering the unequal business costs of incorrect predictions.

The Bank Marketing dataset contains a significant class imbalance, with subscribers representing only 11.27% of the observations. Because of this imbalance, the majority-class baseline achieved high accuracy while failing completely to identify subscribers.

Five classification algorithms were evaluated: Logistic Regression, Decision Tree, Random Forest, Support Vector Machine (SVM), and K-Nearest Neighbors (KNN). Class weighting and SMOTE were then investigated as approaches for handling the minority class.

Finally, threshold optimization was performed using the business costs specified in the task. A threshold of 0.25 produced the lowest estimated business cost among the tested thresholds.

---

## 2. Business Context

The bank conducts marketing calls to potential customers.

The business scenario defines:

- Cost of a false positive call: **$5**
- Estimated value lost from a missed subscriber: **$500**
- Approximate current conversion rate: **11%**

This creates an asymmetric cost problem.

A false positive results in a relatively small cost because the bank makes an unnecessary call. A false negative is considerably more expensive because a potential subscriber is missed.

Therefore, the classification system should prioritize identifying the positive class rather than optimizing accuracy alone.

---

## 3. Dataset

The Bank Marketing dataset was used for this analysis.

The dataset contains customer demographic attributes, financial information, previous campaign information, contact details, and economic indicators.

The target variable is:

- `0` — Customer did not subscribe
- `1` — Customer subscribed

After cleaning duplicate observations, the dataset contained approximately **41,176 observations**.

### Target Distribution

| Class | Count | Percentage |
|---|---:|---:|
| Non-subscriber | 36,537 | 88.73% |
| Subscriber | 4,639 | 11.27% |

The target distribution demonstrates substantial class imbalance.

---

## 4. Data Processing

The following preprocessing steps were performed:

1. Loaded the dataset using the semicolon delimiter.
2. Checked dataset dimensions and column types.
3. Identified duplicate observations.
4. Removed duplicate rows.
5. Investigated unknown values in categorical features.
6. Converted the target variable from `yes/no` to binary `1/0`.
7. Separated features from the target variable.
8. Created a stratified 80/20 train-test split.
9. Applied appropriate preprocessing to numerical and categorical features.
10. Used pipelines to ensure consistent preprocessing between training and testing data.

The stratified split preserved the original class distribution in both training and testing sets.

### Dataset Split

| Set | Observations | Features |
|---|---:|---:|
| Training | 32,940 | 20 |
| Testing | 8,236 | 20 |

---

## 5. Baseline Model

A majority-class baseline was established before training the classification models.

### Baseline Performance

| Metric | Score |
|---|---:|
| Accuracy | 0.8873 |
| Precision | 0.0000 |
| Recall | 0.0000 |
| F1 Score | 0.0000 |
| ROC-AUC | 0.5000 |
| PR-AUC | 0.1127 |

Although the baseline achieved **88.73% accuracy**, it failed to identify any subscribers.

This demonstrates why accuracy is misleading for this dataset. A model can obtain high accuracy simply by predicting the majority class while providing no useful information about the minority class.

---

## 6. Classification Models

The following models were evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine
- K-Nearest Neighbors

### Standard Model Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC | PR-AUC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.9095 | 0.6522 | 0.4224 | 0.5128 | 0.9390 | 0.6014 |
| Decision Tree | 0.9143 | 0.6500 | 0.5183 | 0.5767 | 0.9320 | 0.6094 |
| Random Forest | 0.9095 | 0.7427 | 0.3017 | 0.4291 | 0.9422 | 0.6527 |
| SVM | 0.9119 | 0.6683 | 0.4321 | 0.5249 | 0.9163 | 0.6292 |
| KNN | 0.9014 | 0.5858 | 0.4267 | 0.4938 | 0.8741 | 0.4920 |

The standard Random Forest achieved the highest ROC-AUC and PR-AUC among the standard models, although its recall was relatively low.

The Decision Tree achieved the highest accuracy and F1 score among the standard models.

---

## 7. Class Weighting

Class weighting was used to increase the importance of minority-class observations during model training.

### Balanced Model Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC | PR-AUC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.8643 | 0.4494 | 0.9084 | 0.6013 | 0.9403 | 0.5921 |
| Decision Tree | 0.8384 | 0.4062 | 0.9407 | 0.5674 | 0.9355 | 0.6208 |
| Random Forest | 0.8627 | 0.4473 | 0.9278 | 0.6036 | 0.9444 | 0.6399 |

Class weighting substantially increased recall for all evaluated models.

For example, Random Forest recall increased from **30.17% to 92.78%**.

This improvement comes with a reduction in precision and accuracy because the models become more willing to classify customers as potential subscribers.

---

## 8. SMOTE

SMOTE was evaluated as an alternative method for handling class imbalance.

SMOTE was applied only to the training data. The test set was kept unchanged to prevent data leakage.

### SMOTE Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC | PR-AUC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 0.8679 | 0.4565 | 0.9041 | 0.6067 | 0.9396 | 0.5893 |
| Random Forest | 0.8806 | 0.4832 | 0.8513 | 0.6165 | 0.9408 | 0.6236 |

SMOTE improved the Random Forest F1 score compared with its class-weighted version, increasing it from approximately **0.6036 to 0.6165**.

However, its recall decreased from **92.78% to 85.13%**.

This highlights the trade-off between precision and recall when different imbalance-handling strategies are applied.

---

## 9. Threshold Optimization

The default classification threshold of 0.50 was not assumed to be optimal because the business costs of false positives and false negatives are very different.

The following cost function was used:

```text
Business Cost =
(False Positives × $5) +
(False Negatives × $500)