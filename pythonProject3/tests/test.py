import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 2, 2) == 4

    def test_multiply_success(self):
        assert self.calc.multiply(self, 3, 3) == 9

    def test_division_success(self):
        assert self.calc.division(self, 16, 4) == 4

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 8, 5) == 3