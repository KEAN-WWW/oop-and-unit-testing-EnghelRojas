


from app.addition import add
from app.Subtraction import subtract
from app.Multiplication import multiply
from app.Division import divide


class Calculator(object):
    """This module contains functions for performing arithmetic operations such as addition, subtraction, multiplication, and division."""

    @staticmethod
    def addition(val1, val2):
        return add(val1, val2)

    @staticmethod
    def subtraction(val1, val2):
        return subtract(val1, val2)

    @staticmethod
    def multiplication(val1, val2):
        return multiply(val1, val2)

    @staticmethod
    def division(val1, val2):
        return divide(val1, val2)