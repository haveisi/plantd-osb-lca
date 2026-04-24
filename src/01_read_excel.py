import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
excel_path = BASE_DIR / "data" / "Plantd_openLCA_extracted_dataset.xlsx"

print("BASE_DIR:", BASE_DIR)
print("Looking for file at:", excel_path)
print("Exists?", excel_path.exists())

if not excel_path.exists():
    raise FileNotFoundError(f"File not found: {excel_path}")

sheets = pd.read_excel(excel_path, sheet_name=None)

print("Sheets found:")
for name in sheets:
    print("-", name)

df_input = sheets["openLCA_Input_Table"]

print(df_input.to_string())