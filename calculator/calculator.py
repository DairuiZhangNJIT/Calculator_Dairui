""" This is the increment function"""
from cal.addition import Addition
from cal.division import Division
from cal.subtraction import Subtraction
from cal.multiplication import Multiplication


class Calculator:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        """Get first history"""
        return Calculator.history[0].get_result()

    @staticmethod
    def clear_history():
        """Clear history"""
        Calculator.history.clear()
        return True

    @staticmethod
    def history_count():
        """count history"""
        return len(Calculator.history)

    @staticmethod
    def add_calculation_to_history(calculation):
        """add to history"""
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        """get last history"""
        return Calculator.history[-1].get_result()

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        addition = Addition.create(value_a, value_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        Calculator.add_calculation_to_history(Multiplication.create(value_a, value_b))
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def division_numbers(value_a, value_b):
        """DIVISION"""
        Calculator.add_calculation_to_history(Division.create(value_a, value_b))
        return Calculator.get_result_of_last_calculation_added_to_history()
