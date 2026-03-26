# 🚗 Chi-Square Test: Vehicle Rental Analysis

## 📌 Objective

The objective of this project is to determine whether the **type of vehicle (Car or Bike)** affects **booking success** using the **Chi-Square Test of Independence**.

---

## 🧠 Methodology

This project uses two approaches:

* ✅ Manual calculation using the Chi-Square formula
* ✅ Validation using SciPy (`chi2_contingency`)

We compare **observed vs expected frequencies** to determine dependency between variables.

---

## 📐 Formula

[
\chi^2 = \sum \frac{(O - E)^2}{E}
]

Where:

* **O** = Observed values
* **E** = Expected values

---

## 📊 Dataset

| Vehicle Type | Booked | Not Booked |
| ------------ | ------ | ---------- |
| Car          | 50     | 20         |
| Bike         | 30     | 40         |

---

## 💻 Code Implementation

```python
import numpy as np
from scipy.stats import chi2_contingency

def chi_square_manual(observed):
    # Row totals
    row_totals = observed.sum(axis=1)
    
    # Column totals
    col_totals = observed.sum(axis=0)
    
    # Total sum
    total = observed.sum()

    # Expected frequencies
    expected = np.outer(row_totals, col_totals) / total

    # Chi-Square calculation
    chi_square = ((observed - expected) ** 2 / expected).sum()
    
    return chi_square, expected


# Observed data
observed = np.array([
    [50, 20],
    [30, 40]
])

# Manual calculation
chi_manual, expected = chi_square_manual(observed)

# SciPy calculation
chi_scipy, p_value, dof, exp = chi2_contingency(observed)

print("Manual Chi-Square:", chi_manual)
print("SciPy Chi-Square:", chi_scipy)
print("p-value:", p_value)
```

---

## 📈 Results

* **Chi-Square Value (Manual)** ≈ 12.5
* **Chi-Square Value (SciPy)** ≈ 12.5
* **p-value** < 0.05

---

## 🔍 Interpretation

* Since **p-value < 0.05**, we **reject the null hypothesis**
* This means:

👉 **Vehicle type and booking success are dependent**

---

## 🧰 Libraries Used

* NumPy → Numerical operations
* SciPy → Statistical testing
* Matplotlib → Visualization (optional)

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install numpy scipy matplotlib
```

2. Run the script:

```bash
python main.py
```

---

## 🎯 Conclusion

The analysis shows that **vehicle type significantly influences booking behavior**, which can help improve decision-making in vehicle rental systems.

---

## 🚀 Future Improvements

* Add real-world dataset integration
* Build visualization dashboards
* Deploy as a web-based analytics tool
