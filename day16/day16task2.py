import numpy as np
import pandas as pd

np.random.seed(42)

data = np.random.normal(loc=50, scale=10, size=1000)

data = np.append(data, [120, 130, -20])

df = pd.DataFrame(data, columns=["Value"])

mean = df["Value"].mean()
std = df["Value"].std()

print("Mean (μ):", mean)
print("Standard Deviation (σ):", std)

df["z_score"] = (df["Value"] - mean) / std

outliers = df[np.abs(df["z_score"]) > 3]

print("\nOutliers Detected:")
print(outliers)

print("\nTotal Outliers:", len(outliers))
