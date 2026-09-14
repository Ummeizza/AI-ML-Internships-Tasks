# Task 12 — Model Interpretation with SHAP and LIME

## Overview

This task focuses on interpreting machine learning predictions using SHAP and LIME in a credit-risk classification scenario. The German Credit dataset was used to understand why a model predicts a customer as Good Credit or Bad Credit.

The workflow covers data preprocessing, baseline modeling, global and local interpretability, SHAP explainers, LIME explanations, and a fairness-audit scaffold.

## Dataset

**Dataset:** German Credit Dataset
**Records:** 1,000
**Input Features:** 20
**Target:** `credit_risk`

The original target contains two classes:

* `1` — Good Credit
* `2` — Bad Credit

For binary classification, the target was converted to:

* `0` — Good Credit
* `1` — Bad Credit

The dataset was loaded in the notebook as `GermanData_Credit.csv`.

## Workflow

The task covered the following stages:

1. Loaded and inspected the German Credit dataset.
2. Assigned feature names and checked data quality.
3. Analyzed the target distribution: 70% Good Credit and 30% Bad Credit.
4. Performed a stratified 80/20 train-test split.
5. Built a leakage-safe preprocessing pipeline using scaling and one-hot encoding.
6. Trained Logistic Regression as the baseline model.
7. Evaluated the model using accuracy, precision, recall, F1-score, and confusion matrix.
8. Applied SHAP LinearExplainer for global and local interpretation.
9. Generated SHAP summary, dependence, waterfall, and force plots.
10. Demonstrated model-agnostic SHAP KernelExplainer.
11. Applied LIME Tabular Explainer for local interpretation.
12. Compared SHAP and LIME explanations.
13. Performed a fairness-audit scaffold using the `housing` attribute.
14. Trained Random Forest and applied SHAP TreeExplainer.
15. Compared feature importance with feature-effect direction.
16. Reviewed reproducibility and interpretation best practices.

## Model Results

### Logistic Regression

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 78.00% |
| Precision | 66.67% |
| Recall    | 53.33% |
| F1-Score  | 59.26% |

Logistic Regression was retained as the primary baseline because it achieved better recall and F1-score than Random Forest.

### Random Forest

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 76.00% |
| Precision | 67.65% |
| Recall    | 38.33% |
| F1-Score  | 48.94% |

Random Forest was included to demonstrate tree-based SHAP interpretation using TreeExplainer.

## SHAP Interpretation

Three SHAP approaches were demonstrated:

* **LinearExplainer** for the Logistic Regression model.
* **KernelExplainer** as a model-agnostic explanation method.
* **TreeExplainer** for the Random Forest model.

The global Logistic Regression SHAP analysis identified `checking_status_A14` as the most influential processed feature, followed by `installment_rate`, `credit_history_A34`, `savings_status_A61`, and `checking_status_A11`.

Local SHAP analysis showed that the most influential features for an individual customer can differ from the globally important features.

## LIME Interpretation

LIME Tabular Explainer was used to provide a local explanation for an individual customer. SHAP and LIME identified some common influential features while producing different rankings because they use different explanation approaches.

## Fairness Audit

A fairness-audit scaffold was implemented using the `housing` attribute.

The largest observed disparities were:

* Recall: 0.2449
* Positive Prediction Rate: 0.2537
* F1-Score: 0.1662

These values indicate differences in model behavior across groups, but they should not be treated as a definitive fairness or legal conclusion because the dataset is relatively small and group sizes are unequal.

## Key Learning Outcomes

* Understanding global and local model interpretability.
* Applying SHAP LinearExplainer, KernelExplainer, and TreeExplainer.
* Generating SHAP summary, dependence, waterfall, and force plots.
* Using LIME for local tabular explanations.
* Distinguishing feature importance from feature-effect direction.
* Performing a basic fairness audit.
* Building reproducible and leakage-safe interpretation workflows.
* Understanding the limitations of post-hoc model explanations.

## Repository Structure

```text
data/        Dataset directory
notebook/    Complete Task 12 notebook
src/         Reusable interpretation helper functions
figures/     Visualization directory
README.md    Task overview and results
REPORT.md    Detailed task report
requirements.txt
.gitignore
```

## Conclusion

The task demonstrated how SHAP and LIME can improve the transparency of machine learning predictions in a credit-risk setting. Global explanations, local explanations, model comparison, and fairness auditing together provided a broader understanding of model behavior and its limitations.