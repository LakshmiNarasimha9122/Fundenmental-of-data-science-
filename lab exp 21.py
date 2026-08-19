import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Read data from CSV file
df = pd.read_csv("data2.csv")

# Display the data
print("Data:")
print(df)

# Calculate mean, median and standard deviation
print("\nMean:")
print(df.mean())

print("\nMedian:")
print(df.median())

print("\nStandard Deviation:")
print(df.std())

# Boxplot for Age and %Fat
plt.figure(figsize=(8, 5))
df.boxplot(column=["Age", "%Fat"])
plt.title("Boxplot of Age and Body Fat")
plt.ylabel("Values")
plt.show()

# Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df["Age"], df["%Fat"])
plt.title("Scatter Plot of Age vs %Fat")
plt.xlabel("Age")
plt.ylabel("%Fat")
plt.show()

# Q-Q plot for Age
plt.figure(figsize=(8, 5))
stats.probplot(df["Age"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Age")
plt.show()

# Q-Q plot for %Fat
plt.figure(figsize=(8, 5))
stats.probplot(df["%Fat"], dist="norm", plot=plt)
plt.title("Q-Q Plot of %Fat")
plt.show()
