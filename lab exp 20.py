import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import string
# Read CSV file
data = pd.read_csv("data.csv")
# Combine all feedback into one string
text = " ".join(data["feedback"].astype(str))
text = text.lower()
text = text.translate(str.maketrans("", "", string.punctuation))
stop_words = {
    "the", "and", "is", "to", "a", "an", "of", "in",
    "for", "with", "on", "at", "this", "that", "very"
}
words = [word for word in text.split() if word not in stop_words]
frequency = Counter(words)
N = int(input("Enter the value of N: "))
# Top N words
top_words = frequency.most_common(N)
print("\nTop", N, "Most Frequent Words\n")
for word, count in top_words:
    print(word, ":", count)
# Prepare data for graph
words = [item[0] for item in top_words]
counts = [item[1] for item in top_words]
# Bar graph
plt.bar(words, counts)
plt.title("Top Frequent Words")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()
