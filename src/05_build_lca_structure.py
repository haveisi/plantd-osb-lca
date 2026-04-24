import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "outputs"

df = pd.read_csv(OUTPUT_DIR / "openlca_input_table_clean.csv")

# Build simplified LCA structure
lca_rows = []

for _, row in df.iterrows():
    exchange = row.get("process___exchange", "")
    value = row.get("value", None)
    status = row.get("data_status", "")

    # Skip meaningless rows
    if pd.isna(exchange):
        continue

    # Replace missing with assumptions
    if str(value).upper() == "MISSING" or pd.isna(value):
        value = 1  # placeholder
        quality = "assumed"
    else:
        quality = "reported"

    lca_rows.append({
        "flow_name": exchange,
        "amount": value,
        "unit": row.get("unit", ""),
        "type": "input",
        "data_quality": quality
    })

lca_df = pd.DataFrame(lca_rows)

output_path = OUTPUT_DIR / "plantd_lca_structure.csv"
lca_df.to_csv(output_path, index=False)

print(lca_df.to_string())
print("\nSaved:", output_path)