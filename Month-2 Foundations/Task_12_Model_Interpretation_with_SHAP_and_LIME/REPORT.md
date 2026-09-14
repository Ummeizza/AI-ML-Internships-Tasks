# Task 12 — Model Interpretation with SHAP and LIME

## 1. Objective

The objective of this task was to interpret machine learning predictions in a credit-risk classification scenario using SHAP and LIME. The German Credit dataset was used to understand global and local model behavior, feature contributions, and fairness considerations.

## 2. Dataset and Preprocessing

The German Credit dataset contained 1,000 records and 20 input features. The target variable `credit_risk` contained two original classes: 1 for Good Credit and 2 for Bad Credit.

The target was converted into binary labels, where 0 represented Good Credit and 1 represented Bad Credit. The dataset contained 700 Good Credit records and 300 Bad Credit records.

No missing values or duplicate records were found. The data was divided into 80% training and 20% testing sets using stratified sampling.

The seven numerical features were standardized using `StandardScaler`, while the 13 categorical features were transformed using one-hot encoding. The preprocessing was implemented through a `ColumnTransformer` and Pipeline to maintain a consistent and leakage-safe workflow.

## 3. Baseline Model

Logistic Regression was selected as the baseline classification model.

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 78.00% |
| Precision | 66.67% |
| Recall    | 53.33% |
| F1-Score  | 59.26% |

The confusion matrix showed that 32 out of 60 Bad Credit cases were correctly identified, while 28 were incorrectly classified as Good Credit.

## 4. SHAP Interpretation

SHAP was used to provide both global and local model explanations.

### LinearExplainer

Since Logistic Regression is a linear model, SHAP `LinearExplainer` was used. After preprocessing, the original 20 features became 61 processed numerical features.

The top globally influential processed features were:

1. `checking_status_A14` — 0.427943
2. `installment_rate` — 0.328632
3. `credit_history_A34` — 0.313747
4. `savings_status_A61` — 0.302180
5. `checking_status_A11` — 0.281553

The SHAP summary and dependence plots provided global information about feature influence and effects.

### Local SHAP Explanation

For the selected customer, the actual class was Good Credit and Logistic Regression also predicted Good Credit with a Bad Credit probability of 22.68%.

The strongest local SHAP contributions included `savings_status_A64`, `savings_status_A61`, `checking_status_A14`, and the `other_installment_plans` features.

Positive SHAP contributions moved the model output toward Bad Credit, while negative contributions moved it toward Good Credit.

### KernelExplainer

KernelExplainer was demonstrated as a model-agnostic SHAP method using a limited background sample and 10 test observations to reduce computational cost.

The most influential Kernel SHAP feature was `credit_history_A34`, followed by `savings_status_A61`, `employment_A74`, `installment_rate`, and `purpose_A40`.

Seven features appeared in the Top 10 rankings of both Linear SHAP and Kernel SHAP, showing useful agreement between the two approaches.

## 5. LIME Interpretation

LIME Tabular Explainer was applied to the selected customer to generate a local explanation.

Important LIME features included `purpose_A46`, `checking_status_A14`, `checking_status_A11`, `credit_history_A34`, and `property_A124`.

Three features appeared in both the Top 10 SHAP and Top 10 LIME local explanations:

* `savings_status_A61`
* `checking_status_A11`
* `checking_status_A14`

The difference between SHAP and LIME rankings is expected because the methods use different explanation approaches and their contribution values are not directly comparable.

## 6. Random Forest and Tree SHAP

A Random Forest classifier was trained on the same preprocessed features to demonstrate SHAP TreeExplainer.

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 76.00% |
| Precision | 67.65% |
| Recall    | 38.33% |
| F1-Score  | 48.94% |

Random Forest showed lower recall and F1-score than Logistic Regression and was therefore not selected as the primary model.

TreeExplainer generated SHAP values for 200 test observations, 61 processed features, and both credit-risk classes.

The most influential Tree SHAP feature was `checking_status_A14`, followed by `duration`, `checking_status_A11`, `credit_amount`, and `credit_history_A34`.

For the selected customer, Random Forest predicted Good Credit with a Bad Credit probability of 33.00%.

## 7. Global vs Local Interpretability

Global SHAP analysis identified features that were generally influential across the test dataset, while local SHAP analysis identified the features that had the strongest influence on a particular customer's prediction.

The two perspectives produced different feature rankings, demonstrating that a feature can be globally important without being the strongest contributor to every individual decision.

## 8. Feature Importance vs Feature Effects

Mean absolute SHAP values were used to measure overall feature importance, while the sign of SHAP values was used to understand effect direction.

For example, `checking_status_A14` had the highest global importance with a mean absolute SHAP value of 0.4279 and a positive average SHAP effect of 0.0266, indicating an overall tendency toward Bad Credit.

In contrast, `checking_status_A11` had high importance of 0.2816 but a negative average SHAP effect of -0.0428, indicating an overall tendency toward Good Credit.

This demonstrates why feature importance and feature direction should be interpreted separately.

## 9. Fairness Audit

A group-level fairness-audit scaffold was implemented using the `housing` attribute.

The observed maximum differences between groups were:

| Metric                   | Max-Min Difference |
| ------------------------ | -----------------: |
| Accuracy                 |             0.0829 |
| Precision                |             0.1500 |
| Recall                   |             0.2449 |
| F1-Score                 |             0.1662 |
| Positive Prediction Rate |             0.2537 |

The results indicate differences in prediction behavior and performance across groups. However, these are descriptive audit indicators only. The dataset is relatively small and the group sizes are unequal, so further statistical and domain-specific analysis would be required before making a definitive fairness conclusion.

## 10. Reproducibility and Best Practices

The workflow used fixed random states for reproducibility and separated training and testing data before model fitting.

Preprocessing was performed through a structured pipeline to reduce leakage risk. Appropriate SHAP explainers were selected according to model type:

* LinearExplainer for Logistic Regression
* KernelExplainer for model-agnostic interpretation
* TreeExplainer for Random Forest

Kernel SHAP was restricted to a smaller sample because of computational cost. SHAP and LIME explanations were treated as explanations of model behavior rather than causal relationships.

## 11. Limitations

The main limitations were:

* The dataset contains only 1,000 records.
* Some fairness groups have relatively small sample sizes.
* Kernel SHAP can become computationally expensive.
* One-hot encoding produces multiple processed features for categorical variables.
* SHAP and LIME do not establish causal relationships.
* The fairness analysis is an audit scaffold rather than a definitive fairness assessment.

## 12. Final Conclusion

This task successfully demonstrated how SHAP and LIME can be used to improve the interpretability of credit-risk machine learning predictions.

The workflow covered data preprocessing, leakage-safe modeling, baseline evaluation, global and local SHAP interpretation, Kernel SHAP, Tree SHAP, LIME, feature-effect analysis, fairness auditing, and reproducibility practices.

Logistic Regression was retained as the primary model because it achieved better recall and F1-score than Random Forest on the test dataset. Random Forest was included to demonstrate the use of SHAP TreeExplainer for tree-based models.

Overall, the task showed how model interpretation can provide greater transparency around credit-risk predictions while also highlighting the importance of fairness, reproducibility, and careful interpretation of explanation methods.