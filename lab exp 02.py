#2. Scenario: You are a data analyst working for a company that sells products online. You have been  tasked with analyzing the sales data for the past month. The data is stored in a NumPy array. 
#Question: How would you find the average price of all the products sold in the past month? Assume  3x3 matrix with each row representing the sales for a different product

import numpy as np
import pandas as pd

data = pd.read_csv("sales_data.csv")

sales_data = data.to_numpy()

average_price = np.mean(sales_data)

print("Sales Data:")
print(sales_data)

print("\nAverage Price of All Products Sold =", round(average_price, 2))
