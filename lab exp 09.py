#9. Scenario: You work for a real estate agency and have been given a dataset containing information  about properties for sale. The dataset is stored in a Pandas DataFrame named property_data. The  DataFrame has columns for property ID, location, number of bedrooms, area in square feet, and listing  price. Your task is to analyze the data and answer specific questions about the properties. 
#Question: Using Pandas DataFrame operations, how would you find the following information from  the property_data DataFrame: 
#1. The average listing price of properties in each location. 
#2. The number of properties with more than four bedrooms. 
#. The property with the largest area. 


import pandas as pd

df = pd.read_csv("property_data.csv")

print("1. Average Price by Location:")
print(df.groupby("Location")["Listing_Price"].mean())

print("\n2. Properties with More Than 4 Bedrooms:")
print((df["Bedrooms"] > 4).sum())

print("\n3. Property with Largest Area:")
print(df.loc[df["Area_sqft"].idxmax()])
