# """Testing the Calculator"""
# import pytest
# from calculator.calculator import Calculator
#
#
# def test_calculator_result():
#     """testing calculator result is 0"""
#     calc = Calculator()
#     assert calc.result == 0
#
# def test_zero_division():
#     """Testing the division function of the calculator"""
#     # AAA-Arrange by instantiating the calc class
#     calc = Calculator()
#     #AAA-Act by calling the method to be tested
#     with pytest.raises(ZeroDivisionError):
#         calc.division_numbers(1,0)
# def test_calculator_add():
#     """Testing the Add function of the calculator"""
#     # AAA-Arrange by instantiating the calc class
#     calc = Calculator()
#     # AAA-Act by calling the method to be tested
#     calc.add_number(4)
#     #AAA-Assert that the results are correct
#     assert calc.result == 4
#
# def test_calculator_get_result():
#     """Testing the Get result method of the calculator"""
#     calc = Calculator()
#     assert calc.get_result() == 0
#
# def test_calculator_subtract():
#     """Testing the subtract method of the calculator"""
#     calc = Calculator()
#     calc.subtract_number(1)
#     assert calc.get_result() == -1
# def test_calculator_multiply():
#     """ tests multiplication of two numbers"""
#     calc = Calculator()
#     result  = calc.multiply_numbers(1,2)
#     assert result == 2
# def test_calculator_division():
#     """ tests division of two numbers"""
#     calc = Calculator()
#     result = calc.division_numbers(2,1)
#     assert result == 2
"""Testing the Calculator"""
import pprint

import pytest

from calculator.calculator import Calculator


# this is how you define a function that will run each time you pass it to a test, it is called a fixture
@pytest.fixture
def clear_history():
    Calculator.clear_history()


def test_calculator_add(clear_history):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    pprint.pprint(Calculator.history)


def test_clear_history(clear_history):
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.clear_history() == True
    assert Calculator.history_count() == 0


def test_count_history(clear_history):
    assert Calculator.history_count() == 0
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.history_count() == 2


def test_get_last_calculation_result(clear_history):
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_last_calculation_added_to_history() == 5


def test_get_first_calculation_result(clear_history):
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_first_calculation_added_to_history() == 4


def test_calculator_subtract(clear_history):
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(1, 2) == -1


def test_calculator_multiply(clear_history):
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(1, 2) == 2
