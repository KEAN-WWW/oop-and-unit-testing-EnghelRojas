"""Unit tests for the subtraction functionality of the calculator."""

from app.Subtraction import subtract


def test_subtraction():
    """
    Test the subtraction functionality of the calculator with various inputs:
    positive results, negative results, zero, and floating-point subtraction.
    """

    assert subtract(10, 5) == 5  # Test positive result
    assert subtract(5, 10) == -5  # Test negative result
    assert subtract(0, 5) == -5  # Test subtraction with zero
    assert subtract(3.5, 1.5) == 2.0  # Test floating-point subtraction
