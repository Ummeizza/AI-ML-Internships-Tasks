# Task 10 — Pipeline Engineering with Scikit-Learn

## 1. Overview

This task focused on building a reproducible machine learning pipeline for Titanic survival prediction using Scikit-Learn.

The main objective was to combine feature engineering, data preprocessing, model training, evaluation, and model serialization into a single workflow. This approach helps prevent inconsistencies between training and inference preprocessing.

---

## 2. Business Problem

The data science team had multiple notebooks with inconsistent preprocessing workflows. Such inconsistencies can cause models to behave differently during production inference.

The goal was therefore to create one reusable pipeline that handles the complete workflow from feature engineering and preprocessing to prediction.

---

## 3. Dataset

**Dataset:** Titanic Dataset

The Titanic dataset contains passenger information and survival outcomes.

The target variable is:

- `Survived`

where:

- `0` = Did Not Survive
- `1` = Survived

Selected input features included passenger class, age, sex, number of siblings/spouses, number of parents/children, fare, and embarkation port.

---

## 4. Data Preprocessing

The following preprocessing steps were implemented:

- Selected relevant numerical and categorical features.
- Handled missing numerical values using median imputation.
- Handled missing categorical values using the most frequent value.
- Standardized numerical features using `StandardScaler`.
- Converted categorical variables using `OneHotEncoder`.
- Used `handle_unknown="ignore"` for safer inference on unseen categories.

All preprocessing steps were integrated into the Scikit-Learn pipeline.

---

## 5. Custom Feature Engineering

A custom `FamilySizeTransformer` was created using Scikit-Learn's `BaseEstimator` and `TransformerMixin`.

The `FamilySize` feature was derived as:

`FamilySize = SibSp + Parch + 1`

The custom transformer increased the feature representation from 7 original selected features to 8 features after feature engineering.

This transformation was integrated into the pipeline so that the same feature engineering operation is automatically applied during training and prediction.

---

## 6. ColumnTransformer

A `ColumnTransformer` was used to apply different preprocessing strategies to numerical and categorical features.

### Numerical features

- Median imputation
- Standard scaling

### Categorical features

- Most-frequent imputation
- One-hot encoding

This allowed different feature types to be processed correctly within the same workflow.

---

## 7. Machine Learning Model

A Random Forest Classifier was used as the main model.

The model configuration included:

- `n_estimators = 200`
- `class_weight = "balanced"`
- `random_state = 42`

The model was integrated directly into the complete Scikit-Learn pipeline.

---

## 8. Integrated Pipeline Results

The final integrated pipeline achieved the following test results:

| Metric | Score |
|---|---:|
| Accuracy | 0.8045 |
| Precision | 0.7742 |
| Recall | 0.6957 |
| F1 Score | 0.7328 |

The pipeline achieved **80.45% test accuracy**.

---

## 9. Classification Results

The classification report showed:

| Class | Precision | Recall | F1 Score |
|---|---:|---:|---:|
| Did Not Survive | 0.82 | 0.87 | 0.85 |
| Survived | 0.77 | 0.70 | 0.73 |

The model performed better on the `Did Not Survive` class than on the `Survived` class.

---

## 10. Baseline Comparison

Logistic Regression was used as a simple baseline.

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression Baseline | 0.8045 | 0.7931 | 0.6667 | 0.7244 |
| Random Forest Pipeline | 0.8045 | 0.7742 | 0.6957 | 0.7328 |

Both models achieved the same accuracy of 80.45%.

However, the Random Forest pipeline achieved slightly higher recall and F1 score, while the Logistic Regression baseline achieved slightly higher precision.

Therefore, the more complex model did not improve overall accuracy, but it provided a small improvement in recall and F1 score.

---

## 11. Pipeline Serialization

The complete trained pipeline was serialized using Joblib.

The saved pipeline included:

- Custom feature engineering
- Data preprocessing
- Feature encoding
- Random Forest model

After loading the saved pipeline, predictions were generated again on the test data.

### Verification Result

- Loaded Pipeline Accuracy: **0.8045**
- Predictions Identical: **True**

This confirmed that the serialized pipeline could be successfully restored and used for inference.

---

## 12. Important Findings

The main findings were:

1. The integrated pipeline achieved 80.45% test accuracy.
2. The baseline Logistic Regression model also achieved 80.45% accuracy.
3. Random Forest achieved slightly better recall and F1 score.
4. Custom feature engineering was successfully integrated into the pipeline.
5. ColumnTransformer successfully handled numerical and categorical preprocessing.
6. The saved and reloaded pipeline produced identical predictions.
7. Pipeline engineering improves reproducibility even when it does not directly increase model accuracy.

---

## 13. Business Insights

The primary business value of this solution is consistency and maintainability.

A single pipeline reduces the risk of training and inference preprocessing differences. This makes the machine learning workflow easier to reproduce and maintain.

The serialized pipeline can also be reused for future predictions without manually repeating the feature engineering and preprocessing steps.

---

## 14. Limitations

- The Titanic dataset is relatively small and historical.
- Only selected passenger features were used.
- The integrated pipeline did not improve accuracy over the baseline.
- Model performance may vary with different train-test splits.
- Additional feature engineering and alternative models could potentially improve performance.

---

## 15. Conclusion

This task successfully implemented a reproducible Scikit-Learn pipeline for Titanic survival prediction.

The final workflow combined custom feature engineering, ColumnTransformer-based preprocessing, Random Forest classification, evaluation, and Joblib serialization into one reusable pipeline.

The pipeline achieved 80.45% test accuracy, and the saved pipeline produced identical predictions after being reloaded.

Although the pipeline did not improve accuracy compared with the Logistic Regression baseline, it successfully addressed the main engineering problem of creating a consistent, reusable, and maintainable machine learning workflow.

---

## 16. Learning Outcomes

Through this task, I learned how to:

- Build Scikit-Learn Pipelines.
- Use ColumnTransformer for mixed data types.
- Create custom Scikit-Learn transformers.
- Integrate feature engineering with preprocessing.
- Reduce preprocessing inconsistencies.
- Evaluate a pipeline against a baseline.
- Serialize and reload models using Joblib.
- Build reproducible and modular machine learning workflows.