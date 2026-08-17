import numpy as np
from scipy import stats


def select_statistical_test(
    variable_type_1,
    variable_type_2,
    number_of_groups=None,
    non_parametric=False
):
    """
    Recommend an appropriate statistical test based on
    variable types and number of groups.
    """

    if variable_type_1 == "categorical" and variable_type_2 == "categorical":
        return "Chi-square test of independence"

    if variable_type_1 == "numerical" and variable_type_2 == "numerical":
        return "Pearson correlation"

    if variable_type_1 == "numerical" and variable_type_2 == "categorical":

        if number_of_groups == 2:
            if non_parametric:
                return "Mann-Whitney U test"
            return "Independent t-test"

        if number_of_groups is not None and number_of_groups >= 3:
            if non_parametric:
                return "Kruskal-Wallis test"
            return "One-way ANOVA"

    return "No suitable test identified"


def independent_t_test(group1, group2):
    """Perform Welch's independent two-sample t-test."""
    return stats.ttest_ind(
        group1,
        group2,
        equal_var=False
    )


def mann_whitney_test(group1, group2):
    """Perform a two-sided Mann-Whitney U test."""
    return stats.mannwhitneyu(
        group1,
        group2,
        alternative="two-sided"
    )


def one_way_anova(*groups):
    """Perform one-way ANOVA across independent groups."""
    return stats.f_oneway(*groups)


def chi_square_test(contingency_table):
    """Perform chi-square test of independence."""
    return stats.chi2_contingency(contingency_table)


def pearson_correlation(x, y):
    """Calculate Pearson correlation and its p-value."""
    return stats.pearsonr(x, y)