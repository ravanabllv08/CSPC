import pandas as pd
from scipy import stats

df = pd.read_csv("chemicals_cancer.csv")
print(df.shape)
print(df.head())

# Task 6: naive analysis
print("--- Task 6: all patients ---")
for c in ["benzene", "cadmium"]:
    r, p = stats.pearsonr(df[c], df["malignancy"])
    print(c, "vs malignancy: r =", round(r, 3), "p =", p)

# pollution_index vs others
print("--- pollution_index vs others ---")
for c in ["benzene", "cadmium", "malignancy"]:
    r, p = stats.pearsonr(df["pollution_index"], df[c])
    print("pollution_index vs", c, ": r =", round(r, 3), "p =", p)

# Task 7: only patients with similar pollution
sub = df[(df["pollution_index"] > 40) & (df["pollution_index"] < 60)]
print("--- Task 7: pollution_index between 40 and 60 ---")
print("patients:", len(sub))
for c in ["benzene", "cadmium"]:
    r, p = stats.pearsonr(sub[c], sub["malignancy"])
    print(c, "vs malignancy: r =", round(r, 3), "p =", p)