\# Chi-Square Test Vehicle Rental Analysis



\## Objective

The objective of this project is to analyze whether the type of vehicle (Car or Bike) has a significant effect on booking success using the Chi-Square Test of Independence.



\## Methodology

This project uses two approaches:

\- Manual calculation of the Chi-Square statistic using the mathematical formula

\- Validation using the SciPy library (`chi2\_contingency`)



The observed data is compared with expected values to determine whether the variables are independent or dependent.



\## Formula

Chi-Square = Σ (O - E)^2 / E  

Where:

\- O = Observed values  

\- E = Expected values  



\## Dataset

The dataset represents booking outcomes for two vehicle types:



\- Car → Booked: 50, Not Booked: 20  

\- Bike → Booked: 30, Not Booked: 40  



This data is used to form a contingency table for analysis.



\## Results

\- Chi-Square Value: Computed using both manual and SciPy methods  

\- p-value: Indicates statistical significance of the relationship  



\## Interpretation

\- If p < 0.05 → Reject null hypothesis → Variables are dependent  

\- If p ≥ 0.05 → Fail to reject null hypothesis → Variables are independent  



\## Libraries Used

\- NumPy → for numerical operations  

\- SciPy → for statistical testing  

\- Matplotlib → for data visualization  



\## How to Run

1\. Install required libraries:

&#x20;  pip install -r requirements.txt  



2\. Execute the program:

&#x20;  python main.py  



The output will display the Chi-Square value, p-value, and final conclusion.

