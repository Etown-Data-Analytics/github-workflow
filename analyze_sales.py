"""
Sales Data Analysis Script

This script demonstrates basic data analytics with Python using pandas.
It analyzes sales data to provide insights on revenue, product categories, and trends.
"""

import pandas as pd
import argparse


def load_data(filepath: str) -> pd.DataFrame:
    """Load sales data from CSV file."""
    try:
        df = pd.read_csv(filepath)
        df['date'] = pd.to_datetime(df['date'])
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file not found: {filepath}")
    except Exception as e:
        raise Exception(f"Error loading data: {e}")


def analyze_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Analyze sales data by product category."""
    category_analysis = df.groupby('category').agg({
        'revenue': 'sum',
        'quantity': 'sum',
        'product': 'count'
    }).round(2)
    category_analysis.columns = ['Total Revenue', 'Total Quantity', 'Number of Transactions']
    return category_analysis.sort_values('Total Revenue', ascending=False)


def get_top_products(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Get top N products by revenue."""
    product_analysis = df.groupby('product').agg({
        'revenue': 'sum',
        'quantity': 'sum'
    }).round(2)
    product_analysis.columns = ['Total Revenue', 'Total Quantity']
    return product_analysis.sort_values('Total Revenue', ascending=False).head(n)


def calculate_daily_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate daily total revenue."""
    daily_revenue = df.groupby('date').agg({
        'revenue': 'sum',
        'quantity': 'sum'
    }).round(2)
    daily_revenue.columns = ['Total Revenue', 'Total Items Sold']
    return daily_revenue


def generate_summary_stats(df: pd.DataFrame) -> dict:
    """Generate overall summary statistics."""
    return {
        'total_revenue': round(df['revenue'].sum(), 2),
        'total_transactions': len(df),
        'total_quantity_sold': df['quantity'].sum(),
        'average_transaction_value': round(df['revenue'].mean(), 2),
        'date_range': f"{df['date'].min().date()} to {df['date'].max().date()}"
    }


def print_analysis_report(df: pd.DataFrame, verbose: bool = False):
    """Print comprehensive analysis report."""
    print("=" * 60)
    print("SALES DATA ANALYSIS REPORT")
    print("=" * 60)

    # Summary Statistics
    summary = generate_summary_stats(df)
    print("\n📊 SUMMARY STATISTICS")
    print("-" * 60)
    print(f"Total Revenue:            ${summary['total_revenue']:,.2f}")
    print(f"Total Transactions:       {summary['total_transactions']}")
    print(f"Total Items Sold:         {summary['total_quantity_sold']}")
    print(f"Avg Transaction Value:    ${summary['average_transaction_value']:,.2f}")
    print(f"Date Range:               {summary['date_range']}")

    # Category Analysis
    print("\n📦 REVENUE BY CATEGORY")
    print("-" * 60)
    category_data = analyze_by_category(df)
    print(category_data.to_string())

    # Top Products
    print("\n🏆 TOP 5 PRODUCTS BY REVENUE")
    print("-" * 60)
    top_products = get_top_products(df, n=5)
    print(top_products.to_string())

    if verbose:
        print("\n📅 DAILY REVENUE BREAKDOWN")
        print("-" * 60)
        daily_data = calculate_daily_revenue(df)
        print(daily_data.to_string())

    print("\n" + "=" * 60)


def main():
    """Main function to run the sales analysis."""
    parser = argparse.ArgumentParser(
        description='Analyze sales data and generate insights'
    )
    parser.add_argument(
        '--data',
        type=str,
        default='data/sales_data.csv',
        help='Path to sales data CSV file (default: data/sales_data.csv)'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed daily breakdown'
    )

    args = parser.parse_args()

    # Load and analyze data
    print(f"Loading data from: {args.data}")
    df = load_data(args.data)
    print(f"✓ Loaded {len(df)} records\n")

    # Generate and print report
    print_analysis_report(df, verbose=args.verbose)


if __name__ == "__main__":
    main()
