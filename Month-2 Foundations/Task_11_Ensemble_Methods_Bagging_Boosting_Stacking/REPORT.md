# Task 11 — Ensemble Methods

## 1. Objective

The objective of this task was to understand and implement ensemble learning methods including Bagging, Boosting, Voting, and Stacking.

## 2. Business Problem

Single machine learning models may reach a performance plateau. The goal was to combine diverse models and evaluate whether ensemble methods could improve prediction performance for the Spaceship Titanic dataset.

## 3. Dataset

The Spaceship Titanic dataset from Kaggle was used.

- Dataset: Spaceship Titanic
- Target: Transported
- Records: 8,693
- Features: 13 input features before feature engineering

## 4. Data Preprocessing

The following preprocessing steps were applied:

- Missing numerical values were handled using median imputation.
- Missing categorical values were handled using most-frequent imputation.
- Numerical features were standardized using StandardScaler.
- Categorical features were encoded using OneHotEncoder.
- `Cabin` was split into Deck, Cabin Number, and Side.
- TotalSpending was created from passenger spending columns.
- GroupSize was extracted from PassengerId.
- PassengerId and Name were removed as identifier fields.

All preprocessing was implemented through Scikit-Learn pipelines to reduce the risk of data leakage.

## 5. Models Implemented

### Baseline
- Logistic Regression

### Bagging
- Random Forest
- BaggingClassifier

### Boosting
- XGBoost
- LightGBM
- CatBoost

### Ensemble Methods
- Soft Voting
- Stacking

## 6. Results

The Logistic Regression baseline achieved:

- Accuracy: 78.72%
- Precision: 78.30%
- Recall: 79.91%
- F1 Score: 79.10%

The Soft Voting ensemble achieved the strongest overall performance:

- Accuracy: 81.31%
- Precision: 81.70%
- Recall: 81.05%
- F1 Score: 81.38%

The Stacking ensemble achieved:

- Accuracy: 80.56%
- Precision: 79.63%
- Recall: 82.53%
- F1 Score: 81.05%

## 7. Diversity Analysis

Prediction disagreement was analyzed between Random Forest, XGBoost, LightGBM, and CatBoost.

The highest disagreement was observed between Random Forest and CatBoost at approximately 9.8%, while XGBoost and LightGBM showed lower disagreement of approximately 3.2%.

This indicates that the base models have different prediction behaviors, although some boosting models produce relatively similar predictions.

## 8. Key Findings

- Soft Voting achieved the highest overall accuracy and F1-score.
- Soft Voting improved accuracy over the Logistic Regression baseline by 2.59 percentage points.
- Stacking achieved the highest recall at 82.53%.
- Stacking did not outperform Soft Voting in overall accuracy.
- Ensemble performance depends on model diversity and complementary prediction behavior.

## 9. Business Impact

The ensemble approach provides a more robust prediction strategy than relying only on a single baseline model. Combining different learning algorithms can improve predictive performance and provide alternative trade-offs between precision, recall, and F1-score.

## 10. Limitations

- Performance depends on feature engineering and model configuration.
- Some models showed relatively similar predictions.
- Evaluation was performed using a single held-out test set.
- Further hyperparameter tuning could potentially improve performance.
- Stacking was not the best overall model in this experiment.

## 11. Conclusion

This task demonstrated the practical application of Bagging, Boosting, Voting, and Stacking ensemble methods.

The Soft Voting ensemble achieved the best overall performance with 81.31% accuracy and 81.38% F1-score. Stacking achieved the highest recall of 82.53%, but did not achieve the highest overall accuracy.

The results demonstrate that ensemble methods can improve model performance when diverse models provide complementary predictions.