"""Unit tests for the addition functionality of the calculator."""


from app.addition import add


def test_addition():
    """
       Test the addition functionality of the calculator with various inputs:
       simple addition, negative numbers, zero, and floating-point addition.
       """


    assert add (2, 3) == 5          # Test simple addition
    assert add (-1, -1) == -2                 # Test with negative numbers
    assert add (0, 5) == 5          # Test with zero
    assert add (1.5, 2.5) == 4.0    # Test with floating points
