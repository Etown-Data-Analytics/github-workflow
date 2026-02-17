# Contributing to GitHub Workflow Template

Thank you for your interest in contributing to this project! This document provides guidelines and instructions for contributing.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)

## 🤝 Code of Conduct

This project follows a simple code of conduct:
- Be respectful and inclusive
- Welcome newcomers and beginners
- Provide constructive feedback
- Focus on what is best for the community

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/github-workflow.git
   cd github-workflow
   ```
3. **Set up the development environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/Etown-Data-Analytics/github-workflow.git
   ```

## 🎯 How to Contribute

### Types of Contributions

We welcome various types of contributions:

- 🐛 **Bug Reports**: Report issues or bugs you find
- ✨ **Feature Requests**: Suggest new features or improvements
- 📝 **Documentation**: Improve or add documentation
- 💻 **Code**: Fix bugs or add new features
- 🧪 **Tests**: Add or improve test coverage
- 🎨 **Examples**: Add more data analysis examples

### Reporting Bugs

When reporting bugs, please include:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected vs actual behavior
- Python version and OS
- Any relevant error messages or logs

### Suggesting Features

When suggesting features:
- Explain the problem you're trying to solve
- Describe your proposed solution
- Consider if it fits the project's educational purpose
- Provide examples if possible

## 🔄 Development Workflow

1. **Sync your fork** with upstream:
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**:
   - Write clean, documented code
   - Follow the coding standards below
   - Add tests for new functionality

4. **Test your changes**:
   ```bash
   pytest tests/ -v
   flake8 .
   ```

5. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   **Commit message format**:
   - Use imperative mood ("Add feature" not "Added feature")
   - Keep first line under 50 characters
   - Add detailed description if needed

6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request** on GitHub

## 📏 Coding Standards

### Python Style

- Follow [PEP 8](https://pep8.org/) style guide
- Maximum line length: 127 characters
- Use descriptive variable names
- Add docstrings to functions and classes
- Use type hints where appropriate

### Code Quality

Run these checks before submitting:

```bash
# Linting
flake8 . --count --max-complexity=10 --max-line-length=127 --statistics

# Type checking (optional but recommended)
mypy analyze_sales.py --ignore-missing-imports
```

### Documentation

- Update README.md if adding features
- Add docstrings to new functions
- Include usage examples for new features
- Keep documentation clear and beginner-friendly

## 🧪 Testing Guidelines

### Writing Tests

- Place tests in the `tests/` directory
- Name test files as `test_*.py`
- Use descriptive test function names
- Test both success and error cases
- Aim for good coverage of new code

### Test Structure

```python
def test_feature_name():
    """Brief description of what is being tested."""
    # Arrange - Set up test data
    data = create_test_data()
    
    # Act - Execute the function being tested
    result = function_to_test(data)
    
    # Assert - Check the result
    assert result == expected_value
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ -v --cov=. --cov-report=term-missing

# Run specific test file
pytest tests/test_analyze_sales.py -v

# Run specific test function
pytest tests/test_analyze_sales.py::test_load_data -v
```

## 🔀 Pull Request Process

### Before Submitting

- ✅ All tests pass locally
- ✅ Code follows style guidelines
- ✅ New code has tests
- ✅ Documentation is updated
- ✅ Commit messages are clear
- ✅ Branch is up to date with main

### PR Description

Include in your PR:
- **Summary**: What does this PR do?
- **Motivation**: Why is this change needed?
- **Changes**: What was changed?
- **Testing**: How was it tested?
- **Screenshots**: If applicable (for UI changes)

### PR Review Process

1. Automated checks will run (CI workflow)
2. Maintainers will review your code
3. Address any feedback or requested changes
4. Once approved, your PR will be merged

### After Merge

- Your contribution will be credited
- Consider watching the repo for updates
- Look for other issues you can help with

## 🎓 First Time Contributors

New to open source? We're here to help!

- Look for issues labeled `good first issue`
- Don't hesitate to ask questions
- Small contributions are welcome (even fixing typos!)
- Learn by doing - we all started somewhere

## 💡 Tips for Success

- **Start small**: Begin with documentation or small bug fixes
- **Ask questions**: If unsure, ask in the issue or PR
- **Be patient**: Reviews may take a few days
- **Learn from feedback**: Code reviews are learning opportunities
- **Stay engaged**: Respond to comments and questions

## 📞 Getting Help

- **Issues**: Open an issue on GitHub
- **Discussions**: Use GitHub Discussions for questions
- **Documentation**: Check the README and existing issues

## 🙏 Recognition

Contributors are recognized in:
- GitHub's contributor list
- Project documentation
- Release notes (for significant contributions)

---

Thank you for contributing to making this project better! Your efforts help others learn and grow. 🌟
