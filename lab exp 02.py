#2. Scenario: You are a data analyst working for a company that sells products online. You have been  tasked with analyzing the sales data for the past month. The data is stored in a NumPy array. 
#Question: How would you find the average price of all the products sold in the past month? Assume  3x3 matrix with each row representing the sales for a different product

import numpy as np

# 3x3 matrix
# Rows = Different products
# Columns = Sales prices during the month

sales_data = np.array([
    [100, 120, 110],
    [200, 180, 220],
    [150, 160, 170]
])

# Calculate the average price of all products sold
average_price = np.mean(sales_data)

print("Sales Data:")
print(sales_data)

print("\nAverage Price of All Products Sold =", average_price)
