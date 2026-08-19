#5. Scenario: You are a data analyst working for a car manufacturing company. As part of your analysis,  you have a dataset containing information about the fuel efficiency of different car models. The dataset is stored in a NumPy array named fuel_efficiency, where each element represents the fuel efficiency (in miles per gallon) of a specific car model. Your task is to calculate the average fuel efficiency and  determine the percentage improvement in fuel efficiency between two car models. 
#Question: How would you use NumPy arrays and arithmetic operations to calculate the average fuel  efficiency and determine the percentage improvement in fuel efficiency between two car models?

import numpy as np
import pandas as pd

data = pd.read_csv("fuel_efficiency.csv")

fuel_efficiency = data["Fuel_Efficiency"].to_numpy()

average_efficiency = np.mean(fuel_efficiency)

percentage_improvement = (
    (fuel_efficiency[-1] - fuel_efficiency[0])
    / fuel_efficiency[0]
) * 100

print("Fuel Efficiency:", fuel_efficiency)
print("Average Fuel Efficiency:", average_efficiency)
print("Percentage Improvement:", round(percentage_improvement, 2), "%")
