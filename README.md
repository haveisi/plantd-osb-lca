# Plantd vs OSB — Screening LCA Workflow

## What this is

A structured, reproducible workflow to build a **screening-level life cycle assessment (LCA)** comparing:

- Plantd structural panels  
- Conventional OSB structural panels  

Built using:
- Excel (data extraction)
- Python (data cleaning + modeling)
- openLCA-ready structure

---

## Why this matters

Structural panels are widely used in construction.  
Even small reductions in embodied carbon scale quickly.

This project explores whether a **bio-based structural panel (Plantd)** could reduce emissions compared to **OSB**, which is the real benchmark.

---

## Functional unit

**1 m² structural panel**  
Used for wall or roof sheathing.

---

## System boundary

**Cradle-to-gate (screening level)**

---

## Workflow

### 1. Data extraction
- Extracted from technical reports and LCA literature  
- Stored in Excel  

### 2. Data cleaning
```text
src/02_clean_openlca_inputs.py