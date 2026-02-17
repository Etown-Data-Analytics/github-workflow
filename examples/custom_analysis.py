# Example: Create your own analysis script
# This shows how you can extend the template with your own analysis

from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))
from analyze_sales import load_data  # noqa: E402

# Load the data
df = load_data('data/sales_data.csv')

# Your custom analysis here
# For example: Find the most expensive product
most_expensive = df.loc[df['price'].idxmax()]
print(f"Most expensive product: {most_expensive['product']} at ${most_expensive['price']}")

# Calculate profit margin (assuming 30% margin)
df['profit'] = df['revenue'] * 0.30
total_profit = df['profit'].sum()
print(f"Estimated total profit: ${total_profit:.2f}")

# Find products with low sales
low_sales = df[df['quantity'] < 10]
print("\nProducts with low sales (< 10 units):")
print(low_sales[['product', 'quantity', 'revenue']])
