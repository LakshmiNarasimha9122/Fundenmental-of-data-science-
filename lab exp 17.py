import pandas as pd
data = pd.read_csv("cust_data.csv")
print("Customer Data:\n")
print(data)
age_frequency = data["Age"].value_counts().sort_index()
print("\nFrequency Distribution of Customer Ages:\n")
print(age_frequency)
