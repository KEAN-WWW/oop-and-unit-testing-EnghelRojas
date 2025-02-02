"""Unit tests for the division functionality of the calculator."""
import pytest
from app.Division import divide

def test_division():
    """
    Test the division functionality of the calculator with various inputs:
    positive integers, negative numbers, float values, and division by 1.
    """

    # Test with positive integers
    assert divide(10, 2) == 5
    # Test with negative numbers
    assert divide(-10, 2) == -5
    # Test with float values
    assert divide(9.0, 3) == 3.0
    # Test division by 1
    assert divide(7, 1) == 7


def test_divide_zero_exception():
    """
    Test that the divide function raises a ZeroDivisionError
    when attempting to divide by zero.
    """
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
