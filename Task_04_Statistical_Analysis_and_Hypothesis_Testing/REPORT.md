# Task 04 — Statistical Analysis and Hypothesis Testing

## 1. Business Problem

A health insurance company wants to determine whether smoking status, BMI, and region are associated with differences in medical charges. The analysis aims to provide statistically supported evidence that can help inform fair and data-driven insurance pricing decisions.

## 2. Dataset

The analysis uses the Medical Cost Personal dataset.

The dataset contains 1,338 original observations and 7 variables:

- age
- sex
- bmi
- children
- smoker
- region
- charges

One duplicate row was identified and removed, resulting in 1,337 observations for the statistical analysis.

No missing values were found.

## 3. Data Processing

The dataset was loaded and inspected for data types, missing values, duplicate records, and basic statistical properties.

The duplicate row was removed to prevent repeated observations from affecting the statistical analysis. Categorical variables were retained in their original form because the selected statistical tests operate on categorical groupings directly.

## 4. Statistical Methods

The following statistical methods were applied:

- Independent Welch's t-test
- Mann-Whitney U test
- Cohen's d
- Rank-biserial correlation
- 95% confidence interval for mean difference
- Pearson correlation
- 95% confidence interval for Pearson correlation
- One-way ANOVA
- Tukey HSD multiple comparison test
- Chi-square test of independence
- Cramér's V

Reusable helper functions were implemented in the `src/` directory to improve modularity and reproducibility.

## 5. Smoking Status and Medical Charges

The mean medical charge for smokers was approximately $32,050.23 compared with $8,440.66 for non-smokers.

An independent t-test produced a t-statistic of 32.7423 with a p-value below 0.001, indicating a statistically significant difference.

The Mann-Whitney U test also produced a statistically significant result (p < 0.001).

The effect sizes were:

- Cohen's d = 3.1603
- Rank-biserial correlation = -0.9492

These effect sizes indicate a very large practical difference between smokers and non-smokers.

The 95% confidence interval for the mean difference was approximately $22,190.79 to $25,028.35.

## 6. BMI and Medical Charges

Pearson correlation was used to examine the relationship between BMI and medical charges.

The correlation coefficient was:

r = 0.1984

The p-value was below 0.001, indicating a statistically significant positive relationship.

However, the relatively small correlation coefficient indicates that the relationship is weak in practical terms.

The 95% confidence interval for the correlation was approximately 0.1463 to 0.2494.

## 7. Regional Differences

A one-way ANOVA was used to compare medical charges across the four regions.

The ANOVA produced:

- F-statistic = 2.9261
- p-value = 0.0328

Since the p-value is below 0.05, the null hypothesis of equal group means was rejected.

Tukey HSD was subsequently applied to identify pairwise differences while controlling the family-wise error rate.

## 8. Sex and Smoking Status

A chi-square test of independence was used to examine the relationship between sex and smoking status.

The test produced:

- Chi-square statistic = 7.4691
- p-value = 0.00628
- Degrees of freedom = 1

The result indicates a statistically significant association between sex and smoking status.

However, Cramér's V was only 0.0747, indicating that the strength of this association is very weak.

## 9. Baseline Comparison

A descriptive baseline comparing mean and median charges between smokers and non-smokers showed a substantial difference before formal hypothesis testing.

| Group | Mean Charges | Median Charges |
|---|---:|---:|
| Non-Smokers | 8440.66 | 7345.73 |
| Smokers | 32050.23 | 34456.35 |

The descriptive results are consistent with the formal hypothesis tests and effect-size measures.

## 10. Modular Implementation

The statistical analysis was organized into reusable modules:

- `statistical_tests.py` — statistical test selection and test functions
- `effect_sizes.py` — effect-size calculations
- `confidence_intervals.py` — confidence interval calculations

The modular functions were verified against the calculations performed during exploratory analysis and reproduced the same results.

## 11. Business Interpretation

Smoking status showed the strongest relationship with medical charges among the factors investigated. Smokers had substantially higher medical charges than non-smokers, and both parametric and non-parametric tests supported this finding.

BMI showed a statistically significant but relatively weak relationship with charges. Regional differences were statistically significant overall, although the ANOVA result alone does not imply that every region differs from every other region.

The association between sex and smoking status was statistically significant but practically very weak.

These findings suggest that statistical significance should always be interpreted together with effect size and confidence intervals when making business decisions.

## 12. Limitations

- The analysis is observational and therefore does not establish causation.
- The dataset may not represent the entire insured population.
- Statistical significance can be influenced by sample size.
- Other factors may contribute to medical charges but are not fully examined in this analysis.
- Association between smoking and charges should not be interpreted as proof that smoking alone causes the observed difference.

## 13. Conclusion

The analysis provides strong statistical evidence of substantially higher medical charges among smokers. The finding is supported by multiple hypothesis tests, large effect sizes, and a confidence interval that remains well above zero.

BMI has a weak positive relationship with charges, while regional differences are statistically significant overall. The relationship between sex and smoking status is statistically significant but weak in magnitude.

Overall, combining hypothesis tests, effect sizes, confidence intervals, and multiple-comparison correction provides a more reliable basis for interpreting the insurance company's pricing-related questions.