import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Set random seed for reproducibility
np.random.seed(42)

# -----------------------------
# 1. Normal Distribution (Heights)
# -----------------------------
heights = np.random.normal(loc=170, scale=10, size=1000)
df_heights = pd.DataFrame(heights, columns=["Heights"])

mean_h = df_heights["Heights"].mean()
median_h = df_heights["Heights"].median()

plt.figure()
plt.hist(df_heights["Heights"], bins=30, density=True)
kde = gaussian_kde(df_heights["Heights"])
x_vals = np.linspace(df_heights["Heights"].min(), df_heights["Heights"].max(), 1000)
plt.plot(x_vals, kde(x_vals))
plt.title("Normal Distribution - Human Heights")
plt.axvline(mean_h)
plt.axvline(median_h)
plt.show()

print("Heights -> Mean:", mean_h, "Median:", median_h)


# -----------------------------
# 2. Right-Skewed Distribution (Incomes)
# -----------------------------
incomes = np.random.exponential(scale=50000, size=1000)
df_incomes = pd.DataFrame(incomes, columns=["Incomes"])

mean_i = df_incomes["Incomes"].mean()
median_i = df_incomes["Incomes"].median()

plt.figure()
plt.hist(df_incomes["Incomes"], bins=30, density=True)
kde = gaussian_kde(df_incomes["Incomes"])
x_vals = np.linspace(df_incomes["Incomes"].min(), df_incomes["Incomes"].max(), 1000)
plt.plot(x_vals, kde(x_vals))
plt.title("Right-Skewed Distribution - Household Incomes")
plt.axvline(mean_i)
plt.axvline(median_i)
plt.show()

print("Incomes -> Mean:", mean_i, "Median:", median_i)

scores = 100 - np.random.exponential(scale=10, size=1000)
df_scores = pd.DataFrame(scores, columns=["Scores"])

mean_s = df_scores["Scores"].mean()
median_s = df_scores["Scores"].median()

plt.figure()
plt.hist(df_scores["Scores"], bins=30, density=True)
kde = gaussian_kde(df_scores["Scores"])
x_vals = np.linspace(df_scores["Scores"].min(), df_scores["Scores"].max(), 1000)
plt.plot(x_vals, kde(x_vals))
plt.title("Left-Skewed Distribution - Easy Exam Scores")
plt.axvline(mean_s)
plt.axvline(median_s)
plt.show()

print("Scores -> Mean:", mean_s, "Median:", median_s)
