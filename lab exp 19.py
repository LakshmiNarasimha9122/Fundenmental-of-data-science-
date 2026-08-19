import pandas as pd
from collections import Counter
import string
data = pd.read_csv("reviews.csv")
# Remove leading/trailing spaces from column names
data.columns = data.columns.str.strip()
print("Columns:", data.columns)
text = " ".join(data["Review"].astype(str))
text = text.lower()
text = text.translate(str.maketrans("", "", string.punctuation))
words = text.split()
frequency = Counter(words)
for word, count in frequency.items():
    print(word, ":", count)
