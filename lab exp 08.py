#8. Scenario: You are a data scientist working for a company that sells products online. You have been  tasked with analyzing the sales data for the past month. The data is stored in a Pandas data frame. 
#Question: How would you find the top 5 products that have been sold the most in the past month? 

import pandas as pd

# Sample DataFrame
sales_data = pd.DataFrame({
    'Product_Name': ['Laptop', 'Mouse', 'Keyboard', 'Laptop',
                     'Mouse', 'Laptop', 'Keyboard', 'Monitor'],
    'Quantity_Sold': [5, 10, 8, 7, 6, 4, 9, 3]
})

# Find Top 5 Most Sold Products
top5_products = sales_data.groupby('Product_Name')['Quantity_Sold'].sum() \
                          .sort_values(ascending=False) \
                          .head(5)

print("Top 5 Most Sold Products:")
print(top5_products)
