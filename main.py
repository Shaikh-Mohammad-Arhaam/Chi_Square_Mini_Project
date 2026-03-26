# Entry point: loads data, runs chi-square tests, and prints results
import numpy as np
import pandas as pd
from chi_square.manual import chi_square_manual
from chi_square.scipy_test import chi_square_scipy

#Load CSV data
data = pd.read_csv('data/rental_data.csv')

print("Dataset:\n", data)
#  Extract observed frequency matrix from the dataframe
observed = data[['Booked', 'NotBooked']].values

print("\nObserved Data:\n", observed)
#  Run manual chi-square calculation for comparison

chi_manual = chi_square_manual(observed)
print("\nManual Chi-Square:", chi_manual)

chi2, p = chi_square_scipy(observed)
print("\nSciPy Chi-Square:", chi2)
# Hypothesis decision: p < 0.05 rejects independence
print("p-value:", p)

if p < 0.05:
    print("\nConclusion: Variables are dependent")
else:
    print("\nConclusion: Variables are independent")
