import pandas as pd
from scipy import stats

# Read CSV file
df = pd.read_csv("conversion_rates.csv")

# Separate Design A and Design B
A = df[df["Design"] == "A"]["Conversion_Rate"]
B = df[df["Design"] == "B"]["Conversion_Rate"]

# Calculate mean
mean_A = A.mean()
mean_B = B.mean()

# Perform independent two-sample t-test
t_stat, p_value = stats.ttest_ind(A, B)

# Display results
print("Mean Conversion Rate of Design A:", round(mean_A, 2))
print("Mean Conversion Rate of Design B:", round(mean_B, 2))

print("\nT-statistic:", round(t_stat, 4))
print("P-value:", round(p_value, 4))

# Test at 5% significance level
alpha = 0.05

if p_value < alpha:
    print("\nThere is a statistically significant difference")
    print("between Design A and Design B.")
else:
    print("\nThere is no statistically significant difference")
    print("between Design A and Design B.")
