import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("soccer_players.csv")

print("Soccer Players Dataset")
print(df)

print("\nTop 5 Players by Goals:")
top_goals = df.nlargest(5, "Goals")
print(top_goals[["Name", "Goals"]])

print("\nTop 5 Players by Weekly Salary:")
top_salary = df.nlargest(5, "WeeklySalary")
print(top_salary[["Name", "WeeklySalary"]])

average_age = df["Age"].mean()

print("\nAverage Age:", average_age)

above_average = df[df["Age"] > average_age]

print("\nPlayers Above Average Age:")
print(above_average[["Name", "Age"]])

position_count = df["Position"].value_counts()

print("\nPlayers by Position:")
print(position_count)

plt.figure(figsize=(8, 5))

position_count.plot(kind="bar")

plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.title("Distribution of Players by Position")

plt.xticks(rotation=0)
plt.grid(axis="y")

plt.show()
