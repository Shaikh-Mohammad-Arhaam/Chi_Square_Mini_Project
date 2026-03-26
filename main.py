import numpy as np
import pandas as pd
from chi_square.manual import chi_square_manual
from chi_square.scipy_test import chi_square_scipy

# Load CSV data
data = pd.read_csv('data/rental_data.csv')

print("Dataset:\n", data)

observed = data[['Booked', 'NotBooked']].values

print("\nObserved Data:\n", observed)

chi_manual = chi_square_manual(observed)
print("\nManual Chi-Square:", chi_manual)

chi2, p = chi_square_scipy(observed)
print("\nSciPy Chi-Square:", chi2)
print("p-value:", p)

if p < 0.05:
    print("\nConclusion: Variables are dependent")
else:
    print("\nConclusion: Variables are independent")
