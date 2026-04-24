import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

excel_path = DATA_DIR / "Plantd_openLCA_extracted_dataset.xlsx"

df = pd.read_excel(excel_path, sheet_name="openLCA_Input_Table")

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("/", "_")
)

print("Columns:")
print(df.columns.tolist())

print("\nFull cleaned table:")
print(df.to_string())

output_path = OUTPUT_DIR / "openlca_input_table_clean.csv"
df.to_csv(output_path, index=False)

print("\nSaved clean CSV to:")
print(output_path)