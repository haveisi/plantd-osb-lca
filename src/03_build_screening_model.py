import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "outputs"

input_path = OUTPUT_DIR / "openlca_input_table_clean.csv"
df = pd.read_csv(input_path)

# Manual screening assumptions
# These are NOT verified LCA results.
screening = pd.DataFrame([
    {
        "scenario": "OSB_low",
        "material": "Conventional OSB panel",
        "functional_unit": "1 m2 structural panel",
        "gwp_kgco2e_per_m2": 20,
        "data_quality": "proxy estimate",
        "note": "Low baseline estimate"
    },
    {
        "scenario": "OSB_mid",
        "material": "Conventional OSB panel",
        "functional_unit": "1 m2 structural panel",
        "gwp_kgco2e_per_m2": 25,
        "data_quality": "proxy estimate",
        "note": "Mid baseline estimate"
    },
    {
        "scenario": "OSB_high",
        "material": "Conventional OSB panel",
        "functional_unit": "1 m2 structural panel",
        "gwp_kgco2e_per_m2": 30,
        "data_quality": "proxy estimate",
        "note": "High baseline estimate"
    },
    {
        "scenario": "Plantd_low",
        "material": "Plantd structural panel",
        "functional_unit": "1 m2 structural panel",
        "gwp_kgco2e_per_m2": 10,
        "data_quality": "screening estimate",
        "note": "Needs real Plantd LCI"
    },
    {
        "scenario": "Plantd_mid",
        "material": "Plantd structural panel",
        "functional_unit": "1 m2 structural panel",
        "gwp_kgco2e_per_m2": 14,
        "data_quality": "screening estimate",
        "note": "Needs real Plantd LCI"
    },
    {
        "scenario": "Plantd_high",
        "material": "Plantd structural panel",
        "functional_unit": "1 m2 structural panel",
        "gwp_kgco2e_per_m2": 18,
        "data_quality": "screening estimate",
        "note": "Needs real Plantd LCI"
    },
])

# Calculate reduction against OSB midpoint
osb_mid = 25
screening["reduction_vs_osb_mid_percent"] = (
    (osb_mid - screening["gwp_kgco2e_per_m2"]) / osb_mid * 100
).round(1)

output_path = OUTPUT_DIR / "screening_gwp_results.csv"
screening.to_csv(output_path, index=False)

print(screening.to_string(index=False))
print("\nSaved:")
print(output_path)