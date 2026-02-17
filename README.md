# 📊 GitHub Workflow Template - Sales Data Analytics

[![CI - Lint and Test](https://github.com/Etown-Data-Analytics/github-workflow/actions/workflows/ci.yml/badge.svg)](https://github.com/Etown-Data-Analytics/github-workflow/actions/workflows/ci.yml)
[![Run Data Analysis](https://github.com/Etown-Data-Analytics/github-workflow/actions/workflows/analyze.yml/badge.svg)](https://github.com/Etown-Data-Analytics/github-workflow/actions/workflows/analyze.yml)

A template repository demonstrating GitHub workflows and best practices using a simple Python data analytics project. Perfect for learning GitHub Actions, CI/CD, and collaborative development workflows.

## 🎯 Purpose

This template demonstrates:
- ✅ **GitHub Actions workflows** for CI/CD
- ✅ **Automated testing** with pytest
- ✅ **Code quality checks** with flake8
- ✅ **Python data analytics** using pandas
- ✅ **Project structure** best practices
- ✅ **Documentation** standards

## 📁 Project Structure

```
github-workflow/
├── .github/
│   └── workflows/
│       ├── ci.yml              # Continuous Integration workflow
│       └── analyze.yml         # Data analysis workflow
├── data/
│   └── sales_data.csv          # Sample sales data
├── tests/
│   ├── __init__.py
│   └── test_analyze_sales.py  # Unit tests
├── analyze_sales.py            # Main analysis script
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository** (or use as template):
   ```bash
   git clone https://github.com/Etown-Data-Analytics/github-workflow.git
   cd github-workflow
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Running the Analysis

Basic usage:
```bash
python analyze_sales.py
```

With detailed output:
```bash
python analyze_sales.py --verbose
```

Using custom data file:
```bash
python analyze_sales.py --data path/to/your/data.csv
```

### Running Tests

Run all tests:
```bash
pytest tests/
```

Run tests with coverage:
```bash
pytest tests/ -v --cov=. --cov-report=term-missing
```

### Code Quality Checks

Run linting:
```bash
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

## 📊 Sample Output

The analysis script provides:
- **Summary Statistics**: Total revenue, transactions, items sold
- **Category Analysis**: Revenue breakdown by product category
- **Top Products**: Best-selling products by revenue
- **Daily Breakdown**: Daily revenue trends (with --verbose flag)

## 🔄 GitHub Workflows

### CI Workflow (`ci.yml`)

Triggers on:
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches

Actions:
1. **Lint**: Check code quality with flake8
2. **Test**: Run tests on Python 3.9, 3.10, and 3.11
3. **Coverage**: Generate and upload coverage reports

### Data Analysis Workflow (`analyze.yml`)

Triggers on:
- Push to `main` branch
- Daily schedule (9 AM UTC)
- Manual workflow dispatch

Actions:
1. Run the sales analysis
2. Generate analysis report
3. Upload results as artifacts

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Start for Contributors

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest tests/`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📚 Learning Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Python pandas Documentation](https://pandas.pydata.org/docs/)
- [pytest Documentation](https://docs.pytest.org/)
- [Git Workflow Guide](https://www.atlassian.com/git/tutorials/comparing-workflows)

## 📝 License

This project is open source and available under the MIT License.

## 🎓 Educational Use

This template is designed for educational purposes. Feel free to:
- Use it as a starting point for your projects
- Modify it to fit your needs
- Share it with others learning GitHub workflows

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Happy coding and analyzing! 📊✨**
