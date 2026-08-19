#2. Scenario: You are a data analyst working for a company that sells products online. You have been  tasked with analyzing the sales data for the past month. The data is stored in a NumPy array. 
#Question: How would you find the average price of all the products sold in the past month? Assume  3x3 matrix with each row representing the sales for a different product

import numpy as np

rows = int(input("Enter number of products: "))
columns = int(input("Enter number of sales prices for each product: "))

sales_data = []

for i in range(rows):
    print(f"\nEnter sales prices for Product {i + 1}:")
    product_sales = []

    for j in range(columns):
        price = float(input(f"Price {j + 1}: "))
        product_sales.append(price)

    sales_data.append(product_sales)

sales_data = np.array(sales_data)

average_price = np.mean(sales_data)

print("\nSales Data:")
print(sales_data)

print("\nAverage Price of All Products Sold =", average_price)
