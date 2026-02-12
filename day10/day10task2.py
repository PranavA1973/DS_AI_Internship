import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "customer_orders.csv"

if csv_path.exists():
    df = pd.read_csv(csv_path)
else:
    raise FileNotFoundError("Dataset not found. Expected 'customer_orders.csv'.")

print("Initial data types:")
print(df.dtypes)

if "price" in df.columns:
    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )
else:
    print("Column 'price' not found.")

if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
else:
    print("Column 'date' not found.")

print("\nData types after conversion:")
print(df.dtypes)
