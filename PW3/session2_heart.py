import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("heart_disease.csv")

# two groups
disease = df[df["target"] == 1]["thalach"]
healthy = df[df["target"] == 0]["thalach"]
print(len(disease), len(healthy))

# Mann-Whitney test (thalach is not normal)
u_stat, p = stats.mannwhitneyu(disease, healthy)
print("p =", p)

if p < 0.05:
    print("reject H0: the difference is real")
else:
    print("fail to reject H0: cannot claim an effect")

# mean and standard error of each group
mean_d = disease.mean()
se_d = disease.std(ddof=1) / np.sqrt(len(disease))
mean_h = healthy.mean()
se_h = healthy.std(ddof=1) / np.sqrt(len(healthy))
print("disease:", mean_d, "+-", se_d)
print("healthy:", mean_h, "+-", se_h)

# plot with error bars
plt.errorbar([0, 1], [mean_h, mean_d], yerr=[se_h, se_d], fmt="o", capsize=6)
plt.xticks([0, 1], ["healthy", "disease"])
plt.ylabel("thalach")
plt.savefig("session2_means.png")
plt.show()

# Task 5: age vs thalach
rho, p_s = stats.spearmanr(df["age"], df["thalach"])
print("Spearman rho =", rho, "p =", p_s)

plt.figure()
plt.scatter(df["age"], df["thalach"], alpha=0.6)
plt.xlabel("age")
plt.ylabel("thalach")
plt.savefig("session2_age_thalach.png")
plt.show()
# Bonus: how balanced is target?
import numpy as np
props = df["target"].value_counts(normalize=True)
print(props)
entropy = -np.sum(props * np.log2(props))
print("entropy (bits) =", entropy)