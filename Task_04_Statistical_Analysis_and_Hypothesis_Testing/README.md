# Statistical Analysis of Medical Insurance Charges

## Overview

This project investigates the factors associated with medical insurance charges using the Medical Cost Personal dataset.

The main focus of the analysis is to answer practical questions that matter to an insurance provider:

- Do smokers actually have higher medical charges?
- Is BMI meaningfully related to insurance charges?
- Do medical charges differ across regions?
- Is smoking status associated with sex?

Instead of relying only on p-values, the analysis combines hypothesis testing, confidence intervals, and effect sizes to distinguish statistical significance from practical importance.

## Dataset

The analysis uses the Medical Cost Personal dataset containing 1,338 observations and 7 variables:

`age`, `sex`, `bmi`, `children`, `smoker`, `region`, and `charges`.

During preprocessing, one duplicate record was identified and removed. No missing values were found, leaving **1,337 observations** for the analysis.

## Approach

The analysis follows a question-driven statistical workflow.

### 1. Exploratory Analysis

The dataset was first inspected for:

- Data types
- Missing values
- Duplicate records
- Numerical distributions
- Categorical distributions
- Group-level differences

### 2. Smoking Status vs Medical Charges

Smoking status was treated as the primary business question.

Both parametric and non-parametric approaches were used:

- Welch's independent t-test
- Mann-Whitney U test

Effect sizes were also calculated using:

- Cohen's d
- Rank-biserial correlation

A 95% confidence interval was calculated for the difference in mean charges.

### 3. BMI vs Medical Charges

Pearson correlation was used to measure the linear relationship between BMI and charges.

The correlation coefficient was accompanied by:

- p-value
- 95% confidence interval

This allowed the strength of the relationship to be considered separately from statistical significance.

### 4. Regional Differences

A one-way ANOVA was used to compare charges across the four regions.

Because ANOVA only indicates whether at least one group differs, Tukey HSD was subsequently used for pairwise comparisons while controlling the family-wise error rate.

### 5. Sex vs Smoking Status

A chi-square test of independence was used to examine whether sex and smoking status were associated.

Cramér's V was calculated to measure the strength of the association.

## Key Findings

### Smoking Status

Smoking status showed the strongest difference observed in the analysis.

| Group | Mean Charges | Median Charges |
|---|---:|---:|
| Non-Smokers | $8,440.66 | $7,345.73 |
| Smokers | $32,050.23 | $34,456.35 |

The mean difference was approximately **$23,609.57**, with a 95% confidence interval of approximately **$22,190.79–$25,028.35**.

Both the t-test and Mann-Whitney U test produced p-values far below 0.05.

The effect sizes were:

- **Cohen's d = 3.1603**
- **Rank-biserial correlation = -0.9492**

Together, these results indicate that the difference between smoker and non-smoker charges is not only statistically significant but also very large in practical terms.

### BMI

BMI had a statistically significant positive relationship with medical charges:

- **Pearson r = 0.1984**
- **95% CI = 0.1463–0.2494**
- **p < 0.001**

Although statistically significant, the correlation is relatively weak. This is an example of why statistical significance should not be interpreted without considering effect size.

### Region

The one-way ANOVA produced:

- **F = 2.9261**
- **p = 0.0328**

This indicates an overall statistically significant difference in charges across regions. Tukey HSD was used to investigate which specific regional comparisons contributed to the difference.

### Sex and Smoking Status

The chi-square test produced:

- **χ² = 7.4691**
- **p = 0.00628**
- **Cramér's V = 0.0747**

Although the association was statistically significant, the very small Cramér's V indicates that the relationship is weak in magnitude.

## Interpretation

The results suggest that smoking status is considerably more informative for explaining differences in medical charges than the other factors examined in this analysis.

However, these findings represent **associations rather than causal relationships**. The dataset is observational, so the results should not be interpreted as proving that any single factor directly causes a change in insurance charges.

For insurance pricing decisions, statistical significance alone would therefore be insufficient. Effect sizes, confidence intervals, population representativeness, and potential confounding factors should also be considered.

