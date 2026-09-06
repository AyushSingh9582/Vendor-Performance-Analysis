# Vendor Performance Analysis
Evaluates vendor metrics from raw inventory, purchase, and sales data to support vendor selection, profitability analysis, and pricing optimization.

## Tech Stack
- Database: SQLite
- Language: Python
- Data Manipulation: Pandas, NumPy
- Visualization: Matplotlib, Seaborn
- Statistics: SciPy (`scipy.stats`)

## Data Pipeline
Raw data lives in an SQLite database (`inventory.db`) with tables: `begin_inventory`, `end_inventory`, `purchases`, `purchase_prices`, `sales`, `vendor_invoice`.

`get_vendor.py` runs the ETL process:

1. Extract & merge — SQL CTEs aggregate purchase quantities, sales dollars, and freight costs into a single dataframe.
2. Clean — handles missing values and trims string inconsistencies.
3. Calculate KPIs — `GrossProfit`, `ProfitMargin`, `StockTurnover`, `SalestoPurchaseRatio`.
4. Load — writes the result to a new `vendor_sales_summary` table.

## Analysis

Done in `Vendor Performance Analysis.ipynb`:

- Summary statistics on `TotalSalesDollars`, `TotalPurchaseDollars`, `Volume`, and calculated KPIs.
- Vendor contribution charts — donut charts (Top 10 vendors by purchase %) and Pareto charts (cumulative contribution).
- Statistical inference — KDE histograms comparing profit margin distributions between top and bottom vendors, followed by a two-sample t-test (unequal variances) to test whether the difference between upper- and lower-quartile vendors (by total sales) is significant.

## How to Run

```bash
git clone https://github.com/YourUsername/vendor-performance-analysis.git
cd vendor-performance-analysis
pip install pandas numpy matplotlib seaborn scipy
python get_vendor.py
jupyter notebook "Vendor Performance Analysis.ipynb"
```

## Key Findings

- *[Add your t-test result, e.g. "Rejected the null hypothesis — top-quartile vendors have significantly higher profit margins (p < 0.05)"]*
- *[Add your Pareto result, e.g. "Top 10 vendors account for 65.69% of total purchase contribution"]*

---
Author: Ayush
