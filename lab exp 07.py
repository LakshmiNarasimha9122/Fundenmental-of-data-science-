#7. Scenario: You are working as a data analyst for an e-commerce company. You have been given a  dataset containing information about customer orders, stored in a Pandas DataFrame named order_data. The DataFrame has columns for customer ID, order date, product name, and order quantity.  Your task is to analyze the data and answer specific questions about the orders. 
#Question: Using Pandas DataFrame operations, how would you find the following information from  the order_data DataFrame: 
#1. The total number of orders made by each customer. 
#2. The average order quantity for each product. 
#3. The earliest and latest order dates in the dataset. 
import pandas as pd

df = pd.read_csv("order_data.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("1. Total Orders:")
print(df.groupby("Customer_ID").size())

print("\n2. Average Quantity:")
print(df.groupby("Product_Name")["Order_Quantity"].mean())

print("\n3. Earliest:", df["Order_Date"].min())
print("Latest:", df["Order_Date"].max())
