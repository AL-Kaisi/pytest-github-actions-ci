"""
Calculator Module
This module provides basic arithmetic operations:
- Addition
- Subtraction
- Multiplication
- Division
"""


def add(a, b):
    """Returns the sum of two numbers"""
    return a + b


def subtract(a, b):
    """Returns the difference between two numbers"""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers"""
    return a * b


def divide(a, b):
    """Returns the quotient of two numbers; raises an error if dividing by zero"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
