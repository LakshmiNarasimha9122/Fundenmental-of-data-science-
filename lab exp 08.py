#8. Scenario: You are a data scientist working for a company that sells products online. You have been  tasked with analyzing the sales data for the past month. The data is stored in a Pandas data frame. 
#Question: How would you find the top 5 products that have been sold the most in the past month? 

import pandas as pd

df = pd.read_csv("sales_data.csv")

top5 = df.groupby("Product_Name")["Quantity_Sold"].sum().sort_values(ascending=False).head(5)

print("Top 5 Most Sold Products:")
print(top5)
