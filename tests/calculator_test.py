"""Testing the Calculator"""
import pytest
from calculator.main import Calculator


def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_zero_division():
    """Testing the division function of the calculator"""
    # AAA-Arrange by instantiating the calc class
    calc = Calculator()
    #AAA-Act by calling the method to be tested
    with pytest.raises(ZeroDivisionError):
        calc.division_numbers(1,0)
def test_calculator_add():
    """Testing the Add function of the calculator"""
    # AAA-Arrange by instantiating the calc class
    calc = Calculator()
    # AAA-Act by calling the method to be tested
    calc.add_number(4)
    #AAA-Assert that the results are correct
    assert calc.result == 4

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    assert calc.get_result() == 0

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtract_number(1)
    assert calc.get_result() == -1
def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    calc = Calculator()
    result  = calc.multiply_numbers(1,2)
    assert result == 2
def test_calculator_division():
    """ tests division of two numbers"""
    calc = Calculator()
    result = calc.division_numbers(2,1)
    assert result == 2
