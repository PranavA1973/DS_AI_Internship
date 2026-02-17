import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual", "Automatic"],
    "Color": ["Red", "Blue", "Green", "Blue", "Red"]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)

le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])

print("\nAfter Label Encoding (Transmission):\n")
print(df)

df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print("\nAfter One-Hot Encoding (Color):\n")
print(df)

print("\nFinal Processed Dataset:\n")
print(df)
