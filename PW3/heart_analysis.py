import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "heart+disease/processed.cleveland.data",
    header=None,
    na_values="?"
)

df.columns = [
    "age", "sex", "cp", "trestbps", "chol",
    "fbs", "restecg", "thalach", "exang",
    "oldpeak", "slope", "ca", "thal", "target"
]

df["target"] = (df["target"] > 0).astype(int)

print(df.shape)
print(df.head())

continuous_columns = ["age", "chol", "trestbps", "thalach"]
continuous_data = df[continuous_columns]

print(continuous_data.head())

continuous_data.hist(figsize=(10, 8))
plt.tight_layout()
plt.savefig("heart_histograms.png")
plt.show()