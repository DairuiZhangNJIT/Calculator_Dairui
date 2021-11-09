"""DIVISION"""
from cal.calculation import Calculation


class Division(Calculation):
    """The addition class has one method to get the result of the the cal A and B come from
    the cal parent class"""

    def get_result(self):
        """GET RESULT"""
        return self.value_a / self.value_b
