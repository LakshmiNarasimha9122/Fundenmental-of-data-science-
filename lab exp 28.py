import pandas as pd
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv("car_prices.csv")

print("Car Dataset:")
print(df)

brand_map = {
    "Toyota": 1,
    "Honda": 2,
    "BMW": 3,
    "Ford": 4,
    "Audi": 5,
    "Hyundai": 6
}

engine_map = {
    "Petrol": 1,
    "Diesel": 2
}

df["Brand"] = df["Brand"].map(brand_map)
df["EngineType"] = df["EngineType"].map(engine_map)

X = df[["Mileage", "Age", "Brand", "EngineType"]]
y = df["Price"]

model = DecisionTreeRegressor(random_state=42)
model.fit(X, y)

print("\nEnter New Car Details")

mileage = float(input("Enter Mileage: "))
age = float(input("Enter Age: "))
brand = input("Enter Brand: ")
engine = input("Enter Engine Type: ")

brand_value = brand_map[brand]
engine_value = engine_map[engine]

new_car = [[mileage, age, brand_value, engine_value]]

predicted_price = model.predict(new_car)[0]

print("\nPredicted Car Price:", round(predicted_price, 2))

node_indicator = model.decision_path(new_car)
leaf_id = model.apply(new_car)

tree = model.tree_

print("\nDecision Path:")

node_index = node_indicator.indices[
    node_indicator.indptr[0]:node_indicator.indptr[1]
]

for node_id in node_index:

    if node_id == leaf_id[0]:
        print("Reached leaf node -> Predicted Price:",
              round(tree.value[node_id][0][0], 2))
    else:
        feature = tree.feature[node_id]
        threshold = tree.threshold[node_id]

        feature_name = X.columns[feature]
        value = new_car[0][feature]

        if value <= threshold:
            print(
                feature_name,
                "=",
                value,
                "<=",
                round(threshold, 2),
                "-> Go LEFT"
            )
        else:
            print(
                feature_name,
                "=",
                value,
                ">",
                round(threshold, 2),
                "-> Go RIGHT"
            )
