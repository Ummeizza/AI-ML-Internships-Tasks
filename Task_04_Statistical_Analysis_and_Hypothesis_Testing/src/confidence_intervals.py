import numpy as np
from scipy import stats


def mean_difference_ci(group1, group2, confidence=0.95):
    """
    Calculate a confidence interval for the difference
    between two independent group means using Welch's method.
    """

    mean1 = np.mean(group1)
    mean2 = np.mean(group2)

    n1 = len(group1)
    n2 = len(group2)

    var1 = np.var(group1, ddof=1)
    var2 = np.var(group2, ddof=1)

    difference = mean1 - mean2

    standard_error = np.sqrt(
        var1 / n1 + var2 / n2
    )

    degrees_of_freedom = (
        (var1 / n1 + var2 / n2) ** 2
        /
        (
            ((var1 / n1) ** 2 / (n1 - 1))
            +
            ((var2 / n2) ** 2 / (n2 - 1))
        )
    )

    alpha = 1 - confidence

    critical_value = stats.t.ppf(
        1 - alpha / 2,
        degrees_of_freedom
    )

    margin_of_error = critical_value * standard_error

    return (
        difference - margin_of_error,
        difference + margin_of_error
    )


def correlation_ci(r, n, confidence=0.95):
    """
    Calculate a confidence interval for Pearson correlation
    using Fisher's z-transformation.
    """

    z = np.arctanh(r)

    standard_error = 1 / np.sqrt(n - 3)

    alpha = 1 - confidence

    critical_value = stats.norm.ppf(
        1 - alpha / 2
    )

    z_lower = z - critical_value * standard_error
    z_upper = z + critical_value * standard_error

    return (
        np.tanh(z_lower),
        np.tanh(z_upper)
    )