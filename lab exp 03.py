#3. Scenario: You are working on a project that involves analyzing a dataset containing information about houses in a neighborhood. The dataset is stored in a CSV file, and you have imported it into a NumPy array named house_data. Each row of the array represents a house, and the columns contain  various features such as the number of bedrooms, square footage, and sale price. 
#Question: Using NumPy arrays and operations, how would you find the average sale price of houses  with more than four bedrooms in the neighborhood? 

import numpy as np

num_houses = int(input("Enter number of houses: "))

house_data = []

for i in range(num_houses):
    print(f"\nEnter details for House {i + 1}:")
    
    bedrooms = int(input("Bedrooms: "))
    square_footage = float(input("Square Footage: "))
    sale_price = float(input("Sale Price: "))
    
    house_data.append([bedrooms, square_footage, sale_price])

house_data = np.array(house_data)

houses = house_data[house_data[:, 0] > 4]

print("\nHouses with more than 4 bedrooms:")
print(houses)

if len(houses) > 0:
    average_price = np.mean(houses[:, 2])
    print("\nAverage Sale Price =", average_price)
else:
    print("\nNo houses with more than 4 bedrooms.")
