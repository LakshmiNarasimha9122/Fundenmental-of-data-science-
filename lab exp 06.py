#6. Scenario: You are a cashier at a grocery store and need to calculate the total cost of a customer's purchase, including applicable discounts and taxes. You have the item prices and quantities in separate  lists, and the discount and tax rates are given as percentages. Your task is to calculate the total cost for  the customer. 
#Question: Use arithmetic operations to calculate the total cost of a customer's purchase, including discounts and taxes, given the item prices, quantities, discount rate, and tax rate? 

import numpy as np
import pandas as pd

data = pd.read_csv("billing_data.csv")

prices = data["Price"].to_numpy()
quantities = data["Quantity"].to_numpy()

discount_rate = data["Discount_Rate"].iloc[0]
tax_rate = data["Tax_Rate"].iloc[0]

subtotal = np.sum(prices * quantities)

discount = subtotal * (discount_rate / 100)

price_after_discount = subtotal - discount

tax = price_after_discount * (tax_rate / 100)

total_cost = price_after_discount + tax

print("Billing Data:")
print(data)

print("\nSubtotal:", subtotal)
print("Discount:", discount)
print("Tax:", tax)
print("Total Cost:", total_cost)
