"""Testing the Calculator"""
import pprint

import pytest

from calculator.calculator import Calculator


# @pytest.fixture
# def clear_history():
#     """clear history"""
#     Calculator.clear_history()
# To remove the warning by pylint,
# I removed the clear function above
# Instead, I make all the test function do clear firstly

def test_calculator_add():
    """Testing the Add function of the calculator"""
    Calculator.clear_history()
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    pprint.pprint(Calculator.history)


def test_clear_history():
    """clear history"""
    Calculator.clear_history()
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.clear_history() is True
    assert Calculator.history_count() == 0


def test_count_history():
    """count history"""
    Calculator.clear_history()
    assert Calculator.history_count() == 0
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.history_count() == 2


def test_get_last_calculation_result():
    """get last history"""
    Calculator.clear_history()
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_last_calculation_added_to_history() == 5


def test_get_first_calculation_result():
    """get first history"""
    Calculator.clear_history()
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_first_calculation_added_to_history() == 4


def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    Calculator.clear_history()
    assert Calculator.subtract_number(1, 2) == -1


def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    Calculator.clear_history()
    assert Calculator.multiply_numbers(1, 2) == 2


def test_zero_division():
    """Testing the division function of the calculator"""
    with pytest.raises(ZeroDivisionError):
        Calculator.division_numbers(1, 0)
