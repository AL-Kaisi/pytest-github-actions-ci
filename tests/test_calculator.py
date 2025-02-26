"""
Unit Tests for Calculator Module
Using Pytest to test:
- Addition
- Subtraction
- Multiplication
- Division (including division by zero)
"""

import pytest
from app.calculator import add, subtract, multiply, divide


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    """Test addition function"""
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (-1, -1, 0),
    (10, 5, 5)
])
def test_subtract(a, b, expected):
    """Test subtraction function"""
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, -1, 1),
    (0, 10, 0)
])
def test_multiply(a, b, expected):
    """Test multiplication function"""
    assert multiply(a, b) == expected


def test_divide():
    """Test division function, including division by zero"""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    with pytest.raises(ValueError):
        divide(10, 0)
