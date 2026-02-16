import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis
import numpy as np

np.random.seed(42)

df = pd.read_csv("housing_data_500.csv")

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

print("First 5 Rows:\n", df.head())
print("\nDataset Shape:", df.shape)
print("\nSummary Statistics:\n", df.describe())

plt.figure(figsize=(6, 4))
sns.histplot(df["Price"], kde=True)
plt.title("Distribution of Housing Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

print("\nSkewness of Price:", skew(df["Price"]))
print("Kurtosis of Price:", kurtosis(df["Price"]))

plt.figure(figsize=(6, 4))
sns.countplot(x=df["City"])
plt.title("Number of Houses by City")
plt.xticks(rotation=45)
plt.show()

df["Log_Price"] = np.log1p(df["Price"])

plt.figure(figsize=(6, 4))
sns.histplot(df["Log_Price"], kde=True)
plt.title("Log-Transformed Price Distribution")
plt.xlabel("Log(Price)")
plt.ylabel("Frequency")
plt.show()
