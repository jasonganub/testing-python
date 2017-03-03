import unittest
from calculate.calculate import Calculate


class TestCalculate(unittest.TestCase):
    def SetUp(self):
        self.calc = Calculate()
