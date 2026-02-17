"""
Unit tests for the sales data analysis script.
"""

import pytest
import pandas as pd
from pathlib import Path
import sys

# Add parent directory to path to import analyze_sales
sys.path.insert(0, str(Path(__file__).parent.parent))
from analyze_sales import (  # noqa: E402
    load_data,
    analyze_by_category,
    get_top_products,
    calculate_daily_revenue,
    generate_summary_stats
)


@pytest.fixture
def sample_data():
    """Create sample sales data for testing."""
    data = {
        'date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03']),
        'product': ['Laptop', 'Mouse', 'Keyboard'],
        'category': ['Electronics', 'Electronics', 'Electronics'],
        'quantity': [2, 10, 5],
        'price': [1000.00, 25.00, 75.00],
        'revenue': [2000.00, 250.00, 375.00]
    }
    return pd.DataFrame(data)


def test_load_data():
    """Test loading data from CSV file."""
    df = load_data('data/sales_data.csv')
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert 'date' in df.columns
    assert 'revenue' in df.columns


def test_load_data_file_not_found():
    """Test error handling for missing file."""
    with pytest.raises(FileNotFoundError):
        load_data('nonexistent_file.csv')


def test_analyze_by_category(sample_data):
    """Test category analysis."""
    result = analyze_by_category(sample_data)
    assert isinstance(result, pd.DataFrame)
    assert 'Total Revenue' in result.columns
    assert 'Total Quantity' in result.columns
    assert len(result) > 0


def test_get_top_products(sample_data):
    """Test getting top products."""
    result = get_top_products(sample_data, n=2)
    assert isinstance(result, pd.DataFrame)
    assert len(result) <= 2
    assert result.iloc[0]['Total Revenue'] >= result.iloc[1]['Total Revenue']


def test_calculate_daily_revenue(sample_data):
    """Test daily revenue calculation."""
    result = calculate_daily_revenue(sample_data)
    assert isinstance(result, pd.DataFrame)
    assert 'Total Revenue' in result.columns
    assert len(result) == 3  # 3 days in sample data


def test_generate_summary_stats(sample_data):
    """Test summary statistics generation."""
    result = generate_summary_stats(sample_data)
    assert isinstance(result, dict)
    assert 'total_revenue' in result
    assert 'total_transactions' in result
    assert result['total_revenue'] == 2625.00
    assert result['total_transactions'] == 3
    assert result['total_quantity_sold'] == 17


def test_data_integrity():
    """Test that actual data file has expected structure."""
    df = load_data('data/sales_data.csv')
    required_columns = ['date', 'product', 'category', 'quantity', 'price', 'revenue']
    for col in required_columns:
        assert col in df.columns, f"Missing required column: {col}"

    # Check data types
    assert pd.api.types.is_datetime64_any_dtype(df['date'])
    assert pd.api.types.is_numeric_dtype(df['quantity'])
    assert pd.api.types.is_numeric_dtype(df['revenue'])
