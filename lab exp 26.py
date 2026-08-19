import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

df = pd.read_csv("clinical_trial.csv")

control = df[df["Group"] == "Control"]["Effect"]
treatment = df[df["Group"] == "Treatment"]["Effect"]

t_stat, p_value = ttest_ind(control, treatment)

print("Control Group Mean:", control.mean())
print("Treatment Group Mean:", treatment.mean())
print("T-statistic:", t_stat)
print("P-value:", p_value)

alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis")
    print("Treatment is statistically significant")
else:
    print("Fail to reject the null hypothesis")
    print("Treatment is not statistically significant")

plt.figure(figsize=(8, 5))

plt.boxplot(
    [control, treatment],
    tick_labels=["Control", "Treatment"]
)

plt.ylabel("Treatment Effect")
plt.title("Clinical Trial: Control vs Treatment")

plt.text(
    1.5,
    max(df["Effect"]) + 1,
    "p-value = " + str(round(p_value, 4)),
    ha="center"
)

plt.grid(axis="y")
plt.show()
