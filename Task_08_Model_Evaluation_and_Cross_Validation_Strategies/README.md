# Task 08 Report — Model Evaluation and Cross Validation Strategies

## 1. Introduction

This task evaluates machine learning models for a heart disease prediction problem using robust model evaluation and cross-validation strategies.

The main objective was to determine whether a model's performance remains reliable across different validation strategies rather than relying only on a single train-test accuracy score.

## 2. Data Processing

The Heart Disease dataset was loaded and inspected for data types, missing values and target distribution.

The data was divided into training and testing sets. Preprocessing was implemented using a pipeline to reduce the risk of data leakage during cross-validation.

## 3. Models

Two classification models were evaluated:

- Logistic Regression as the baseline model
- Random Forest as a stronger nonlinear model

## 4. Cross Validation Strategies

The following evaluation strategies were implemented:

### K-Fold Cross Validation

K-Fold validation divided the training data into multiple folds and evaluated the model across different train-validation splits.

### Stratified K-Fold

Stratified K-Fold preserved the class distribution across folds and was particularly appropriate for the binary classification problem.

### Leave-One-Out Cross Validation

LOOCV was demonstrated on a smaller representative subset because applying LOOCV to the complete dataset would require a model to be trained once for every observation.

The demonstration produced a mean accuracy of approximately 0.53.

### Nested Cross Validation

Nested Cross Validation separated model selection from model evaluation.

The mean outer ROC-AUC was:

**0.5140**

with a standard deviation of:

**0.0097**

## 5. Model Evaluation

The baseline models achieved approximately 80% test accuracy.

However, both models produced:

- Precision: 0.00
- Recall: 0.00
- F1 Score: 0.00

for the positive heart disease class.

The ROC-AUC values were close to 0.50, indicating weak discrimination.

## 6. Learning Curve Analysis

The learning curve showed that training ROC-AUC decreased as more training data was introduced, while validation ROC-AUC remained close to 0.50–0.52.

This indicates that the models have limited predictive signal.

## 7. Validation Curve Analysis

The validation curve was used to evaluate Logistic Regression performance across different regularization strengths.

The results were used to assess model complexity and identify signs of underfitting or overfitting.

## 8. Bias-Variance Analysis

The final training ROC-AUC was approximately:

**0.5449**

The final validation ROC-AUC was approximately:

**0.5115**

The training-validation gap was:

**0.0334**

The results indicated signs of high bias.

## 9. Statistical Significance

A paired t-test was performed to compare the ROC-AUC scores of Logistic Regression and Random Forest.

The results were:

- T-statistic: 0.0835
- P-value: 0.9375

Since the p-value was greater than 0.05, the difference between the two models was not statistically significant.

## 10. Business Interpretation

The evaluation demonstrates that high accuracy does not necessarily indicate a reliable medical prediction model.

Although the models achieved approximately 80% accuracy, they failed to identify positive heart disease cases effectively.

This highlights the importance of recall, F1-score, ROC-AUC and robust cross-validation in healthcare applications.

The current models should not be deployed clinically without further investigation, improved features, better class representation and additional model development.

## 11. Limitations

The current models showed weak predictive discrimination.

The evaluation also demonstrated that different validation strategies can produce substantially different estimates of performance.

Further investigation of the dataset, target encoding, class distribution, feature quality and model selection would be required before deployment.

## 12. Conclusion

Task 08 demonstrated the importance of reliable model evaluation and cross-validation.

Using multiple validation strategies provided a more complete understanding of model behavior and showed why relying solely on accuracy can result in misleading conclusions.

The evaluation framework provides a stronger basis for making model selection and deployment decisions in a healthcare environment.