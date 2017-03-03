import unittest
from calculate.calculate import Calculate


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))

    def test_assert_raises(self):
        with self.assertRaises(AttributeError):
            [].get

if __name__ == "__main__":
    unittest.main()