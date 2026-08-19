#4. Scenario: You are working on a project that involves analyzing the sales performance of a company  over the past four quarters. The quarterly sales data is stored in a NumPy array named sales_data,  where each element represents the sales amount for a specific quarter. 
#Your task is to calculate the  total sales for the year and determine the percentage increase in sales from the first quarter to the fourth  quarter
import numpy as np

sales_data = np.array([50000, 60000, 70000, 90000, 95000, 100000])

total_sales = np.sum(sales_data)

percentage_increase = ((sales_data[-1] - sales_data[0]) / sales_data[0]) * 100

print("Total Sales:", total_sales)
print("Percentage Increase:", percentage_increase, "%")
