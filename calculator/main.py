""" Calculator homework"""
# Dairui Zhang

class Calculator:
    """ Calculator Class"""
    result = 0
    def __init__(self):
        pass

    def get_result(self):
        """ Get Result """
        return self.result
    def add_number(self, value_a:float):
        """ Add """
        self.result = self.result + value_a
        return self.result
    def subtract_number(self, value_a:float):
        """ Subtract """
        self.result = self.result - value_a
        return self.result
    def multiply_numbers(self, value_a:float, value_b:float):
        """ Multiply """
        self.result = value_a * value_b
        return self.result
    def division_numbers(self, value_a:float, value_b:float):
        """ Division """
        # if value_b == 0:
        #     raise Exception(ZeroDivisionError)
        self.result = round(value_a / value_b, 9)
        return  self.result
