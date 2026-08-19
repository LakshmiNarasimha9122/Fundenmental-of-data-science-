import pandas as pd
from scipy import stats
import numpy as np

# Read the CSV file
df = pd.read_csv("customer_reviews.csv")

# Get the ratings
ratings = df["Rating"]

# Calculate sample statistics
n = len(ratings)
mean = ratings.mean()
std = ratings.std()

# 95% confidence level
confidence = 0.95
alpha = 1 - confidence

# Calculate t-critical value
t_value = stats.t.ppf(1 - alpha / 2, n - 1)

# Calculate margin of error
margin_error = t_value * (std / np.sqrt(n))

# Calculate confidence interval
lower = mean - margin_error
upper = mean + margin_error

# Display results
print("Customer Reviews Analysis")
print("-------------------------")

print("Number of Reviews:", n)
print("Mean Rating:", round(mean, 2))
print("Standard Deviation:", round(std, 2))

print("\n95% Confidence Interval")
print("Lower Limit:", round(lower, 2))
print("Upper Limit:", round(upper, 2))
