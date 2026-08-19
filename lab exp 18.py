import pandas as pd
data = pd.read_csv("post_data.csv")
print("Post Data:\n")
print(data)
likes_frequency = data["Likes"].value_counts().sort_index()
print("\nFrequency Distribution of Likes:\n")
print(likes_frequency)
