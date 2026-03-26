import numpy as np

def chi_square_manual(observed):
    row_totals = observed.sum(axis=1)
    col_totals = observed.sum(axis=0)
    total = observed.sum()

    expected = np.outer(row_totals, col_totals) / total

    chi_square = ((observed - expected) ** 2 / expected).sum()
    return chi_square