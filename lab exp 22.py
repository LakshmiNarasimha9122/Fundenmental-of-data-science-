import pandas as pd
from scipy import stats

# Read the data from CSV
df = pd.read_csv("blood_pressures.csv")

# Separate Drug and Placebo groups
drug = df[df["Group"] == "Drug"]["Reduction"]
placebo = df[df["Group"] == "Placebo"]["Reduction"]

# Function to calculate 95% confidence interval
def confidence_interval(data):
    n = len(data)
    mean = data.mean()
    std = data.std()

    # 95% CI using t-distribution
    t_value = stats.t.ppf(0.975, n - 1)

    margin_error = t_value * (std / (n ** 0.5))

    lower = mean - margin_error
    upper = mean + margin_error

    return mean, lower, upper


# Drug group
drug_mean, drug_lower, drug_upper = confidence_interval(drug)

# Placebo group
placebo_mean, placebo_lower, placebo_upper = confidence_interval(placebo)


# Display results
print("95% Confidence Interval for New Drug Group")
print("Mean Reduction:", round(drug_mean, 2))
print("Confidence Interval:",
      round(drug_lower, 2), "to", round(drug_upper, 2))

print("\n95% Confidence Interval for Placebo Group")
print("Mean Reduction:", round(placebo_mean, 2))
print("Confidence Interval:",
      round(placebo_lower, 2), "to", round(placebo_upper, 2))
