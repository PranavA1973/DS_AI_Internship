import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("housing_data_500.csv")

# Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(df["Square_Feet"], df["Price"])
plt.title("Square Footage vs Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x=df["City"], y=df["Price"])
plt.title("Price Distribution by City")
plt.xticks(rotation=45)
plt.show()
