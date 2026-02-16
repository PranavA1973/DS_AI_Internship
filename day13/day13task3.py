import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("housing_data_500.csv")

corr_matrix = df.corr(numeric_only=True)

print("Correlation Matrix:\n", corr_matrix)

# Heatmap visualization
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()

# Find highly correlated pairs
for col in corr_matrix.columns:
    for row in corr_matrix.index:
        if col != row and abs(corr_matrix.loc[row, col]) > 0.8:
            print(f"High correlation between {row} and {col}: {corr_matrix.loc[row, col]:.2f}")

plt.figure(figsize=(6,4))
sns.boxplot(y=df["Price"])
plt.title("Boxplot of Housing Prices")
plt.ylabel("Price")
plt.show()

