import numpy as np


def cohens_d(group1, group2):
    """
    Calculate Cohen's d for two independent groups.
    """

    n1 = len(group1)
    n2 = len(group2)

    mean1 = np.mean(group1)
    mean2 = np.mean(group2)

    var1 = np.var(group1, ddof=1)
    var2 = np.var(group2, ddof=1)

    pooled_std = np.sqrt(
        ((n1 - 1) * var1 + (n2 - 1) * var2)
        / (n1 + n2 - 2)
    )

    return (mean1 - mean2) / pooled_std


def rank_biserial_correlation(u_statistic, n1, n2):
    """
    Calculate rank-biserial correlation from
    a Mann-Whitney U statistic.
    """

    return 1 - (2 * u_statistic) / (n1 * n2)


def cramers_v(chi2_statistic, contingency_table):
    """
    Calculate Cramér's V for a contingency table.
    """

    n = contingency_table.to_numpy().sum()

    rows, cols = contingency_table.shape

    return np.sqrt(
        chi2_statistic /
        (n * min(rows - 1, cols - 1))
    )