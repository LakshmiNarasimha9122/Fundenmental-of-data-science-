import numpy as np
import pandas as pd
from scipy import stats

# Read data from CSV file
data = pd.read_csv("rare_elements.csv")

# Convert concentration column into NumPy array
values = data["Concentration"].to_numpy()

# Get user inputs
n = int(input("Enter sample size: "))
confidence = float(input("Enter confidence level (%): "))
precision = float(input("Enter desired level of precision: "))

# Select the required sample
sample = values[:n]

# Point estimation - sample mean
mean = np.mean(sample)

# Sample standard deviation
std = np.std(sample, ddof=1)

# Significance level
alpha = 1 - confidence / 100

# t-critical value
t_value = stats.t.ppf(1 - alpha / 2, n - 1)

# Margin of error
margin_error = t_value * (std / np.sqrt(n))

# Confidence interval
lower = mean - margin_error
upper = mean + margin_error

# Display results
print("\n--- Results ---")
print("Sample Size:", n)
print("Sample Mean:", round(mean, 4))
print("Standard Deviation:", round(std, 4))
print("Confidence Level:", confidence, "%")
print("Desired Precision:", precision)
print("Margin of Error:", round(margin_error, 4))

print("\n95%/Specified Confidence Interval:")
print("Lower Limit:", round(lower, 4))
print("Upper Limit:", round(upper, 4))
