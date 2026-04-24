# Plantd vs OSB — Screening LCA Workflow

## Overview

This project develops a structured and reproducible workflow for a screening-level life cycle assessment (LCA) comparing:

- Plantd structural panels  
- Conventional OSB (Oriented Strand Board) structural panels  

The workflow integrates Excel-based data extraction with Python-driven data cleaning, modeling, and visualization. Outputs are structured to support future integration with openLCA.

---

## Objective

The objective is to assess whether a bio-based structural panel (Plantd) may offer lower embodied carbon compared to conventional OSB, which serves as the appropriate structural benchmark.

---

## Functional Unit

1 m² of structural panel used for wall or roof sheathing, assuming equivalent functional performance.

---

## System Boundary

Cradle-to-gate (screening-level boundary)

---

## Methodological Approach

### Data Sources
- Plantd structural panel technical report  
- LCA literature on bio-based construction panels  
- Comparative studies of conventional building materials  

### Workflow

**1. Data Extraction**  
Data were extracted from technical documents and literature and compiled into a structured Excel dataset.

**2. Data Cleaning and Structuring**  
`src/02_clean_openlca_inputs.py`  
- Standardized variable names  
- Structured inputs for modeling  
- Exported cleaned dataset  

**3. Screening Model Development**  
`src/03_build_screening_model.py`  
- Established OSB baseline scenarios  
- Developed Plantd emission estimates  
- Calculated comparative performance  

**4. Visualization**  
`src/04_make_chart.py`  
- Generated comparative emissions chart  

**5. LCA Process Structuring**  
`src/05_build_lca_structure.py`  
- Translated extracted inputs into LCA-style flows  
- Constructed a simplified foreground process model  

---

## Results (Screening Level)

| Scenario      | GWP (kg CO2e/m²) |
|--------------|------------------|
| OSB (low)    | 20 |
| OSB (mid)    | 25 |
| OSB (high)   | 30 |
| Plantd (low) | 10 |
| Plantd (mid) | 14 |
| Plantd (high)| 18 |

Estimated reduction relative to the OSB midpoint scenario is approximately 30% to 60%.

---

## Foreground LCA Process Structure

A simplified foreground process was constructed to represent the Plantd panel using the following input categories:

- Biomass feedstock (plant strands)  
- Binder or resin  
- Electricity for manufacturing  
- Thermal energy for drying and pressing  
- Transport of biomass  
- Packaging  

Where primary data were unavailable, placeholder values were introduced and explicitly flagged. This preserves model structure while maintaining transparency and enabling future refinement.

---

## Outputs

- Cleaned dataset: `outputs/openlca_input_table_clean.csv`  
- Screening model results: `outputs/screening_gwp_results.csv`  
- LCA structure file: `outputs/plantd_lca_structure.csv`  
- Visualization: `outputs/plantd_vs_osb_screening_chart.png`  

---

## Limitations

This analysis is a screening-level assessment and does not constitute a full LCA.

The Plantd technical documentation provides structural and performance data but does not include a complete life cycle inventory (LCI). Key missing elements include:

- Material composition and mass per functional unit  
- Binder/resin type and proportion  
- Manufacturing energy consumption  
- Transport distances and logistics  
- End-of-life assumptions  

All results should therefore be interpreted as preliminary estimates.

---

## Path to Full LCA

To develop a complete and verifiable LCA, the following steps are required:

- Incorporate an OSB Environmental Product Declaration (EPD) or database dataset  
- Develop a detailed Plantd foreground inventory  
- Integrate with an LCA database (e.g., ecoinvent) in openLCA  
- Apply a recognized LCIA method (e.g., IPCC GWP 100a)  

---

## Project Structure

```

plantd-osb-lca/
│
├── data/
│   └── Plantd_openLCA_extracted_dataset.xlsx
│
├── outputs/
│   ├── openlca_input_table_clean.csv
│   ├── screening_gwp_results.csv
│   ├── plantd_lca_structure.csv
│   └── plantd_vs_osb_screening_chart.png
│
├── src/
│   ├── 01_read_excel.py
│   ├── 02_clean_openlca_inputs.py
│   ├── 03_build_screening_model.py
│   ├── 04_make_chart.py
│   └── 05_build_lca_structure.py
│
├── docs/
│   └── methodology.md
│
├── README.md
├── requirements.txt
└── .gitignore

```

---

## Key Takeaways

This project demonstrates:

- Structuring incomplete sustainability data into a usable analytical format  
- Developing a transparent and reproducible screening model  
- Explicitly handling data gaps in LCA modeling  
- Preparing datasets for integration into professional LCA tools  

---

## Disclaimer

This project is intended for analytical and educational purposes. Results should not be interpreted as verified environmental performance claims.
```