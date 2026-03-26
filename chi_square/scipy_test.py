from scipy.stats import chi2_contingency

def chi_square_scipy(observed):
    chi2, p, dof, expected = chi2_contingency(observed)
    return chi2, p