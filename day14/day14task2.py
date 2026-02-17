import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

data = {
    "Age": [22, 25, 30, 35, 40, 28, 32, 45, 50, 38],
    "Salary": [25000, 30000, 50000, 70000, 90000, 45000, 60000, 120000, 150000, 80000]
}

df = pd.DataFrame(data)

print("Original Data:\n")
print(df)


standard_scaler = StandardScaler()
df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)

print("\nStandardized Data:\n")
print(df_standardized)

minmax_scaler = MinMaxScaler()
df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)

print("\nNormalized Data:\n")
print(df_normalized)

plt.figure(figsize=(15,4))

plt.subplot(1,3,1)
plt.hist(df["Salary"], bins=5)
plt.title("Original Salary")


plt.subplot(1,3,2)
plt.hist(df_standardized["Salary"], bins=5)
plt.title("Standardized Salary")

plt.subplot(1,3,3)
plt.hist(df_normalized["Salary"], bins=5)
plt.title("Normalized Salary")

plt.tight_layout()
plt.show()
