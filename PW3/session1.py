import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("heart_disease.csv")
print(df.shape)
print(df.head())

cols = ["age", "chol", "trestbps", "thalach"]
continuous_data = df[cols]
print(continuous_data.describe())

# histograms
continuous_data.hist(figsize=(10, 8))
plt.tight_layout()
plt.savefig("session1_histograms.png")
plt.show()

# Q-Q plots
for c in cols:
    stats.probplot(df[c], dist="norm", plot=plt)
    plt.title("Q-Q plot: " + c)
    plt.savefig("qq_" + c + ".png")
    plt.show()

# Shapiro-Wilk
for c in cols:
    W, p = stats.shapiro(df[c])
    print(c, "W =", round(W, 4), "p =", p)
    if p < 0.05:
        print("  reject H0 -> not normal")
    else:
        print("  fail to reject H0 -> normal OK")