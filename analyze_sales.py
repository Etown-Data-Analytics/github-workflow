import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])
    return df

def main():
    # Load the data
    df = load_data('data/sales_data.csv')
    print(f"Loaded {len(df)} records\n")

    # --- Summary ---
    print("=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Total Revenue:       ${df['revenue'].sum():,.2f}")
    print(f"Total Transactions:  {len(df)}")
    print(f"Total Items Sold:    {df['quantity'].sum()}")
    print(f"Avg Transaction:     ${df['revenue'].mean():,.2f}")
    print(f"Date Range:          {df['date'].min().date()} to {df['date'].max().date()}")
    
if __name__ == "__main__":
    main()
