# """ Calculator homework"""
# # Dairui Zhang
#
# class Calculator:
#     """ Calculator Class"""
#     result = 0
#     def __init__(self):
#         pass
#
#     def get_result(self):
#         """ Get Result """
#         return self.result
#     def add_number(self, value_a:float):
#         """ Add """
#         self.result = self.result + value_a
#         return self.result
#     def subtract_number(self, value_a:float):
#         """ Subtract """
#         self.result = self.result - value_a
#         return self.result
#     def multiply_numbers(self, value_a:float, value_b:float):
#         """ Multiply """
#         self.result = value_a * value_b
#         return self.result
#     def division_numbers(self, value_a:float, value_b:float):
#         """ Division """
#         # if value_b == 0:
#         #     raise Exception(ZeroDivisionError)
#         self.result = round(value_a / value_b, 9)
#         return  self.result
""" This is the increment function"""
# first import the addition namespace
from calculation.addition import Addition
from calculation.subtraction import Subtraction
from calculation.multiplication import Multiplication


class Calculator:
    """ This is the Calculator class"""
    # this is the calculator static property
    history = []

    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        return Calculator.history[0].getResult()

    @staticmethod
    def clear_history():
        Calculator.history.clear()
        return True

    @staticmethod
    def history_count():
        return len(Calculator.history)

    @staticmethod
    def add_calculation_to_history(calculation):
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        # -1 gets the last item added to the list automaticly and you can expect it to have the get result method
        return Calculator.history[-1].getResult()

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        # create an addition object using the factory we created on the calculation class
        addition = Addition.create(value_a, value_b)
        # addition = Addition(value_a,value_b) <-this is not good but will work.  It will be repeated too much
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    # this is an example of a calling method
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        # create an subtraction object using the factory we created on the calculation class
        subtraction = Subtraction.create(value_a, value_b)
        # addition = Addition(value_a,value_b) <-this is not good but will work.  It will be repeated too much
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        # this is a shorthand way to create the multiplication object and added it the history in one line
        Calculator.add_calculation_to_history(Multiplication.create(value_a, value_b))
        return Calculator.get_result_of_last_calculation_added_to_history()