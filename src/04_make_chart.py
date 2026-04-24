import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "outputs"

df = pd.read_csv(OUTPUT_DIR / "screening_gwp_results.csv")

plt.figure(figsize=(10, 6))
plt.bar(df["scenario"], df["gwp_kgco2e_per_m2"])

plt.ylabel("GWP kg CO2e per m²")
plt.xlabel("Scenario")
plt.title("Screening GWP: Plantd Structural Panel vs OSB")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

chart_path = OUTPUT_DIR / "plantd_vs_osb_screening_chart.png"
plt.savefig(chart_path, dpi=300)
plt.show()

print("Saved chart:")
print(chart_path)