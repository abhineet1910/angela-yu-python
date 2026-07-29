"""
generate_data.py
-----------------
Generates a synthetic retail sales dataset (retail_sales.csv) with columns:
[order_id, date, product, category, region, sales, profit]

This script only exists to CREATE sample data so the project runs out of the box.
In real use, you would swap this out for a Kaggle CSV (e.g. "Superstore Sales
Dataset") and skip running this file entirely.
"""

import numpy as np
import pandas as pd

np.random.seed(42)

# ---- Define realistic categories, products, and regions ----
categories = {
    "Furniture": ["Office Chair", "Bookshelf", "Study Table", "Sofa"],
    "Electronics": ["Wireless Mouse", "Bluetooth Speaker", "LED Monitor", "Power Bank"],
    "Stationery": ["Notebook Pack", "Pen Set", "Sticky Notes", "Whiteboard"],
    "Clothing": ["T-Shirt", "Jeans", "Jacket", "Sneakers"],
}
regions = ["North", "South", "East", "West"]

n_rows = 3000

# ---- Randomly generate transaction-level data ----
dates = pd.to_datetime(
    np.random.choice(pd.date_range("2023-01-01", "2024-12-31"), size=n_rows)
)

cat_choices = np.random.choice(list(categories.keys()), size=n_rows)
product_choices = [np.random.choice(categories[c]) for c in cat_choices]
region_choices = np.random.choice(regions, size=n_rows)

# Sales roughly log-normal so it looks like real transaction data (some big orders)
sales = np.round(np.random.lognormal(mean=5.2, sigma=0.6, size=n_rows), 2)

# Profit margin varies by category, with some deliberately loss-making rows
margin_by_category = {"Furniture": 0.12, "Electronics": 0.18, "Stationery": 0.25, "Clothing": 0.20}
profit = []
for cat, s in zip(cat_choices, sales):
    margin = margin_by_category[cat] + np.random.normal(0, 0.08)
    profit.append(round(s * margin, 2))

df = pd.DataFrame({
    "order_id": range(1001, 1001 + n_rows),
    "date": dates,
    "product": product_choices,
    "category": cat_choices,
    "region": region_choices,
    "sales": sales,
    "profit": profit,
})

# ---- Inject some messiness on purpose, so the cleaning step in analysis.py has real work to do ----
# 1. A few missing values
missing_idx = np.random.choice(df.index, size=25, replace=False)
df.loc[missing_idx, "profit"] = np.nan

# 2. A few duplicate rows
df = pd.concat([df, df.sample(10, random_state=1)], ignore_index=True)

# 3. Inconsistent text casing in region/category (common in real exports)
messy_idx = np.random.choice(df.index, size=40, replace=False)
df.loc[messy_idx, "region"] = df.loc[messy_idx, "region"].str.lower()

df = df.sort_values("date").reset_index(drop=True)
df.to_csv("data/retail_sales.csv", index=False)

print(f"Generated data/retail_sales.csv with {len(df)} rows (includes intentional dupes/missing/messy text).")
