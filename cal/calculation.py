"""This is our cal base class / Abstract Class"""


class Calculation:
    """Calculation class"""

    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

    def just_for_too_few_methods(self):
        """just for too few methods"""

    @classmethod
    def create(cls, value_a, value_b):
        """CREATE"""
        return cls(value_a, value_b)
