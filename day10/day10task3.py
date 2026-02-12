import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "order.csv"
df = pd.read_csv(csv_path)

if 'Location' in df.columns:
	df['Location'] = df['Location'].astype(str).str.strip().str.title()

	print("Unique values in 'Location' after normalization:")
	print(df['Location'].unique())
else:
	print("Column 'Location' not found in the dataset.")
