import numpy as np

def chi_square_manual(observed):
    # Calculate sum of each row (row-wise totals)
    row_totals = observed.sum(axis=1) 

    # Calculate sum of each column (column-wise totals)
    col_totals = observed.sum(axis=0)     
    
    # Calculate total sum of all observations
    total = observed.sum()     

    # Compute expected frequencies using outer product formula:
    # expected[i][j] = (row_total[i] * col_total[j]) / total
    expected = np.outer(row_totals, col_totals) / total
    
    # Apply Chi-Square formula:
    # χ² = Σ ((Observed - Expected)^2 / Expected)
    chi_square = ((observed - expected) ** 2 / expected).sum()
    return chi_square
