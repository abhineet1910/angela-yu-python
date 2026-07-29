"""
analysis.py
-----------------------------------------------------------------------------
Retail Sales EDA & Dashboard

What this script does:
    1. Loads a retail sales CSV [date, product, category, region, sales, profit]
    2. Cleans the data (duplicates, missing values, inconsistent text)
    3. Computes monthly sales trends
    4. Finds the top 5 products by total profit
    5. Computes region-wise performance
    6. Generates 4 charts saved to the outputs/ folder

Run it from the project root with:
    python analysis.py
-----------------------------------------------------------------------------
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------------------------
# 0. SETUP
# ---------------------------------------------------------------------------
DATA_PATH = "data/retail_sales.csv"
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

sns.set_theme(style="whitegrid")  # gives all charts a consistent, clean look


# ---------------------------------------------------------------------------
# 1. LOAD DATA
# ---------------------------------------------------------------------------
print("Loading data...")
df = pd.read_csv(DATA_PATH)
print(f"Raw shape: {df.shape}")


# ---------------------------------------------------------------------------
# 2. CLEAN DATA
# ---------------------------------------------------------------------------
print("\nCleaning data...")

# 2a. Parse date column properly (so we can extract month/year later)
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# 2b. Remove exact duplicate rows (common in raw exports)
before = len(df)
df = df.drop_duplicates()
print(f" - Removed {before - len(df)} duplicate rows")

# 2c. Standardize text columns (fixes things like "north" vs "North")
df["region"] = df["region"].str.strip().str.title()
df["category"] = df["category"].str.strip().str.title()
df["product"] = df["product"].str.strip()

# 2d. Handle missing values in numeric columns
# For "profit", a missing value is filled with the median profit for that
# product's category, since profit margins differ a lot by category —
# this is more accurate than filling with the global median.
df["profit"] = df.groupby("category")["profit"].transform(
    lambda x: x.fillna(x.median())
)

# 2e. Drop any row that still has nulls in critical columns after cleaning
before = len(df)
df = df.dropna(subset=["date", "sales", "profit", "region", "category", "product"])
print(f" - Dropped {before - len(df)} rows with unrecoverable missing values")

# 2f. Add helper columns used throughout the analysis
df["year_month"] = df["date"].dt.to_period("M").astype(str)

print(f"Clean shape: {df.shape}")


# ---------------------------------------------------------------------------
# 3. MONTHLY SALES TRENDS
# ---------------------------------------------------------------------------
print("\nComputing monthly sales trends...")
monthly_sales = df.groupby("year_month")["sales"].sum().reset_index()
monthly_sales = monthly_sales.sort_values("year_month")
print(monthly_sales.tail())  # quick sanity check in the console


# ---------------------------------------------------------------------------
# 4. TOP 5 PRODUCTS BY PROFIT
# ---------------------------------------------------------------------------
print("\nComputing top 5 products by profit...")
top_products = (
    df.groupby("product")["profit"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)
print(top_products)


# ---------------------------------------------------------------------------
# 5. REGION-WISE PERFORMANCE
# ---------------------------------------------------------------------------
print("\nComputing region-wise performance...")
region_performance = (
    df.groupby("region")
    .agg(total_sales=("sales", "sum"), total_profit=("profit", "sum"), orders=("order_id", "count"))
    .sort_values("total_sales", ascending=False)
    .reset_index()
)
print(region_performance)


# ---------------------------------------------------------------------------
# 6. BASIC STATS SUMMARY (printed for the viva / report)
# ---------------------------------------------------------------------------
print("\n--- Basic Stats Summary ---")
print(f"Total revenue: {df['sales'].sum():,.2f}")
print(f"Total profit: {df['profit'].sum():,.2f}")
print(f"Average order value: {df['sales'].mean():,.2f}")
print(f"Overall profit margin: {(df['profit'].sum() / df['sales'].sum()) * 100:.2f}%")


# ---------------------------------------------------------------------------
# 7. CHART 1 — Monthly Sales Trend (line chart)
# ---------------------------------------------------------------------------
plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly_sales, x="year_month", y="sales", marker="o", color="steelblue")
plt.xticks(rotation=45, ha="right")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/1_monthly_sales_trend.png", dpi=150)
plt.close()


# ---------------------------------------------------------------------------
# 8. CHART 2 — Top 5 Products by Profit (bar chart)
# ---------------------------------------------------------------------------
plt.figure(figsize=(8, 5))
sns.barplot(data=top_products, x="profit", y="product", hue="product", palette="viridis", legend=False)
plt.title("Top 5 Products by Total Profit")
plt.xlabel("Total Profit")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/2_top5_products_by_profit.png", dpi=150)
plt.close()


# ---------------------------------------------------------------------------
# 9. CHART 3 — Region-wise Sales vs Profit (grouped bar chart)
# ---------------------------------------------------------------------------
region_melted = region_performance.melt(
    id_vars="region", value_vars=["total_sales", "total_profit"],
    var_name="metric", value_name="amount"
)
plt.figure(figsize=(8, 5))
sns.barplot(data=region_melted, x="region", y="amount", hue="metric", palette="Set2")
plt.title("Region-wise Sales vs Profit")
plt.xlabel("Region")
plt.ylabel("Amount")
plt.legend(title="Metric")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/3_region_sales_vs_profit.png", dpi=150)
plt.close()


# ---------------------------------------------------------------------------
# 10. CHART 4 — Category-wise Profit Distribution (box plot)
# ---------------------------------------------------------------------------
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="category", y="profit", hue="category", palette="coolwarm", legend=False)
plt.title("Profit Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Profit per Order")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/4_profit_distribution_by_category.png", dpi=150)
plt.close()

print(f"\nAll 4 charts saved to the '{OUTPUT_DIR}/' folder.")
print("Done.")
