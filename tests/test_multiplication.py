"""Unit tests for the multiplication functionality of the calculator."""

from app.Multiplication import multiply


def test_multiplication():
    """
       Test the multiplication functionality of the calculator with various inputs:
       positive numbers, negative numbers, zero, and floating-point multiplication.
       """
    assert multiply (3, 4) == 12  # Test positive numbers
    assert multiply (-2, 3) == -6  # Test with negative numbers
    assert multiply (0, 5) == 0  # Test multiplication by zero
    assert multiply (1.5, 2) == 3.0  # Test floating point multiplication
