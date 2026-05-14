# Contributing to TypeFx

Thank you for your interest in contributing! Here's how you can help.

## Development Setup

```bash
git clone https://github.com/rkriad585/PyTypeFx.git
cd PyTypeFx
pip install -e .
```

## Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_banners.py -v

# Run with coverage
python -m pytest --cov=typefx tests/
```

## Code Style

- Follow PEP 8 conventions
- Use descriptive variable names
- Add type hints to all function signatures
- Keep backward compatibility — new params should have defaults
- All imports in `typefx/__init__.py` must be explicit (no star imports)

## Adding Features

### Adding a new ASCII animal

1. Add the art string to the `ANIMALS` dict in `typefx/banners.py`
2. Add a test in `tests/test_banners.py`
3. Add the demo in `main.py`

### Adding a new banner function

1. Add the function in `typefx/banners.py`
2. Export it in `typefx/__init__.py` (both import and `__all__`)
3. Add tests in `tests/test_banners.py`
4. Update `docs/api.md` with the function signature
5. Add a demo call in `main.py`

### Adding a new kaomoji category

1. Add entries to the `KAOMOJI` dict in `typefx/banners.py`
2. Add a test verifying the new category works

### Adding a new color or style

1. Add the ANSI code in `typefx/colors.py`
2. Add the style preset in `typefx/styles.py`
3. Export in `typefx/__init__.py`

## Pull Request Process

1. Ensure all tests pass: `python -m pytest`
2. Add tests for new functionality
3. Update relevant documentation
4. Describe your changes clearly in the PR

## Reporting Issues

Open an issue at https://github.com/rkriad585/PyTypeFx/issues with:
- A clear description
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
